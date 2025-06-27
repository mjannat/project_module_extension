{
    'name': 'Project Task Dashboard',
    'version': '16.0.1.0.0',
    'summary': 'Dashboard for total project tasks with time filters',
    'description': 'Adds a dashboard to show the total number of project tasks with filters for this week, this month, previous week, and previous month.',
    'category': 'Project/',
    'author': 'Your Company',
    'website': 'https://yourcompany.com',
    'license': 'AGPL-3',
    'depends': ['project'],
    'data': [
        'views/project_task_dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_task_dashboard/static/src/js/task_dashboard.js',
            'project_task_dashboard/static/src/xml/task_dashboard.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
} 