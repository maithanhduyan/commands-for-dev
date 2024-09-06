{
    'name': 'Tracking Station Module',
    'version': '1.0',
    'category': 'Tracking',
    'summary': 'Module for tracking stations via tracking code',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/tracking_record_views.xml',
        'views/tracking_station_views.xml',
        'views/tracking_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'pacel_tracking/static/src/css/style.css',
            'pacel_tracking/static/src/js/script.js',
        ],
    },
    'installable': True,
    'application': True,
    'demo': [
        'data/demo_data.xml',
    ],
}
