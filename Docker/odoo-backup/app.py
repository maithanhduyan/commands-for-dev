import requests
import os
from datetime import datetime
import schedule
import time
import configparser

# Load cấu hình từ file backup.conf
config = configparser.ConfigParser()
config.read('backup.conf')

ODOO_URL = config['odoo']['url']
ODOO_DB = config['odoo']['db']
ODOO_USER = config['odoo']['user']
ODOO_PASSWORD = config['odoo']['password']

BACKUP_MASTER_PASSWORD = config['backup']['master_password']
BACKUP_FORMAT = config['backup']['format']

BACKUP_DIR = "./odoobackup"
os.makedirs(BACKUP_DIR, exist_ok=True)

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
        print(f"Backup request sent successfully at {date_time}.")
    else:
        print("Failed to send backup request.")

schedule.every().sunday.at("00:00").do(backup)

# test
# backup()

if __name__ == "__main__":
    print(datetime.now(), "Running Odoo backup ...")
    # Tạo công việc chạy backup mỗi tuần vào Chủ nhật lúc 0 giờ
    # schedule.every().sunday.at("00:00").do(backup)
    backup()
    
    # Loop : Vòng lặp chạy tác vụ
    while True:
        schedule.run_pending()
        time.sleep(5)
