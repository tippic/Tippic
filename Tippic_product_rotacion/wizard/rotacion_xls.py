# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import xlwt
import datetime
import unicodedata
import base64
import io
from io import StringIO
import csv
# import cStringIO
from datetime import datetime
from odoo import api, fields, models, _


class RotacionReportOut(models.Model):        
    _name = 'rotacion.report.out'
    _description = 'Rotacion order report'
    
    rotacion_work = fields.Char('Name', size=256)
    file_names = fields.Binary('Reporte CSV', readonly=True)
    
   
class RotacionWizards(models.Model):        
    _name = 'rotacion.reports'
    _description = 'rotacion wizard'
    
#purchase order excel report button actions               
    @api.multi
    def action_rotacion_report(self):

# XLS report
        custom_value = {}
        label_lists = ['CODIGO', 'PRODUCTO', 'STOCK REAL', 'UNIDADES']
        order = self.env['product.template'].browse(self._context.get('active_ids', list()))

        datas = []
        for values in order:
            item = [
                    str(values.default_code or ''),
                    str(values.name or ''),
                    str(values.qty_available or ''),
                    str(values.uom_id.name or ''),
                    ]
            datas.append(item)

        
        output = StringIO()        
        label = (';'.join(label_lists))               
        output.write(label)         
        output.write("\n")   
        
        for data in datas:       
            record = ';'.join(data)           
            output.write(record)
            output.write("\n")
        data = base64.b64encode(bytes(output.getvalue(),"utf-8"))
                              

                       
# Files actions         
        attach_vals = {
                'rotacion_work':'Invoice move'+ '.csv',
                'file_names':data,
            } 
            
        act_id = self.env['rotacion.report.out'].create(attach_vals)
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'rotacion.report.out',
        'res_id': act_id.id,
        'view_type': 'form',
        'view_mode': 'form',
        'context': self.env.context,
        'target': 'new',
        }
                          
        

 




















