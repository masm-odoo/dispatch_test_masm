{
    'name': 'Stock - Report Updated',
    'depends': ['stock'],
    'data': [
        'report/report_stockpicking_operations.xml',
    ],
    "auto_install": True,
    'installable': True,
}

#./odoo-bin --addons-path=addons,../enterprise,../Github/odoo-training-2024 -d masm-db --db-filter=masm-db -i base