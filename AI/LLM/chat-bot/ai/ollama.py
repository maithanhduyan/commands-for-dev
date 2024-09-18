import asyncio
from ollama import AsyncClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

async def send_message_to_ai(message, html_tg,driver,LLMODEL):
    __chat_id__ = html_tg
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
