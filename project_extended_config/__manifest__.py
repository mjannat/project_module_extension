# -*- coding: utf-8 -*-
{
    'name': "project_extended_config",

    'summary': """
       This module is use for all kind of configuration for team wise project management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mim Jannat",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom/',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/team_config_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
