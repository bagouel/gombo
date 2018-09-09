# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018-2019 (<http://africa-performance.com>).
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
	'name': 'Attendances for Schools',
    'version': '1.2',
    'category': 'Human Resources',
    'description':"""
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Sign in/Sign out) performed by them.
       """,
    'author': 'Armel VANIE',
    'depends': ['base','hr_attendance'],
     'js': [
        'static/src/js/jquery.webcam.js',
        'static/src/js/hr_webcam.js',
    ],
    'css': [
        'static/src/css/hr_webcam.css',
    ],
    'qweb': [
        'static/src/xml/hr_webcam.xml',
    ],
    'data': ['views/menu_view.xml'
             ],
    'installable': True,
    'auto_install': False,

}