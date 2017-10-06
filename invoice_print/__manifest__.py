# -*- coding: utf-8 -*-
{
    'name': "invoice prints",

    'description': """
        Print Invoice With Gst
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','product','sale'],

    'data': [
        'views/product_view.xml',
        'views/partner_view.xml',
        'views/order_view.xml',
        'data/invoice_data.xml',
        'report/sale_order_report_view.xml',
    ],
}