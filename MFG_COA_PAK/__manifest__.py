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
    'author': 'Itech Resources',
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
