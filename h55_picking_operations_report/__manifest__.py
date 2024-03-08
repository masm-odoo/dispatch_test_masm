{
    'name': 'Stock - Report Updated',
    'depends': ['stock_picking_batch'],
    'data': [
        'report/stock_picking_views.xml',
    ],
    "auto_install": True,
    'installable': True,
}

#./odoo-bin --addons-path=addons,../enterprise,../Github/odoo-training-2024 -d masm-db --db-filter=masm-db -i base