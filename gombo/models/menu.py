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


import time
from datetime import datetime

from openerp.osv import fields, osv
from openerp import models
from openerp.tools.translate import _





class hr_classroom(osv.osv):
	_name="hr.classroom"
	_res_name='classroom_id'
	_columns={
		'classroom_id':fields.char('Classroom Id'),
        'designation_classroom':fields.char(string="Classroom Name", required=True),
		'classroom_name':fields.one2many('hr.attendance','classroom'),
        'person_number':fields.char(string="Personn Numbers", required=True),
		
	}
	_defaults={
        'active': True,
		'classroom_id':lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'hr.classroom'),
	}
class hr_discipline(osv.osv):
	_name="hr.discipline"
	_res_name='discipline_id'
	_columns={
		'discipline_id':fields.char('Discipline Id'),
        'designation_discipline':fields.char(string="Discipline Name", required=True),
		'discipline_name':fields.one2many('hr.attendance','discipline'),
	}
	_defaults ={
        'active': True,
		'discipline_id':lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'hr.discipline'),
	}



class hr_attendance(osv.osv):
    _name = "hr.attendance"
    _inherit="hr.attendance"
    _description = "Attendance"

    def action_take_picture(self, cr, uid, ids, context=None):

        if context is None:
            context = {}

        res_model, res_id = self.pool.get('ir.model.data').get_object_reference(cr, uid,'hr_webcam','action_take_photo')
        dict_act_window = self.pool.get('ir.actions.client').read(cr, uid, res_id, [])
        if not dict_act_window.get('params', False):
            dict_act_window.update({'params': {}})
        dict_act_window['params'].update(
            {'employee_id': len(ids) and ids[0] or False})
        return dict_act_window


    def _uptime_(self, cr, uid, fieldnames, args, context=None):
           time=datetime.strptime(self.sharp_time,'%Y-%m-%d %H:%M:%S')
           times=datetime.strptime(self.start_time,'%Y-%m-%d %H:%M:%S')
           res=time-times
           resultat=((res.seconds) / 60) / 60.0
           return resultat

    _columns={
    	'classroom':fields.many2one('hr.classroom',string="Classroom"),
        'discipline':fields.many2one('hr.discipline',string="Discipline"),
        'date':fields.date(string="Date", required=True),
        'start_time':fields.datetime(string='Start Time',required=True),
        'sharp_time':fields.datetime(string='Sharp Time',required=True),
        'uptime':fields.float( string='Uptime', store=True),
        'digital_signature':fields.char('Digital Signature'),
        'control_signature':fields.char('Control Signature'),
        'element_id':fields.many2one('hr.employee','summary_elements', 'Order Reference', ondelete='cascade', domain=[('sale_ok', '=', True)], readonly=True),
        'image':fields.binary('Picture', filters='*.png,*.gif'),
        }
    _defaults = {
        'active': True,
		
    }
class hr_employee(osv.osv):
	_name="hr.employee"
	_inherit="hr.employee"
	_description="Employee"
	_columns={
		'teacher':fields.boolean('It is Teacher?', Yes="Yes, it is a Teacher !", No='No, it  is not a Teacher! '),
        'timetable_volume':fields.char('timetable Volume'),
        'summary_elements':fields.one2many('hr.attendance', 'element_id', 'Order Lines'),

	}

class hr_photos(models.Model):
    _inherit = 'hr.attendance'

    def action_take_picture(self, cr, uid, ids, context=None):

        if context is None:
            context = {}

        res_model, res_id = self.pool.get(
            'ir.model.data').get_object_reference(cr, uid,
                                                  'hr_webcam',
                                                  'action_take_photo')
        dict_act_window = self.pool.get(
            'ir.actions.client').read(cr, uid, res_id, [])
        if not dict_act_window.get('params', False):
            dict_act_window.update({'params': {}})
        dict_act_window['params'].update(
            {'employee_id': len(ids) and ids[0] or False})
        return dict_act_window
