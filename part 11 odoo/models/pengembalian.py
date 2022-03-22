from email.policy import default
from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'weddingorg.pengembalian'
    _description = 'Pengembalian barang'

    order_id = fields.Many2one(comodel_name='weddingorg.order', string='Kode Order')
    name = fields.Char(compute='_compute_name', string='Nama Penyewa')
    
    @api.depends('order_id')
    def _compute_name(self):
        for record in self:
            record.name = self.env['weddingorg.order'].search([('id','=',record.order_id.id)]).mapped('pemesan').name
    
    tgl_pengembalian = fields.Date(string='Tanggal Pengembalian', default = fields.Date.today())
    
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
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

    def unlink(self):
        for wed in self:
            self.env['weddingorg.order'].search([('id','=',wed.order_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()
