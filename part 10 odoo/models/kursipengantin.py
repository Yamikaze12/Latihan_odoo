from odoo import api, fields, models


class KursiPengantin(models.Model):
    _name = 'weddingorg.kursipengantin'
    _description = 'Daftar Kursi Pengantin Pelaminan'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Kursi Pengantin')
    harga = fields.Integer(string='Harga Sewa')
    
    
