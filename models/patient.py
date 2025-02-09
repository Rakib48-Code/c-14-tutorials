from odoo import api, models, fields, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ], string='Gender')
    contact = fields.Char(string='Contact')
    note = fields.Text(string='Description')
    registration_date = fields.Date(string='Registration Date')

    # sequence number
    sl_no = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                        index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl_no', _('New')) == _('New'):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res
