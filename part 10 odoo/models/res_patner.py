from email.policy import default
from odoo import _, api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_pegawainya = fields.Boolean(string='Pegawai', default=False)
    is_costumernya = fields.Boolean(string='Costumer', default=False)
    
