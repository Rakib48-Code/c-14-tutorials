from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Record'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ],string='Gender')
    contact = fields.Char(string='Contact')