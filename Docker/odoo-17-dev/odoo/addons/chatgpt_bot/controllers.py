# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class ChatGPTBotController(http.Controller):
    @http.route('/chatgpt_bot', methods=['GET'], csrf=False, type='http', auth='public')
    def index(self, **kwargs):
        message = request.params.get('message')
        answer = request.env['chatgpt.bot'].get_answer(message)
        if answer:
            return answer
        return 'Không tìm thấy câu trả lời'