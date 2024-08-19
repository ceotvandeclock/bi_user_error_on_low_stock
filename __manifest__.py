# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    "name": "User Error on Low Stock Odoo App",
    "version": "16.0.0.3",
    "category": "Warehouse",
    "summary": "user low stock error low product stock information low stock product error low stock on hand quantity error message low sale product stock low stock information low stock product on hand quantity product low stock message inventory low stock error",
    "description": """

       Product Low Stock Odoo App helps users to get an idea about low stock information. When the on hand qty is less then ordered qty then error message will be popup with detail of product on hand quantity.

	""",
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.com',
    "depends": ["base",
                "crm",
                "sale",
                "account",
                "purchase",
                "sale_management",
                "stock",

                ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/user_error_wizard_view.xml",

        ],
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/DpN31pygS84',
    "images":['static/description/User-Error-on-Low-Stock-Odoo-App-Banner.gif'],
}

