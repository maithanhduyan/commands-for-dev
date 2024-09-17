from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import ollama
import configparser
import json
import asyncio
from ollama import AsyncClient

# 

# Load cấu hình từ file chatbot.conf
config = configparser.ConfigParser()
config.read('chatbot.conf')
WEB_URL = config['chatbot']['url']
USERNAME = config['chatbot']['username']
PASSWORD = config['chatbot']['password']

# For LLMs
LLMODEL = config['chatbot']['llmodel']

# Địa chỉ Selenium server (đang chạy trong Docker)
SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"

# Cấu hình trình duyệt
chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy ở chế độ headless (không mở cửa sổ trình duyệt)
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Khởi động trình duyệt và kết nối với Selenium server trong Docker
driver = webdriver.Remote(
    command_executor=SELENIUM_REMOTE_URL,
    options=chrome_options
)
# Chrome on your desktop
# driver = webdriver.Chrome(options=chrome_options)

async def send_message_to_ollama(message, chat_id):
    __chat_id__=chat_id
    # Gửi tin nhắn đến ollama
    response = await AsyncClient().chat(model=LLMODEL, messages=[
        {
            'role': 'user',
            'content': message,
        },
    ])

    # Trả lời cho khách hàng
    if response:

        # Nếu nhận tin từ ollama thì tìm chat_id và click vào
        driver.find_element(By.XPATH, f"//span[contains(@class, 'o_DiscussSidebarCategoryItem_name') and contains(text(), '#{__chat_id__}')]").click()

        print(response['message']['content'])

        # Tìm chatbox
        textarea = driver.find_element(By.XPATH, "//textarea[contains(@class, 'o_ComposerTextInput_textarea')]")

        # Sử dụng JavaScript để đặt nội dung trực tiếp vào chat box
        driver.execute_script(f"arguments[0].value = `{response['message']['content']}`;", textarea)

        # Focus vào chatbox
        textarea.click()

        # Gửi tin nhắn bằng cách nhấn phím Enter
        textarea.send_keys(Keys.RETURN)

        # Chuyển focus sang hộp thư đến và chờ tin nhắn tiếp theo
        driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()


async def main():
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

        # Khởi động Ollama
        message = {'role': 'user', 'content': ''}
        response = await AsyncClient().chat(model=LLMODEL, messages=[message])

        print("Ollama đã được khởi động với vai trò tư vấn bán hàng:", response)
        
        # Bắt đầu vòng lặp để theo dõi tin nhắn mới từ khách hàng
        while True:
            try:
                # Kiểm tra có tin nhắn mới từ khách hàng không. Focus vào hộp thư đến và đợi
                driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                
                # Tìm phần tử "LIVECHAT" có chứa khách hàng và số tin nhắn mới
                new_message = driver.find_element(By.XPATH, "//div[@class='o_DiscussSidebarCategory_content']//div[@class='o_DiscussSidebarCategoryItem_counter o_DiscussSidebarCategoryItem_item badge badge-pill']")

                if new_message:
                    print("Có khách hàng mới nhắn tin!")

                    # Tìm khách hàng đó
                    print(new_message.text)
                    new_message.click()
                    
                    # Tìm hộp chatbox
                    # chat_box = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[3]/div[1]/textarea[1]")

                    # Lấy tất cả các tin nhắn
                    client_messages = driver.find_elements(By.XPATH, "//div[@role='group' and @aria-label='Message']")
                    
                    # Lấy tin nhắn cuối cùng
                    last_message = client_messages[-1].text
                    print("Tin nhắn cuối cùng của khách hàng là:", last_message)

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
                    print("Khách truy cập web", chat_id)

                    # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ollama
                    asyncio.create_task(send_message_to_ollama(message_content,chat_id))
                    
                    # Focus vào Hộp thư đến. Đợi tin nhắn mới
                    driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()
                    
                    # Thêm thời gian chờ sau khi xử lý tin nhắn
                    await asyncio.sleep(1)

            except Exception as e:
                # Nếu không có tin nhắn mới hoặc gặp lỗi, bỏ qua và tiếp tục
                pass

            # Chờ một khoảng thời gian trước khi kiểm tra lại
            await asyncio.sleep(1)

    finally:
        # Đóng trình duyệt nếu cần thiết (hoặc không đóng nếu bạn muốn giữ mở liên tục)
        # driver.quit()
        pass

if __name__ == "__main__":
    asyncio.run(main())