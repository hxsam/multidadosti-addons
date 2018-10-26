{
    'name': "Access Emails",

    'summary': """
        Access To Emails.""",

    'description': """
        This Base module includes access emails.
    """,

    'author': "MultidadosTI",
    'website': "www.multidadosti.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'mail',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'views/access_emails.xml',
    ],
}