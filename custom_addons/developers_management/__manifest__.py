{
    'name': 'Developers Management',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Developers management module',
    'depends': ['base'],
    'author': 'Olha',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/developer_views.xml',
        'views/company_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
