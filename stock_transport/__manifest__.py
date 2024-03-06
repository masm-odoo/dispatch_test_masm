{
    'name': 'Stock Transport',
    'depends': ['fleet', 'stock_picking_batch'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
        'views/fleet_vehicle_views.xml'
    ],
    "auto_install": True,
    'installable': True,
}

#./odoo-bin --addons-path=addons,../enterprise,../Github/odoo-training-2024 -d masm-db --db-filter=masm-db -i base