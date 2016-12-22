# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Custom Sales Team',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Custom Sales Team',
    'category': 'Sales',
    'description': """
        Custom module for customize sales_team module
        Changes:
            -translate
            -dashboard view
    """,
    'sequence': 99,
    'depends': [
        'sales_team'
    ],
    'qweb': [
        'static/src/xml/sales_team_dashboard.xml',
    ],
    'installable': True,
}
