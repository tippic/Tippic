# -*- coding: utf-8 -*-
{
    'name': "Filtro de facturas mensuales",

    'summary': """
        Modulo permite agregar filtros avanzados de reportes mensuales""",

    'description': """
        Modulo permite agregar filtros avanzados de reportes mensuales
    """,

    'author': "Luis Palacios",
    'website': "http://www.productostippic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/invoice_search.xml',
    ]
}
