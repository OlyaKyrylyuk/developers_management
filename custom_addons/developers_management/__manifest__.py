{
    'name': 'Developers Management',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Developers management module',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/developer_views.xml',
        'views/company_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
