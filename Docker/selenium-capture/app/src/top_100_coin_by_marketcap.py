
import logging
from logging_config import setup_logging

from selenium import webdriver
import time
import os
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import configparser


current_dir = os.path.dirname(os.path.abspath(__file__))

# Load cấu hình từ file app.conf
config_path = os.path.join(current_dir, 'app.conf')
config = configparser.ConfigParser()
config.read(config_path)

# Thiết lập cấu hình log
setup_logging()

# Tạo logger cho module này
logger = logging.getLogger(__name__)

def capture_top_100_coin_by_marketcap():
    if not os.path.exists('images'):
        os.makedirs('images')

    # Cấu hình cho Selenium WebDriver
    options = Options()
    # options.add_argument('--headless')  # Chạy trình duyệt ở chế độ không hiển thị (không mở cửa sổ trình duyệt)
    options.add_argument("--no-sandbox") # Vô hiệu hóa chế độ sandbox của Chrome.
    options.add_argument("--disable-dev-shm-usage") # Sử dụng ổ đĩa thay vì /dev/shm cho bộ nhớ tạm.
    #options.add_argument("--disable-gpu") # Vô hiệu hóa GPU. Cần thiết khi chạy Chrome headless trên một số hệ thống.
    #options.add_argument("--disable-extensions") # Vô hiệu hóa các tiện ích mở rộng (extensions) của Chrome.
    #options.add_argument("--disable-notifications") # Vô hiệu hóa thông báo từ trang web
    options.add_argument("--start-maximized") # Mở trình duyệt ở chế độ toàn màn hình.
    #options.add_argument("--disable-popup-blocking") # Vô hiệu hóa chặn popup.
    options.add_argument("--window-size=1920,11816") # Đặt kích thước cửa sổ trình duyệt.
    SELENIUM_REMOTE_URL = config['options']['SELENIUM_REMOTE_URL']
    
    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=options
    )

    try:
        # Truy cập trang coingecko.com
        driver.get('https://www.coingecko.com')

        # Chờ trang web tải xong
        time.sleep(5)  # Điều chỉnh thời gian nếu cần thiết

        # Lấy thời gian hiện tại UTC để đặt tên tệp
        now = datetime.utcnow()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

        # Đặt tên tệp ảnh chụp màn hình
        screenshot_filename = f'images/coingecko_top_100_coin_{timestamp}.png'

        # Tìm thẻ table
        table = driver.find_element(By.XPATH, "//table[@data-coin-table-target='table']")

        # Chụp màn hình và lưu lại
        # driver.save_screenshot(screenshot_filename)
        # Chụp hình thẻ table và lưu vào file
        table.screenshot(screenshot_filename)    

        logger.info(f'Đã lưu ảnh chụp màn hình vào {screenshot_filename}')

    finally:
        driver.quit()

# Gọi hàm này ở bất kỳ nơi nào cần chụp
capture_top_100_coin_by_marketcap()