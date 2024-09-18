import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ai.gemini import send_message_to_gemini
# from ai.openai import send_message_to_ai
# from ai.ollama import send_message_to_ai

async def webchat(config):
    # Load cấu hình
    WEB_URL = config['odoo_v15']['url']
    USERNAME = config['odoo_v15']['username']
    PASSWORD = config['odoo_v15']['password']
    LLMODEL = config['odoo_v15']['llmodel']
    API_KEY = config['google']['api_key']

    SELENIUM_REMOTE_URL = f"http://127.0.0.1:4444/wd/hub"

    # Cấu hình trình duyệt
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Chạy ở chế độ headless (không mở cửa sổ trình duyệt)
    # chrome_options.add_argument("--no-sandbox") # Vô hiệu hóa chế độ sandbox của Chrome.
    # chrome_options.add_argument("--disable-dev-shm-usage") # Sử dụng ổ đĩa thay vì /dev/shm cho bộ nhớ tạm.
    # chrome_options.add_argument("--disable-gpu") # Vô hiệu hóa GPU. Cần thiết khi chạy Chrome headless trên một số hệ thống.
    # chrome_options.add_argument("--disable-extensions") # Vô hiệu hóa các tiện ích mở rộng (extensions) của Chrome.
    # chrome_options.add_argument("--disable-notifications") # Vô hiệu hóa thông báo từ trang web
    chrome_options.add_argument("--start-maximized") # Mở trình duyệt ở chế độ toàn màn hình.
    # chrome_options.add_argument("--disable-popup-blocking") # Vô hiệu hóa chặn popup.
    # chrome_options.add_argument("--window-size=1920,1080") # Đặt kích thước cửa sổ trình duyệt.

    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=chrome_options
    )
    
    # Chrome on your desktop
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.set_window_size(1920, 1080)  # Điều chỉnh kích thước cửa sổ trình duyệt nếu cần

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
                # driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                
                # Tìm phần tử "LIVECHAT" có chứa khách hàng và số tin nhắn mới
                # live_chat_tag = driver.find_element(By.XPATH, "//div[contains(@class,'o_DiscussSidebarCategory o_DiscussSidebar_category o_DiscussSidebar_categoryLivechat')]")

                # client_list_tags = live_chat_tag.find_element(By.XPATH,"//div[contains(@class,'o_DiscussSidebarCategory_content')]")

                # new_messages = client_list_tags.find_element(By.XPATH,"//div[contains(@class,'o_DiscussSidebarCategoryItem_counter o_DiscussSidebarCategoryItem_item badge badge-pill')]")
                
                # # Sử dụng WebDriverWait để đợi phần tử xuất hiện
                # wait = WebDriverWait(driver, 10)
                
                # new_messages = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'o_DiscussSidebarCategoryItem o_DiscussSidebarCategory_item') and /div[contains(@class,'o_DiscussSidebarCategoryItem_counter o_DiscussSidebarCategoryItem_item badge badge-pill')] ]")))
                new_message = driver.find_element(By.XPATH, "//div[@class='o_DiscussSidebarCategory_content']//div[@class='o_DiscussSidebarCategoryItem_counter o_DiscussSidebarCategoryItem_item badge badge-pill']")
                if new_message:

                    # Tìm khách hàng đó. Click vào
                    client_tag = new_message.find_element(By.XPATH,"..")
                    print(f"{client_tag.text}")                    
                    # client_name_tag = client_tag.split("\n")
                    # print(f"{client_name_tag[0]}")                    
                    client_tag.click()
                    wait = WebDriverWait(driver, 1)
                    
                    # Lấy tin nhắn
                    client_messages = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='group' and @aria-label='Message']")))
                    # client_messages = driver.find_elements(By.XPATH, "//div[@role='group' and @aria-label='Message']")
                    
                    # Lấy phần tử cuối cùng từ danh sách
                    if client_messages:
                        last_message = client_messages[-1]
                        # print("", last_message.get_attribute("outerHTML"))
                        last_message_content = last_message.find_element(By.XPATH,".//div[contains(@class, 'o_Message_prettyBody')]/p").text
                        
                        # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ai chatbot
                        asyncio.create_task(send_message_to_ai(last_message_content,client_tag,driver,API_KEY))
                        
                        # Focus vào Hộp thư đến. Đợi tin nhắn mới
                        driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                        
                    # # Lấy nội dung văn bản của thẻ <span>
                    # customer_text = id_span.text
                    
                    # # Tách ID truy cập từ nội dung văn bản
                    # chat_id = customer_text.split('#')[-1]
                    # print(customer_text)

                    # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ai chatbot
                    # asyncio.create_task(send_message_to_ai(message_content,customer_text,driver,LLMODEL,API_KEY))
                    
                    # Focus vào Hộp thư đến. Đợi tin nhắn mới
                    # driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                    
                    # Thêm thời gian chờ sau khi xử lý tin nhắn
                    # await asyncio.sleep(1)

            except Exception as e:
                # Nếu không có tin nhắn mới hoặc gặp lỗi, bỏ qua và tiếp tục
                # print(e)
                pass

            # Chờ một khoảng thời gian trước khi kiểm tra lại
            # print('Chờ một khoảng thời gian trước khi kiểm tra lại')
            await asyncio.sleep(1)

    finally:
        print('Đóng trình duyệt nếu cần thiết (hoặc không đóng nếu bạn muốn giữ mở liên tục)')
        driver.quit()
        pass


async def send_message_to_ai(message ,html_tag,driver,API_KEY):
    # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ai chatbot
    print("Tin nhắn cuối cùng là:", message)
    print('gửi tin nhắn đến AI chatbot')
    response = await send_message_to_gemini(message,API_KEY)
    print('',html_tag.text)
    memo_tag = html_tag
    memo_tag.click()
    # Tìm chatbox
    textarea = driver.find_element(By.XPATH, "//textarea[contains(@class, 'o_ComposerTextInput_textarea')]")

    # Sử dụng JavaScript để đặt nội dung trực tiếp vào chat box
    driver.execute_script(f"arguments[0].value = `{response}`;", textarea)
    
    # Focus vào chatbox
    textarea.click()

    # Gửi tin nhắn bằng cách nhấn phím Enter
    textarea.send_keys(Keys.RETURN)

    # Chuyển focus sang hộp thư đến và chờ tin nhắn tiếp theo
    driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()