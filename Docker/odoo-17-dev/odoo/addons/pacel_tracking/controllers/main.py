from odoo import http
from odoo.http import request

class TrackingController(http.Controller):

    @http.route('/tracking', type='http', auth='public', website=True)
    def tracking_page(self, **kwargs):
        return request.render('pacel_tracking.tracking_page_template', {})

    @http.route('/tracking/search', type='http', auth='public', methods=['POST'], website=True)
    def search_tracking(self, tracking_code, **kwargs):
        tracking_record = request.env['tracking.record'].sudo().search([('code', '=', tracking_code)], limit=1)
        if tracking_record:
            return request.render('pacel_tracking.tracking_results_template', {
                'tracking_record': tracking_record,
            })
        else:
            return request.render('pacel_tracking.tracking_results_template', {
                'error_message': "No stations found for this tracking code.",
            })
