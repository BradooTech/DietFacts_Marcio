# -*- coding: utf-8 -*-
{
    'name': "dietfacts",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Products Diet Facts
    """,

    'author': "BradooTech",
    'website': "http://www.bradootech.com",
    'installable': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	'views/dietfacts_view.xml',
    'views/assets.xml',
    'security/ir.model.access.csv',
    'reports/dietfacts_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
