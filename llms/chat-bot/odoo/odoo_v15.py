import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from ai.gemini import send_message_to_ai
# from ai.openai import send_message_to_ai
# from ai.ollama import send_message_to_ai

async def webchat(config):
    # Load cấu hình
    WEB_URL = config['odoo_v15']['url']
    USERNAME = config['odoo_v15']['username']
    PASSWORD = config['odoo_v15']['password']
    LLMODEL = config['odoo_v15']['llmodel']
    API_KEY = config['google']['api_key']

    SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"

    # Cấu hình trình duyệt
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Chạy ở chế độ headless (không mở cửa sổ trình duyệt)
    chrome_options.add_argument("--no-sandbox") # Vô hiệu hóa chế độ sandbox của Chrome.
    chrome_options.add_argument("--disable-dev-shm-usage") # Sử dụng ổ đĩa thay vì /dev/shm cho bộ nhớ tạm.
    chrome_options.add_argument("--disable-gpu") # Vô hiệu hóa GPU. Cần thiết khi chạy Chrome headless trên một số hệ thống.
    chrome_options.add_argument("--disable-extensions") # Vô hiệu hóa các tiện ích mở rộng (extensions) của Chrome.
    chrome_options.add_argument("--disable-notifications") # Vô hiệu hóa thông báo từ trang web
    # chrome_options.add_argument("--start-maximized") # Mở trình duyệt ở chế độ toàn màn hình.
    # chrome_options.add_argument("--disable-popup-blocking") # Vô hiệu hóa chặn popup.

    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=chrome_options
    )
    
    # Chrome on your desktop
    # driver = webdriver.Chrome(options=chrome_options)

    try:
        # Mở trang đăng nhập
        driver.get(WEB_URL)

        # Tìm và điền thông tin đăng nhập
        username_field = driver.find_element(By.NAME, "login")
        password_field = driver.find_element(By.NAME, "password")
        
        username_field.send_keys(USERNAME)  
        password_field.send_keys(PASSWORD)  
        
        # Gửi thông tin đăng nhập
        password_field.send_keys(Keys.RETURN)

        # Chờ đăng nhập thành công
        await asyncio.sleep(5)  # Chờ một vài giây để đăng nhập hoàn tất
        
        # Bắt đầu vòng lặp để theo dõi tin nhắn mới từ khách hàng
        while True:
            try:
                # Kiểm tra có tin nhắn mới từ khách hàng không. Focus vào hộp thư đến và đợi
                driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                
                # Tìm phần tử "LIVECHAT" có chứa khách hàng và số tin nhắn mới
                new_messages = driver.find_element(By.XPATH, "//div[@class='o_DiscussSidebarCategoryItem_counter o_DiscussSidebarCategoryItem_item badge badge-pill']")

                if new_messages:
                    # Tìm khách hàng đó. Click vào
                    new_messages.click()
                    print(f"Có khách hàng mới nhắn tin!{new_messages.text}")                    
                    
                    # Tìm id đã nhắn tin
                    # __id__ = driver.find_element(By.XPATH,'//div[@class="o_ThreadViewTopbar"]')
                    # if __id__:
                    #     print('có id',__id__)
                    # else:
                    #     print('Không tìm thấy')

                    # Lấy tin nhắn
                    client_messages = driver.find_elements(By.XPATH, "//div[@role='group' and @aria-label='Message']")
                    
                    # Lấy tin nhắn cuối cùng
                    last_message = client_messages[-1].text
                    # print("Tin nhắn cuối cùng của khách hàng là:", client_messages.text)

                    # Tách chuỗi dựa trên ký tự xuống dòng (\n)
                    parts = last_message.split("\n")

                    # Phần đầu tiên là tên người gửi
                    sender_name = parts[0]

                    # Phần cuối cùng là nội dung tin nhắn
                    message_content = parts[-1]

                    print("Tên người gửi:", sender_name)
                    print("Nội dung tin nhắn:", message_content)

                    # Lấy ID của Khách
                    # Tìm thẻ <span> chứa ID truy cập
                    id_span = driver.find_element(By.XPATH, "//span[contains(@class, 'o_DiscussSidebarCategoryItem_name') and contains(text(), 'Khách truy cập web')]")
                    
                    # Lấy nội dung văn bản của thẻ <span>
                    customer_text = id_span.text
                    
                    # Tách ID truy cập từ nội dung văn bản
                    chat_id = customer_text.split('#')[-1]
                    print(customer_text)

                    # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ollama
                    asyncio.create_task(send_message_to_ai(message_content,customer_text,driver,LLMODEL,API_KEY))
                    
                    # Focus vào Hộp thư đến. Đợi tin nhắn mới
                    # driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                    
                    # Thêm thời gian chờ sau khi xử lý tin nhắn
                    # await asyncio.sleep(1)

            except Exception as e:
                # Nếu không có tin nhắn mới hoặc gặp lỗi, bỏ qua và tiếp tục
                pass

            # Chờ một khoảng thời gian trước khi kiểm tra lại
            await asyncio.sleep(1)

    finally:
        # Đóng trình duyệt nếu cần thiết (hoặc không đóng nếu bạn muốn giữ mở liên tục)
        # driver.quit()
        pass
