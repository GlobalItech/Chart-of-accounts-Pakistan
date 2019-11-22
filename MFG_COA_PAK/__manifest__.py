# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Pakistan Chart of Accounts (Manufacturing)",
    'description': "Pakistan Chart of Accounts",
    'summary': """
        Chart of Accounts to facilitate Financial Reporting as per IFRS and other applicable local standards, having Raw Material, WIP & Finished Goods Accounts for manufacturing concerns.
        """,
    
    'author': 'Itech Resources,Steigend IT Solutions',
    'website': 'http://itechresources.net/',
    'category': 'Accounting &amp; Finance',
    'version': '1.2.1',
    'depends': ['base', 'account'],
    'data': [
        'security/account_parent_security.xml',
        'views/account_view.xml',
        'views/open_chart.xml',
        #'data/account_type_data.xml',
        'data/l10n_pak_chart_data.xml',
        'data/account_chart_template_data.yml',

    ],
    'demo': [
    ],
    'price': 30.00,
    'currency': 'EUR',
}
