from email.policy import default
from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'weddingorg.pengembalian'
    _description = 'Pengembalian barang'

    name = fields.Char(string='Name')
    order_id = fields.Many2one(comodel_name='weddingorg.order', string='Kode Order')
    nama_penyewa = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.nama_penyewa = self.env['weddingorg.order'].search([('id','=',record.order_id.id)]).mapped('pemesan').name
    
    tgl_pengembalian = fields.Date(string='Tanggal Pengembalian', default = fields.Date.today())
    
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.model
    def create(self, vals):
        record = super(Pengembalian, self).create(vals)
        if record.tgl_pengembalian:
            self.env['weddingorg.order'].search([('id','=',record.order_id.id)]).write({'sudah_kembali':True})
        return record