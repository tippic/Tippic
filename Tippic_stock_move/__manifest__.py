# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Tippic stock move line',
    'version': '11.0',
    'author': 'Productos Tippic',
    'category': 'stock',
    'license': 'LGPL-3',
    'support': 'productostippic.com',
    'website': 'https://www.productostippic.com',
    'summary': 'Tippic stock move line',
    'description': """ tippic stock move line
When user need to print the excel report in purchase order select the purchase order list and
user need to click the "Purchase order Excel Report" button and message will appear.select the "Print Excel report"button
for generating the purchase order excel file""",
    'depends': [
        'stock','base',
    ],
    'data': [
        'wizard/stock_xls_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}