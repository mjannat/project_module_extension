# -*- coding: utf-8 -*-
{
    'name': 'Project Extended Configuration',
    'version': '16.0.1.0.0',
    'summary': 'Extended project configuration with team management',
    'description': 'Adds team-based project management with access control and extended configuration options.',
    'category': 'Project/',
    'author': 'Your Company',
    'website': 'https://yourcompany.com',
    'license': 'AGPL-3',
    'depends': ['project', 'hr'],
    'data': [
        'data/sequence.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        # 'security/project_team_security.xml',
        'views/team_config_view.xml',
        'views/inherit_project_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
