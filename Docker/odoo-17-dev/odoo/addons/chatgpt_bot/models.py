# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class ChatGPTBot(models.Model):
    _name = 'chatgpt.bot'
    _description = 'ChatGPT Bot'

    name = fields.Char(string='Name', required=True)
    api_key = fields.Char(string='API Key', required=True)
    api_url = fields.Char(string='API URL', required=True, default='https://api.openai.com/v1/chat/completions')

    @api.model
    def get_answer(self, message):
        # Gửi yêu cầu đến API OpenAI ChatGPT
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
           'model': 'gpt-3.5-turbo',
            'prompt': message,
           'max_tokens': 2048,
            'temperature': 0.7
        }
        response = requests.post(self.api_url, headers=headers, json=data)

        # Xử lý kết quả
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text']
        else:
            return 'Lỗi khi gửi yêu cầu đến API'