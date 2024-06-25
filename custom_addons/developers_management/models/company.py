from odoo import models, fields

class Company(models.Model):
    _name = 'company'
    _description = 'Company'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    developer_ids = fields.One2many('developer', 'company_id', string='Developers')