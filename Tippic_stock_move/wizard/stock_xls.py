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


class StockReportOut(models.Model):        
    _name = 'stock.report.out'
    _description = 'Stock order report'
    
    stock_work = fields.Char('Name', size=256)
    file_names = fields.Binary('Reporte CSV', readonly=True)
    
   
class StockWizards(models.Model):        
    _name = 'stock.reports'
    _description = 'stock wizard'
    
#purchase order excel report button actions               
    @api.multi
    def action_stock_report(self):

# XLS report
        custom_value = {}
        label_lists = ['FECHA', 'CLIENTE', 'PROVEEDOR', 'MOVIMIENTO', 'PRODUCTO','LOTE', 'CANTIDAD', 'UNIDAD']
        order = self.env['stock.move.line'].browse(self._context.get('active_ids', list()))

        datas = []
        for values in order:
            item = [
                    str(values.date or ''),
                    str(values.move_id.partner_id.name or values.move_id.picking_id.partner_id.name or ''),
                    str(values.move_id.partner_id.name or values.move_id.picking_id.partner_id.name or ''),
                    str(values.reference or ''),
                    str(values.product_id.name or ''),
                    str(values.lot_id.name or ''),
                    str(values.qty_done or ''),
                    str(values.product_uom_id.name or ''),
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
                'stock_work':'Stock move'+ '.csv',
                'file_names':data,
            } 
            
        act_id = self.env['stock.report.out'].create(attach_vals)
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'stock.report.out',
        'res_id': act_id.id,
        'view_type': 'form',
        'view_mode': 'form',
        'context': self.env.context,
        'target': 'new',
        }
                          
        

 




















