from odoo import api, fields, models, _

class AccountInvoice(models.Model):        
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    def _days_due(self):
        for invoice in self:
            if invoice.date_due:
                days_due = fields.Date.from_string(fields.Date.today()) - fields.Date.from_string(invoice.date_due) 
                invoice.days_due = days_due.days
            else:
                invoice.days_due = False
    
    days_due=fields.Integer(compute=_days_due)

class AccountTc(models.Model):        
    _name = 'account.tc'
    _inherit = 'account.tc'

rate=fields.float('res.currency', string='TC')


