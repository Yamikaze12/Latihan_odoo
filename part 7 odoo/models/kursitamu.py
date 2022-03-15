from odoo import api, fields, models


class KursiTamu(models.Model):
    _name = 'weddingorg.kursitamu'
    _description = 'Daftar Kursi Tamu'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Kursi Tamu', selection=[('plastik', 'Plastik'), ('stainless', 'Stainless'),])
    stok = fields.Integer(string='stok kursi')
    harga = fields.Integer(string='Harga Sewa perunit')
    
    
