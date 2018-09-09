# -*- coding: utf-8 -*-
#from os import path2 as path
from openerp.osv import  osv 
from openerp import models, fields, api, _
from datetime import datetime
from lxml import etree
from cStringIO import StringIO
from openerp.exceptions import except_orm, Warning, RedirectWarning
#import openpyxl, platform, os.path, xlwt, time, calendar, base64, logging, openerp.addons.decimal_precision as dp
#from openpyxl import load_workbook
#from openpyxl import workbook
from openerp.modules.module import *


class hr_employee(osv.osv):
    _name="hr.employee"
    _inherit="hr.employee"


    def employee_report_docx(self, cr, uid, ids, context=None): # fonction report employee

    
        module_path=get_module_path('gombo')+"\\templates\\employee_template.docx"
        socialfund_dec=self.browse(cr, uid, ids)
        fl = StringIO()
        if context is None :
                context={}

                # code insertion  in my module
        
        wbk.save(fl)
        fl.seek(0)
        buf=base64.encodestring(fl.read())
        ctx=dict(context)
        ctx.update({'file':buf})
        if context is None:
            context={}
        data = {}
        res= self.read(cr, uid, ids, [], context=context)
        res=  res and res[0] or {}
        data['form'] = res
        try:
                form_id= self.pool.get('ir.model.data').get_object_reference(cr, uid, 'employee_report_docx','view_employee_form')[1]
        except ValueError:
                form_id=False
        return{
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'employee.report.file',
            'views':[(form_id, 'form')],
            'view_id':form_id,
            'target':'new',
            'context':ctx,
        }
