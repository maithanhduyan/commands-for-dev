
import logging
from logging_config import setup_logging

from selenium import webdriver
import time
import os
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import configparser

# Lấy đường dẫn thư mục hiện tại của tệp
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load cấu hình từ file app.conf
config_path = os.path.join(current_dir, 'app.conf')
config = configparser.ConfigParser()
config.read(config_path)

# Thiết lập cấu hình log
setup_logging()

# Tạo logger cho module này
logger = logging.getLogger(__name__)

def take_capture():
    # Kiểm tra và tạo thư mục 'images' nếu chưa tồn tại
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

    # SELENIUM_REMOTE_URL = f"http://selenium:4444/wd/hub"
    SELENIUM_REMOTE_URL = config['options']['SELENIUM_REMOTE_URL']
    # Đường dẫn tới chromedriver (thay đổi đường dẫn cho phù hợp)
    # service = Service(executable_path='/path/to/chromedriver')

    # driver = webdriver.Chrome(service=service, options=options)
    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=options
    )

    # Chrome on your desktop
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.set_window_size(1920, 1080)  # Điều chỉnh kích thước cửa sổ trình duyệt nếu cần

    try:
        # Truy cập trang coingecko.com
        driver.get('https://www.coingecko.com')

        # Chờ trang web tải xong
        time.sleep(5)  # Điều chỉnh thời gian nếu cần thiết

        # Lấy thời gian hiện tại UTC để đặt tên tệp
        now = datetime.utcnow()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

        # Đặt tên tệp ảnh chụp màn hình
        screenshot_filename = f'images/coingecko_{timestamp}.png'

        # Chụp màn hình và lưu lại
        driver.save_screenshot(screenshot_filename)
        logger.info(f'Đã lưu ảnh chụp màn hình vào {screenshot_filename}')

    finally:
        driver.quit()
