import configparser
import asyncio
from odoo.odoo_v15 import webchat

# Load cấu hình từ file app.config
config = configparser.ConfigParser()
config.read('app.config')

VERSION = config.get('chatbot', 'version', fallback='1.0')

if __name__ == "__main__":
    print(f'Chatbot version {VERSION}')
    asyncio.run(webchat(config))
