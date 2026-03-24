# -*- coding: utf-8 -*-
{
    'name': "Ignite Dashboard",

    'summary': """Ignite Dashboard
        """,

    'description': """
        Ignite Dashboard
    """,

    'author': "Appness",
    'website': "https://www.appness.ai/",
    'category': 'Productivity',
    'version': '0.1',
    'application': True,
    'installable': True,

    'depends': ['base', 'web', 'mail', 'ks_dashboard_ninja', 'web_editor',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # 'assets': {
        # 'web_editor.assets_wysiwyg': [
        #     'ignite_dashboard/static/src/xml/web_editor.xml',
        #     'ignite_dashboard/static/src/scss/wysiwyg.scss',
        #     'ignite_dashboard/static/src/js/wysiwyg.js',
        #     'ignite_dashboard/static/src/xml/wysiwyg.xml',
        # ],
        # 'web.assets_backend': [
        #     'ignite_dashboard/static/src/**/*',
        # ],
    # }
}