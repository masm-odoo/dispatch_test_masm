from odoo import api,fields, models

class ConfSetting(models.TransientModel):
   _inherit = "res.config.settings"

   module_stock_transport = fields.Boolean()