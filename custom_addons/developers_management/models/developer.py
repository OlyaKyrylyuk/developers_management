from odoo import models, fields, api
from lxml import etree

class Developer(models.Model):
    _name = 'developer'
    _description = 'Developer'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name must be unique.')
    ]

    name = fields.Char(string='Name', required=True)
    type = fields.Selection([
        ('front-end', 'Front-End'),
        ('back-end', 'Back-End'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out-Stuff')
    ], string='Type', required=True)
    global_identification = fields.Char(string='Global Identification', compute='global_identification_compute', store=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    birth_date = fields.Date(string='Birth Date')
    company_id = fields.Many2one('company', string='Company')

    @api.depends('name', 'type')
    def global_identification_compute(self):
        for developer in self:
            developer.global_identification = f"{developer.name}-{developer.type}"