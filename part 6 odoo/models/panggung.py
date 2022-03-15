from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Jenis Panggung'

    name = fields.Char(string='Name',required=True)
    pelaminan_id = fields.Many2one(comodel_name='wedding.pelaminan', 
                                string='Type Pelaminan',
                                required=True
                                )
    kursipengantin_id = fields.Many2one(comodel_name='wedding.kursipengantin', 
                                string='Type kursi Pengantin',
                                required=True
                                )
    bunga = fields.Selection(string='Jenis Bunga', selection=[('bunga hidup', 'Bunga Hidup'), ('bunga mati', 'Bunga Mati'),])
    Aksesoris = fields.Char(string='Aksesories')
    harga = fields.Integer(compute='_compute_harga', string='Harga Sewa')
    
    @api.depends('pelaminan_id','kursipengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursipengantin_id.harga
    
    stok = fields.Integer(string='Stok paket panggung')
    
    des_pelaminan = fields.Char(compute='_compute_des_pelaminan', string='Deskripsi pelaminan')
    
    @api.depends('pelaminan_id')
    def _compute_des_pelaminan(self):
        for record in self:
            record.des_pelaminan = record.pelaminan_id.deskripsi

    des_kursipengantin = fields.Char(compute='_compute_des_kursipengantin', string='Deskripsi Kursi Pengantin')
    
    @api.depends('kursipengantin_id')
    def _compute_des_kursipengantin(self):
        for record in self:
            record.des_kursipengantin = record.kursipengantin_id.deskripsi
