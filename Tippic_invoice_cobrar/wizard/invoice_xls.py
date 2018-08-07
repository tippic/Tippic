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


class InvoiceReportOut(models.Model):        
    _name = 'invoice.report.out'
    _description = 'Invoice order report'
    
    invoice_work = fields.Char('Name', size=256)
    file_names = fields.Binary('Reporte CSV', readonly=True)
    
   
class InvoiceWizards(models.Model):        
    _name = 'invoice.reports'
    _description = 'invoice wizard'
    
#purchase order excel report button actions               
    @api.multi
    def action_invoice_report(self):

# XLS report
        custom_value = {}
        label_lists = ['EMPRESA', 'N° FACTURA', 'FECHA EMISION', 'FECHA VTO', 'MONTO TOTAL', 'SALDO', 'ESTADO']
        order = self.env['account.invoice'].browse(self._context.get('active_ids', list()))

        datas = []
        for values in order:
            item = [
                    str(values.partner_id.name or ''),
                    str(values.number or ''),
                    str(values.date_invoice or ''),
                    str(values.date_due or ''),
                    str(values.amount_total_signed or ''),
                    str(values.residual_signed or ''),
                    str(values.state or ''),
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
                'invoice_work':'Invoice move'+ '.csv',
                'file_names':data,
            } 
            
        act_id = self.env['invoice.report.out'].create(attach_vals)
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'invoice.report.out',
        'res_id': act_id.id,
        'view_type': 'form',
        'view_mode': 'form',
        'context': self.env.context,
        'target': 'new',
        }
                          
        

 




















