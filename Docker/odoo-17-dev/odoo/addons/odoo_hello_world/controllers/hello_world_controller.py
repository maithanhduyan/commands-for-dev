from odoo import http
from odoo.http import request, Response

class HelloWorldController(http.Controller):
    @http.route('/api/hello', auth='public', methods=['GET'], csrf=False, type='http')
    def hello_world(self):
        return "Helloworld"
