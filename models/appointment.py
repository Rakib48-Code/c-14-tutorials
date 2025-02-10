from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment Record'

    patient_id = fields.Many2one('hospital.patient',string="Patient")
    appointment_date = fields.Date(string='Appointment Date')
    booking_date = fields.Datetime(string='Booking Date')