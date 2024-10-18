import logging
from logging_config import setup_logging
from capture import take_capture
import time
import os
import schedule
import configparser
import pytz

# Lấy đường dẫn thư mục hiện tại của tệp
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load cấu hình từ file app.conf
config_path = os.path.join(current_dir, 'app.conf')
config = configparser.ConfigParser()
config.read(config_path)

# Định nghĩa múi giờ UTC
timezone = pytz.timezone('UTC')

# Thiết lập cấu hình log
setup_logging()

# Tạo logger cho module này
logger = logging.getLogger(__name__)

schedule.every().day.at("00:00").do(take_capture)

if __name__ == "__main__":
    logger.info("Take a picture")
    take_capture()
    
    # Loop : Vòng lặp chạy tác vụ
    while True:
        schedule.run_pending()
        time.sleep(60)

