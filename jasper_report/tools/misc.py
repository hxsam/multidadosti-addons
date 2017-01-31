# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import os

from odoo.tools import config
from odoo.tools.translate import _
from odoo.exceptions import RedirectWarning


def mount_path_jasper(db_name, report_name, report_id):
    # Make a directory name of report files unique
    dir_name = report_name + '_' + str(report_id)

    file_store = config.filestore(db_name)
    report_path = '/'.join([file_store, 'jasper_report', dir_name])

    if not os.path.exists(report_path):
        try:
            os.makedirs(report_path)
        except OSError:
            raise RedirectWarning(
                _('Error!'),
                _('Please, see the write permission and the directory path!'))
    return report_path
