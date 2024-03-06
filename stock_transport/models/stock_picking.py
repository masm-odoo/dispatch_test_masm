from odoo import api,fields, models

class Picking(models.Model):
    _inherit = 'stock.picking'

    product = fields.Many2one('fleet.vehicle', string='Vehicle')
    weight_wh = fields.Float(string='Weight (kg)', compute='_compute_weight_volume')
    volume_wh = fields.Float(string='Volume (m^3)', compute='_compute_weight_volume')

    @api.depends('move_ids')
    def _compute_weight_volume(self):
        for record in self:
            record.weight_wh = sum((record.product_id.weight * record.product_uom_qty) for record in record.move_ids)
            record.volume_wh = sum((record.product_id.volume * record.product_uom_qty) for record in record.move_ids)