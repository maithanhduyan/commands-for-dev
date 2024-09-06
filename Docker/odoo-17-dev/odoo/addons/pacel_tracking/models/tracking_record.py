from odoo import models, fields

class TrackingRecord(models.Model):
    _name = 'tracking.record'
    _description = 'Tracking Record'

    code = fields.Char('Tracking Code', required=True)
    station_ids = fields.Many2many('tracking.station', string='Stations')