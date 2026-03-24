# -*- coding: utf-8 -*-

{
    "name": "Ignite Backend Theme V17",
    "description": """Ignite Backend Theme V17""",
    "summary": "Ignite Backend Theme V17",
    "category": "Themes/Backend",
    "version": "17.0",
    'author': 'Appness Technology',
    'company': 'Appness Technology',
    'maintainer': 'Appness Technology',
    'website': "https://www.appness.ai",
    "depends": ['base', 'web', 'mail', 'ignite_dashboard'],
    "data": [
        'views/menu_icons_common.xml',
        'views/login.xml',
        # 'data/ir_cron_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ignite_backend_theme/static/src/css/output.css',
            'ignite_backend_theme/static/src/css/fonts.css',
            'ignite_backend_theme/static/src/css/custom.css',
            'ignite_backend_theme/static/src/css/theme_accent.scss',
            'ignite_backend_theme/static/src/css/sidebar.scss',
            'ignite_backend_theme/static/src/js/chrome/sidebar_menu.js',
            'ignite_backend_theme/static/src/xml/top_bar_templates.xml',
            'ignite_backend_theme/static/src/css/phosphor-bold-icons.css',
            'ignite_backend_theme/static/src/css/replace_fa.css',
            'ignite_backend_theme/static/src/css/animate.min.css',
        ],
        'web.assets_frontend': [
            'ignite_backend_theme/static/src/css/output.css',
            'ignite_backend_theme/static/src/css/website.css',
        ],
    },
    'license': 'LGPL-3',
    # 'pre_init_hook': 'test_pre_init_hook',
    'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'auto_install': False,
    'application': False
}
