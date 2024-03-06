from odoo import api,fields, models

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    fleet_id = fields.Many2one('fleet.vehicle', string='Fleet')
    category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    stock_dock_id = fields.Many2one('stock.dock')
    
    weight = fields.Float(string='Weight (kg)', compute="_compute_weight_volume", store=True)
    volume = fields.Float(string='Volume (m^3)', compute="_compute_weight_volume", store=True)
    transfers = fields.Integer(string='Transfers', compute="_compute_transfers", store=True)
    lines = fields.Integer(string='Lines', compute="_compute_transfers", store=True)
    date = fields.Date(string="Date")

    # ------------------------------ Methods ------------------------------

    @api.depends('picking_ids', 'category_id')
    def _compute_weight_volume(self):
        self.weight = 0
        self.volume = 0

        for record in self:
            local_w = sum((line.weight_wh) for line in record.picking_ids)
            local_v = sum((line.volume_wh) for line in record.picking_ids)

            if self.category_id.max_weight > 0: self.weight = (local_w/self.category_id.max_weight) * 100
            if self.category_id.max_volume > 0: self.volume = (local_v/self.category_id.max_volume) * 100

    @api.depends('picking_ids', 'move_line_ids')
    def _compute_transfers(self):
        for record in self:
            record.transfers = len(record.picking_ids)
            record. lines = len(record.move_line_ids)