import requests
import os
from datetime import datetime

# Thông tin cơ sở dữ liệu Odoo
ODOO_URL = "http://spexpress.online"
ODOO_DB = "spexpress_db"
ODOO_USER = "odoo"
ODOO_PASSWORD = "odoo15@2024"

# Thông tin backup
BACKUP_MASTER_PASSWORD = "4jpw-hi95-z25k"
BACKUP_FORMAT = "zip"

# Thư mục đích để lưu trữ backup
BACKUP_DIR = "./backup"
os.makedirs(BACKUP_DIR, exist_ok=True)

# Tạo ngày giờ cho tệp tin backup
date_time = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

# Tạo yêu cầu POST với các tham số
data = {
    'master_pwd': BACKUP_MASTER_PASSWORD,
    'name': ODOO_DB,
    'backup_format': BACKUP_FORMAT,
}

# Gửi yêu cầu POST đến trang quản lý cơ sở dữ liệu Odoo
response = requests.post(
    f"{ODOO_URL}/web/database/backup",
    auth=(ODOO_USER, ODOO_PASSWORD),
    data=data
)

# Kiểm tra kết quả
if response.status_code == 200:
    # Lưu file vào thư mục backup
    with open(f"{BACKUP_DIR}/{ODOO_DB}_{date_time}.zip", "wb") as file:
        file.write(response.content)
    print("Backup request sent successfully.")
else:
    print("Failed to send backup request.")
