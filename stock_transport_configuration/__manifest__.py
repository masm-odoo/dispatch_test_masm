{
    'name': 'Stock Transport',
    'depends': ['stock'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
}

#./odoo-bin --addons-path=addons,../enterprise,../Github/odoo-training-2024 -d masm-db --db-filter=masm-db -i base