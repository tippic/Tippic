from odoo import api, fields, models, _

class AccountInvoice(models.Model):        
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    
    def _days_due(self):
        for invoice in self:
            if invoice.date_due:
                days_due = fields.Date.from_string(invoice.date_due) - fields.Date.today()
                invoice.days_due = days_due.days
            else:
                invoice.days_due = False
    
    days_due=fields.Integer(compute=_days_due)
