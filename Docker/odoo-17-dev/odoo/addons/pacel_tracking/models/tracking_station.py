from odoo import models, fields

class TrackingStation(models.Model):
    _name = 'tracking.station'
    _description = 'Tracking Station'

    name = fields.Char('Station Name', required=True)
    code = fields.Char('Station Code', required=True)
    address = fields.Text('Station Address')
