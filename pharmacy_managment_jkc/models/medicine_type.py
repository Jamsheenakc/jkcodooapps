# custom_medicine_type/models/medicine_type.py

from odoo import models, fields

class MedicineType(models.Model):
    _name = 'medicine.type'
    _description = 'Medicine Type'

    name = fields.Char(string='Name', required=True)
