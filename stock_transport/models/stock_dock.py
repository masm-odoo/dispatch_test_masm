from odoo import api,fields, models

class StockDock(models.Model):
    _name = 'stock.dock'

    name = fields.Char('Dock Name', required=True)