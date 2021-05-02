# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    id_number = fields.Integer('ID Number')
    id_date = fields.Date('ID Date')
    barber_name=fields.Char("Name of barber")
    license_number=fields.Integer("License number")
    cr_number=fields.Integer("CR number")
    # vat_number=fields.Integer("VAT number")
    expiry_date=fields.Date("Date Of expiry")