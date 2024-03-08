from odoo import api,fields, models

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    fleet_id = fields.Many2one('fleet.vehicle', string='Fleet')
    category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    stock_dock_id = fields.Many2one('stock.dock')
    
    weight_value = fields.Float(string='Weight (kg)', compute="_compute_weight_volume")
    volume_value = fields.Float(string='Volume (m^3)', compute="_compute_weight_volume")
    weight = fields.Float(string='Weight(%)', compute="_compute_weight_volume", store=True)
    volume = fields.Float(string='Volume(%)', compute="_compute_weight_volume", store=True)
    transfers = fields.Integer(string='Transfers', compute="_compute_transfers", store=True)
    lines = fields.Integer(string='Lines', compute="_compute_transfers", store=True)

    # ------------------------------ Methods ------------------------------

    @api.depends('picking_ids', 'category_id')
    def _compute_weight_volume(self):
        for record in self:
            local_w = sum((line.weight_wh) for line in record.picking_ids)
            local_v = sum((line.volume_wh) for line in record.picking_ids)

            record.weight_value = local_w
            record.volume_value = local_v
            record.weight = (local_w/record.category_id.max_weight) * 100 if record.category_id.max_weight > 0 else 0 
            record.volume = (local_v/record.category_id.max_volume) * 100 if record.category_id.max_volume > 0 else 0

    @api.depends('picking_ids', 'move_line_ids')
    def _compute_transfers(self):
        for record in self:
            record.transfers = len(record.picking_ids)
            record.lines = len(record.move_line_ids)
            # record.lines = len(record.picking_type_idmove_ids_without_package)

    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + " (" + str(format(record.weight,".2f")) + "kg, " + str(format(record.volume,".2f")) + "m3)"