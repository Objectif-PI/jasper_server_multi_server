# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Objectif-PI (<http://www.objectif-pi.com>).
#       Damien CRIER <damien.crier@objectif-pi.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from osv import osv
from osv import fields
from openerp.tools.translate import _


class report_static_configuration(osv.osv):
    _name = 'report.static.configuration'
    _description = """  """

    _columns = {
        'name': fields.char('Name', size=64, required=True, help="help.report.static.configuration.name"),
        'value': fields.text('Value', translate=True, help="help.report.static.configuration.value"),
    }
