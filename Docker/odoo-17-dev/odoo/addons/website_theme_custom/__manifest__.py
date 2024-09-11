{
    'name': 'Website Theme Custom',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom theme for Odoo Website',
    'description': 'This module customizes the Odoo website theme.',
    'author': 'Mai Thành Duy An',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_theme_custom/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': False,
}
