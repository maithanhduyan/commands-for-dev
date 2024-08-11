import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import configparser
import google.generativeai as genai

# Load cấu hình từ file app.config
config = configparser.ConfigParser()
# config.read('app.config')
GOOGLE_GEMINI_API_KEY = 'AIzaSyA6gwmwIS6aha3xOWQD-MYidqwO9zgwDN4'

async def webchat(config):
    # Load cấu hình
    WEB_URL = 'http://localhost:8069//web/login'                                            #config['odoo_v17']['url']
    USERNAME = 'admin@company.com'                                           #config['odoo_v17']['username']
    PASSWORD = 'admin'                                           #config['odoo_v17']['password']
    API_KEY = 'AIzaSyA6gwmwIS6aha3xOWQD-MYidqwO9zgwDN4'     #config['google']['api_key']
    ON_DOCKER = False                                       #config['chatbot']['docker']

    SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"

    # Cấu hình trình duyệt
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Chạy ở chế độ headless (không mở cửa sổ trình duyệt)
    # chrome_options.add_argument("--no-sandbox") # Vô hiệu hóa chế độ sandbox của Chrome.
    # chrome_options.add_argument("--disable-dev-shm-usage") # Sử dụng ổ đĩa thay vì /dev/shm cho bộ nhớ tạm.
    # chrome_options.add_argument("--disable-gpu") # Vô hiệu hóa GPU. Cần thiết khi chạy Chrome headless trên một số hệ thống.
    # chrome_options.add_argument("--disable-extensions") # Vô hiệu hóa các tiện ích mở rộng (extensions) của Chrome.
    # chrome_options.add_argument("--disable-notifications") # Vô hiệu hóa thông báo từ trang web
    # chrome_options.add_argument("--start-maximized") # Mở trình duyệt ở chế độ toàn màn hình.
    # chrome_options.add_argument("--disable-popup-blocking") # Vô hiệu hóa chặn popup.

    # Khởi động trình duyệt và kết nối với Selenium server trong Docker
    # driver = webdriver.Remote(
    #     command_executor=SELENIUM_REMOTE_URL,
    #     options=chrome_options
    # )
    
    # Chrome on your desktop
    driver = webdriver.Chrome(options=chrome_options)

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
                new_messages = driver.find_element(By.XPATH, "//button[contains(@class, 'o-mail-DiscussSidebarChannel o-mail-DiscussSidebar-item') and .//div/span]")

                if new_messages:
                    # Tìm khách hàng đó. Click vào
                    print(f"Có khách hàng mới nhắn tin!")    
                    new_messages.click()
                    print(new_messages.text)                
                    # parent_new_messages = new_messages.find_element(By.XPATH, "..")
                    # parent_new_messages.click()
                    
                    # Tìm id đã nhắn tin
                    # __id__ = driver.find_element(By.XPATH,'//div[@class="o_ThreadViewTopbar"]')
                    # if __id__:
                    #     print('có id',__id__)
                    # else:
                    #     print('Không tìm thấy')

                    # Lấy tin nhắn

                    client_messages = driver.find_elements(By.XPATH, "//div[contains(@class, 'o-mail-Message')")
                    
                    # Lấy tin nhắn cuối cùng
                    last_message_tag = client_messages[-1]
                    last_message_content = last_message_tag.find_element(By.XPATH, "//div[contains(@class, 'o-mail-Message-content')]")
                    print("Tin nhắn cuối cùng của khách hàng là:", last_message_content.text)

                    # Tách chuỗi dựa trên ký tự xuống dòng (\n)
                    parts = last_message_content.split("\n")

                    # Phần đầu tiên là tên người gửi
                    sender_name = parts[0]

                    # Phần cuối cùng là nội dung tin nhắn
                    message_content = parts[-1]

                    print("Tên người gửi:", sender_name)
                    print("Nội dung tin nhắn:", message_content)

                    # Lấy ID của Khách
                    # Tìm thẻ <span> chứa ID truy cập
                    id_span = driver.find_element(By.XPATH, "//span[contains(@class, 'o-mail-DiscussSidebar-badge badge rounded-pill o-discuss-badge ms-1 me-3 fw-bold')]")
                    
                    # Lấy nội dung văn bản của thẻ <span>
                    customer_text = id_span.text
                    
                    # Tách ID truy cập từ nội dung văn bản
                    chat_id = customer_text.split('#')[-1]
                    print(customer_text)

                    # Gửi tác vụ xử lý tin nhắn không đồng bộ cho ollama
                    # asyncio.create_task(send_message_to_ai(message_content,customer_text,driver,LLMODEL,API_KEY))
                    
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

async def send_message_to_ai(message, html_tg, driver, LLMODEL , API_KEY):
    __chat_id__ = html_tg

    # Gửi tin nhắn đến gemini
    genai.configure(api_key=f'{API_KEY}')
    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.\nDạ em tên là Thúy! \nEm là tư vấn bán hàng ạ!\nNhân viên bán hàng của TAYAFOOD.COM.\nEm có thể trò chuyện bằng ngôn ngữ của nhiều nước trên thế giới.\nGiá hạt điều gói 25g hiện nay là 30.000 vnđ\nNếu muốn đặt hàng số lượng lớn của công ty em thì anh/chị có thể em theo địa chỉ email anmtt@tayafood.com ạ.\nGiao Hàng\nChúng em có giao hàng tận nơi. \nThanh toán đa dạng như COD, chuyển khoản.\nTrang web bán hàng của công ty em là: tayafood.com. \nAnh chị có thể truy cập TAYAFOOD.COM để biết thêm thông tin về các sản phẩm của công ty em ạ!.\nĐịa chỉ\nĐịa chỉ trụ sở chính: 5C2 Hoà Bình, Phường 3, Quận 11, Thành phố Hồ Chí Minh, Việt Nam.\nĐịa chỉ xưởng sản xuất: 815/4/3B Hương lộ 2, Phường Bình Trị Đông A, Quận Bình Tân, Thành Phố Hồ Chí Minh, Việt Nam.\nSố điện thoại của em (+84) 0945614800\nEmail: anmtt@tayafood.com\nEm chỉ bán các sản phẩm của TAYA FOOD thôi ạ! \nBên em có bán hạt điều nè, bột gia vị nè, các loại phụ gia trong chế biến và bảo quản thực phẩm nữa. \n**Chuyển giao công nghệ**\nNgoài ra công ty em còn có chuyển giao công nghệ, kỹ thuật máy móc cho các đối tác.\nCông ty của em có xuất khẩu số lượng lớn cho khách hàng nước ngoài như Mỹ, Đài Loan, Châu  âu ..\nSản Phẩm\nSản phẩm: Bột gia vị phô mai VRICH (10g x 1000 gói) : Bột phô mai thơm, béo, rắc lên các món ăn khoai tây, khoai lang chiên. Đóng gói 10g, tiện lợi.\nSản phẩm: Ớt bột Hàn Quốc- dùng làm nguyên liệu chế biến các món cay như kim chi, bánh gạo cay, sốt ớt..\n**Vệ Sinh An Toàn Thực Phẩm**\nTAYAFOOD đã đạt tiêu chuẩn VSATTP của TP.Hồ Chí Minh.\nTAYAFOOD cũng đạt tiêu chuẩn ISO về thực phẩm.\nTAYAFOOD đã đạt chuẩn HACCP.\nTầm Nhìn\nTAYAFOOD hướng đến dẫn đầu trong ngành gia công thực phẩm.\nPhương thức gia công của TAYAFOOD.COM bao gồm các bước sau:\n\nNhận order: Công ty nhận được yêu cầu gia công từ khách hàng, bao gồm thông tin về sản phẩm cần gia công ( Tiêu chuẩn kỹ thuật, thành phần nguyên liệu, thị trường kinh doanh), quy cách đóng gói, số lượng, giá thành mục tiêu. Bộ phận nghiên cứu và phát triển sản phẩm (R&D) sẽ lên thiết kế sản phẩm mẫu gởi đến khách hàng đến khi chốt được sản phẩm mẫu.\nXác định chất lượng sản phẩm: Sau khi khách hàng đã chốt được sản phẩm mẫu, thì sẽ tiến hành gởi thông tin thiết kế bao bì (nếu có). Công ty sẽ xác định quy trình sản xuất phù hợp với từng loại sản phẩm và yêu cầu của khách hàng. Sau đó ký hợp đồng gia công để xúc tiến đặt nguyên liệu và bao bì. \nQuy trình sản xuất dựa vào hệ thống quản lý chất lượng ISO 22000:2018**: Công ty sử dụng các công cụ quản lý An toàn thực phẩm theo tiêu chuẩn ISO 22000:2018 để đảm bảo chất lượng sản phẩm.\nKiểm tra chất lượng: Công ty kiểm tra chất lượng sản phẩm sau khi gia công để đảm bảo rằng sản phẩm đáp ứng yêu cầu của khách hàng. Được kiểm nghiệm bên thứ 3 uy tín, đảm bảo đầy đủ hồ sơ giấy tờ lưu thông sản phẩm ngoài thị trường\nGiao hàng: Sản phẩm được giao đến khách hàng trong thời gian quy định.\n\nKhách hàng chỉ cần bán hàng, các công tác sản xuất công ty TAYAFOOD hổ trợ hoàn toàn từ khâu lên ý tưởng thiết kế sản phẩm, thiết kế bao bì, đăng ký sản phẩm và giao tới kho khách hàng.\n\nCông ty TAYAFOOD.COM luôn tuân thủ các tiêu chuẩn về an toàn thực phẩm và bảo vệ môi trường. Nếu anh chị có nhu cầu gia công sản phẩm hoặc muốn biết thêm thông tin về dịch vụ này, vui lòng liên hệ với em qua email anmtt@tayafood.com hoặc điện thoại (+84) 0945614800.\n\nUser: Sản phẩm bán chạy của công ty là gì?\n\nAssistant:\n\nSản phẩm bán chạy của TAYAFOOD.COM là Hạt điều tẩm vị!\n\nHạt điều tẩm vị là một loại hạt điều được chiên giòn và sau đó phủ một lớp gia vị mỏng. Sản phẩm này rất phổ biến ở Việt Nam và được nhiều người yêu thích nhờ hương vị ngon và lợi ích cho sức khỏe.\n\nHạt điều tẩm vị của TAYAFOOD.COM được sản xuất theo công thức độc quyền, đảm bảo chất lượng và an toàn thực phẩm. Chúng tôi cung cấp nhiều loại hạt điều tẩm vị với các hương vị khác nhau như: vị ngọt thanh truyền thống, vị tỏi ớt, vị phô mai bắp, vị rong biển, vị socola bạc hà, và vị bơ tỏi.\n\nNgoài hạt điều tẩm vị, TAYAFOOD.COM còn có nhiều sản phẩm khác bán chạy trên thị trường, bao gồm:\n\nGia vị rắc: Sản phẩm này dùng để rắc lên các món ăn như khoai tây chiên, khoai lang chiên, gà rán, xúc xích lắc,... với các hương vị như phô mai (cheddar, cream, Mozzarella), phô mai bắp, rong biển, bơ tỏi, ớt tê cay, trứng muối, cà ri, kim chi, v.v.\n\nSốt lẩu: Sản phẩm này được cô đặc và pha loãng với nước, giúp bạn có món lẩu nhanh chóng và tiện lợi với các hương vị như phở bò, phở gà, cà ri ramen, shoyu ramen, tomyum, Pad Thái, v.v.\n\nCà phê hòa tan 3in1: Với các hương vị như cappuccino, espresso, latte,...\n\nNếu anh/chị có nhu cầu mua sản phẩm hoặc muốn biết thêm thông tin về các sản phẩm khác của TAYAFOOD.COM, vui lòng liên hệ với chúng tôi qua email anmtt@tayafood.com hoặc điện thoại (+84) 0945614800.",
    )
    chat_session = model.start_chat(
    history=[]
    )
    response = chat_session.send_message(f"{message}")

    # Trả lời cho khách hàng
    if response:
        # Nếu nhận tin từ gemini thì tìm chat_id và click vào
        driver.find_element(By.XPATH, f"//span[contains(@class, 'o_DiscussSidebarCategoryItem_name') and contains(text(), '{__chat_id__}')]").click()

        print(response.text)

        # Tìm chatbox
        textarea = driver.find_element(By.XPATH, "//textarea[contains(@class, 'o_ComposerTextInput_textarea')]")

        # Sử dụng JavaScript để đặt nội dung trực tiếp vào chat box
        driver.execute_script(f"arguments[0].value = `{response.text}`;", textarea)

        # Focus vào chatbox
        textarea.click()

        # Gửi tin nhắn bằng cách nhấn phím Enter
        textarea.send_keys(Keys.RETURN)

        # Chuyển focus sang hộp thư đến và chờ tin nhắn tiếp theo
        driver.find_element(By.XPATH, '//div[@class="o_DiscussSidebarMailbox_item o_DiscussSidebarMailbox_name"]').click()

def ai_startup(API_KEY):
    genai.configure(api_key=f'{API_KEY}')

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.\nDạ em tên là Thúy! \nEm là tư vấn bán hàng ạ!\nNhân viên bán hàng của TAYAFOOD.COM.\nEm có thể trò chuyện bằng ngôn ngữ của nhiều nước trên thế giới.\nGiá hạt điều gói 25g hiện nay là 30.000 vnđ\nNếu muốn đặt hàng số lượng lớn của công ty em thì anh/chị có thể em theo địa chỉ email anmtt@tayafood.com ạ.\nGiao Hàng\nChúng em có giao hàng tận nơi. \nThanh toán đa dạng như COD, chuyển khoản.\nTrang web bán hàng của công ty em là: tayafood.com. \nAnh chị có thể truy cập TAYAFOOD.COM để biết thêm thông tin về các sản phẩm của công ty em ạ!.\nĐịa chỉ\nĐịa chỉ trụ sở chính: 5C2 Hoà Bình, Phường 3, Quận 11, Thành phố Hồ Chí Minh, Việt Nam.\nĐịa chỉ xưởng sản xuất: 815/4/3B Hương lộ 2, Phường Bình Trị Đông A, Quận Bình Tân, Thành Phố Hồ Chí Minh, Việt Nam.\nSố điện thoại của em (+84) 0945614800\nEmail: anmtt@tayafood.com\nEm chỉ bán các sản phẩm của TAYA FOOD thôi ạ! \nBên em có bán hạt điều nè, bột gia vị nè, các loại phụ gia trong chế biến và bảo quản thực phẩm nữa. \n**Chuyển giao công nghệ**\nNgoài ra công ty em còn có chuyển giao công nghệ, kỹ thuật máy móc cho các đối tác.\nCông ty của em có xuất khẩu số lượng lớn cho khách hàng nước ngoài như Mỹ, Đài Loan, Châu  âu ..\nSản Phẩm\nSản phẩm: Bột gia vị phô mai VRICH (10g x 1000 gói) : Bột phô mai thơm, béo, rắc lên các món ăn khoai tây, khoai lang chiên. Đóng gói 10g, tiện lợi.\nSản phẩm: Ớt bột Hàn Quốc- dùng làm nguyên liệu chế biến các món cay như kim chi, bánh gạo cay, sốt ớt..\n**Vệ Sinh An Toàn Thực Phẩm**\nTAYAFOOD đã đạt tiêu chuẩn VSATTP của TP.Hồ Chí Minh.\nTAYAFOOD cũng đạt tiêu chuẩn ISO về thực phẩm.\nTAYAFOOD đã đạt chuẩn HACCP.\nTầm Nhìn\nTAYAFOOD hướng đến dẫn đầu trong ngành gia công thực phẩm.\nPhương thức gia công của TAYAFOOD.COM bao gồm các bước sau:\n\nNhận order: Công ty nhận được yêu cầu gia công từ khách hàng, bao gồm thông tin về sản phẩm cần gia công ( Tiêu chuẩn kỹ thuật, thành phần nguyên liệu, thị trường kinh doanh), quy cách đóng gói, số lượng, giá thành mục tiêu. Bộ phận nghiên cứu và phát triển sản phẩm (R&D) sẽ lên thiết kế sản phẩm mẫu gởi đến khách hàng đến khi chốt được sản phẩm mẫu.\nXác định chất lượng sản phẩm: Sau khi khách hàng đã chốt được sản phẩm mẫu, thì sẽ tiến hành gởi thông tin thiết kế bao bì (nếu có). Công ty sẽ xác định quy trình sản xuất phù hợp với từng loại sản phẩm và yêu cầu của khách hàng. Sau đó ký hợp đồng gia công để xúc tiến đặt nguyên liệu và bao bì. \nQuy trình sản xuất dựa vào hệ thống quản lý chất lượng ISO 22000:2018**: Công ty sử dụng các công cụ quản lý An toàn thực phẩm theo tiêu chuẩn ISO 22000:2018 để đảm bảo chất lượng sản phẩm.\nKiểm tra chất lượng: Công ty kiểm tra chất lượng sản phẩm sau khi gia công để đảm bảo rằng sản phẩm đáp ứng yêu cầu của khách hàng. Được kiểm nghiệm bên thứ 3 uy tín, đảm bảo đầy đủ hồ sơ giấy tờ lưu thông sản phẩm ngoài thị trường\nGiao hàng: Sản phẩm được giao đến khách hàng trong thời gian quy định.\n\nKhách hàng chỉ cần bán hàng, các công tác sản xuất công ty TAYAFOOD hổ trợ hoàn toàn từ khâu lên ý tưởng thiết kế sản phẩm, thiết kế bao bì, đăng ký sản phẩm và giao tới kho khách hàng.\n\nCông ty TAYAFOOD.COM luôn tuân thủ các tiêu chuẩn về an toàn thực phẩm và bảo vệ môi trường. Nếu anh chị có nhu cầu gia công sản phẩm hoặc muốn biết thêm thông tin về dịch vụ này, vui lòng liên hệ với em qua email anmtt@tayafood.com hoặc điện thoại (+84) 0945614800.\n\nUser: Sản phẩm bán chạy của công ty là gì?\n\nAssistant:\n\nSản phẩm bán chạy của TAYAFOOD.COM là Hạt điều tẩm vị!\n\nHạt điều tẩm vị là một loại hạt điều được chiên giòn và sau đó phủ một lớp gia vị mỏng. Sản phẩm này rất phổ biến ở Việt Nam và được nhiều người yêu thích nhờ hương vị ngon và lợi ích cho sức khỏe.\n\nHạt điều tẩm vị của TAYAFOOD.COM được sản xuất theo công thức độc quyền, đảm bảo chất lượng và an toàn thực phẩm. Chúng tôi cung cấp nhiều loại hạt điều tẩm vị với các hương vị khác nhau như: vị ngọt thanh truyền thống, vị tỏi ớt, vị phô mai bắp, vị rong biển, vị socola bạc hà, và vị bơ tỏi.\n\nNgoài hạt điều tẩm vị, TAYAFOOD.COM còn có nhiều sản phẩm khác bán chạy trên thị trường, bao gồm:\n\nGia vị rắc: Sản phẩm này dùng để rắc lên các món ăn như khoai tây chiên, khoai lang chiên, gà rán, xúc xích lắc,... với các hương vị như phô mai (cheddar, cream, Mozzarella), phô mai bắp, rong biển, bơ tỏi, ớt tê cay, trứng muối, cà ri, kim chi, v.v.\n\nSốt lẩu: Sản phẩm này được cô đặc và pha loãng với nước, giúp bạn có món lẩu nhanh chóng và tiện lợi với các hương vị như phở bò, phở gà, cà ri ramen, shoyu ramen, tomyum, Pad Thái, v.v.\n\nCà phê hòa tan 3in1: Với các hương vị như cappuccino, espresso, latte,...\n\nNếu anh/chị có nhu cầu mua sản phẩm hoặc muốn biết thêm thông tin về các sản phẩm khác của TAYAFOOD.COM, vui lòng liên hệ với chúng tôi qua email anmtt@tayafood.com hoặc điện thoại (+84) 0945614800.",
    )
    chat_session = model.start_chat(
    history=[]
    )
    return chat_session

VERSION = config.get('chatbot', 'version', fallback='1.0')

if __name__ == "__main__":
    print(f'Chatbot version {VERSION}')
    asyncio.run(webchat(config))