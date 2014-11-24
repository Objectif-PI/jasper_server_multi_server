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

{
    'name': 'JasperReport Server Multi Servers',
    'version': '1.3',
    'category': 'Reporting',
    'complexity': "expert",
    'description': """
    Allows to declare severals Jasper servers.
    In 'jasper document' form, choose on which server you want the report to be generated.
    
    V 1.3 changements :
        - fix report result parsing if js-server = 4.5 (SOAP)
        
    V 1.2 changements :
        - can run report directly from a menu which is configured to run a "ir.actions.xml.report" action
        
    V 1.1 changements :
        - Add version selection in server's form.
        - If server's version >= 5.6, then use rest API. Else, use old SOAP API.
        - Now can export odt, xlsx, docx, ... documents and put them as attachments. 
""",
    'author': 'Objectif-PI',
    'website': 'http://www.objectif-pi.com',
    'images': [],
    'depends': [
        'base',
        'jasper_server',
    ],
    'init_xml': [],
    'update_xml': [
        'oojasper.xml',
        'jasper_document_view.xml',
        'report_static_configuration_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
