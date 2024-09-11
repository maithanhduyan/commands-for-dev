import requests
import os
from datetime import datetime
import schedule
import time
import logging
import configparser

# Load cấu hình từ file backup.conf
config = configparser.ConfigParser()
config.read('backup.conf')

# Thư mục lưu log file
LOG_DIR = "./logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Thiết lập cấu hình logging
logging.basicConfig(filename=f"{LOG_DIR}/backup.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ODOO_URL = config['odoo']['url']
ODOO_DB = config['odoo']['db']
ODOO_USER = config['odoo']['user']
ODOO_PASSWORD = config['odoo']['password']

BACKUP_MASTER_PASSWORD = config['backup']['master_password']
BACKUP_FORMAT = config['backup']['format']

BACKUP_DIR = "./storage"
MAX_BACKUP_FILES = 30
os.makedirs(BACKUP_DIR, exist_ok=True)

# Thông tin cấu hình email
email_config = {
    'subject': config['email']['subject'],
    'html_body': '',
    'to_address': ['tiachop0102@gmail.com', 'tayafood@gmail.com', 'anmtt@tayafood.com', 'admin@tayafood.com'],
    'smtp_server': config['email']['smtp_server'],
    'smtp_port': config['email']['smtp_port'],
    'smtp_username': config['email']['smtp_username'],
    'smtp_password': config['email']['smtp_password']
}

def backup():
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    data = {
        'master_pwd': BACKUP_MASTER_PASSWORD,
        'name': ODOO_DB,
        'backup_format': BACKUP_FORMAT,
    }
    response = requests.post(
        f"{ODOO_URL}/web/database/backup",
        auth=(ODOO_USER, ODOO_PASSWORD),
        data=data
    )
    if response.status_code == 200:
        with open(f"{BACKUP_DIR}/{ODOO_DB}_{date_time}.zip", "wb") as file:
            file.write(response.content)
        logging.info(f"Backup request sent successfully at {date_time}.")
        cleanup_old_backups()
    else:
        logging.error("Failed to send backup request.")

def cleanup_old_backups():
    files = sorted(
        [os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR)],
        key=os.path.getctime
    )
    if len(files) > MAX_BACKUP_FILES:
        for file in files[:-MAX_BACKUP_FILES]:
            os.remove(file)
            logging.info(f"Deleted old backup: {file}")

schedule.every().day.at("00:00").do(backup)

# test
# backup()

if __name__ == "__main__":
    logging.info("Running Odoo backup ...")
    # Tạo công việc chạy backup mỗi tuần vào Chủ nhật lúc 0 giờ
    # schedule.every().sunday.at("00:00").do(backup)
    backup()
    
    # Loop : Vòng lặp chạy tác vụ
    while True:
        schedule.run_pending()
        time.sleep(5)
