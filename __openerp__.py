
{
    'name': 'Key Performance Indicator - KPI',
    'version': '1.0',
    'category': 'Management System',
    'summary': 'Smart ISO',
    'author': 'Muhammad Syarif',
    'email': 'muhammad.syarif@proxsisgroup.com',
    'website': 'http://www.proxsisgroup.com',
    'maintainer': 'BizTech Proxsis IT',
    'license': 'AGPL-3',
    'depends': ['mail','base'],
    'data': [
        'views/menu.xml',
        'views/kpi_target.xml',
        'views/kpi_action.xml',
        'views/kpi_activity.xml',
        'views/kpi_achievement.xml',
		'security/kpi.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/smartiso.png'],
    'installable': True,
    'auto_install': False
}