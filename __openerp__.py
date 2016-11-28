# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright © 2016 Techspawn Solutions. (<http://techspawn.in>).
#    Copyright (C) 2004-2015 OpenERP S.A. (<http://www.odoo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Order Line Serial Number",

    'summary': """
        Adds Serial Numbers to Order Lines""",

    'description': """
        This Module Adds Serial Numbers to order Lines in Sales orders and in Purchase orders Dynamically After the Products added and Saved.
    """,

    'author': "Techspawn Solutions Pvt. Ltd.",
    'website': "http://www.techspawn.com",

    'category': 'Others',
    'version': '0.1',

    'depends': ['base', 'sale', 'purchase'],
    
    'images': [
        'images/main.jpg',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
}