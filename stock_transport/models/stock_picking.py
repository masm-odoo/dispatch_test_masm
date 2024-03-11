from odoo import api,fields, models

class Picking(models.Model):
    _inherit = 'stock.picking'

    weight_wh = fields.Float(string='Weight (kg)', compute='_compute_weight_volume')
    volume_wh = fields.Float(string='Volume (m^3)', compute='_compute_weight_volume')

    @api.depends('move_ids')
    def _compute_weight_volume(self):
        for record in self:
            record.weight_wh = sum((line.product_id.weight * line.product_uom_qty) for line in record.move_ids)
            record.volume_wh = sum((line.product_id.volume * line.product_uom_qty) for line in record.move_ids)