from email.policy import default
from odoo import api, fields, models


class Order(models.Model):
    _name = 'weddingorg.order'
    _description = 'New Description'

    orderpanggungdetail_ids = fields.One2many(comodel_name='weddingorg.orderpanggungdetail', 
                                            inverse_name='order_id', 
                                            string='Order Panggung Deskripsi')
    orderkursidetail_ids = fields.One2many(comodel_name='weddingorg.orderkursidetail', 
                                            inverse_name='orderk_id', 
                                            string='Order Kursi Deskripsi')

    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan', default = fields.Datetime.now())
    tanggal_kirim = fields.Date(string='Tanggal Pengiriman', default = fields.Date.today())
    
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('orderpanggungdetail_ids', 'orderkursidetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['weddingorg.orderpanggungdetail'].search([('order_id','=',record.id)]).mapped('harga'))
            b = sum(self.env['weddingorg.orderkursidetail'].search([('orderk_id','=',record.id)]).mapped('harga'))
            record.total = a + b



class OrderPanggungDetail(models.Model):
    _name = 'weddingorg.orderpanggungdetail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='weddingorg.order', string='Order Panggung')
    panggung_id = fields.Many2one(comodel_name='weddingorg.panggung', string='Panggung')
    
    name = fields.Selection(string='Name', selection=[('panggung', 'Panggung'), ('kursi tamu', 'Kursi Order'),])
    harga = fields.Integer(compute='_compute_harga', string='Harga Sewa')
    qty = fields.Integer(string='Quantity')
    
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga_Satuan')
    
    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan =  record.panggung_id.harga
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, vals):
        record = super(OrderPanggungDetail, self).create(vals)
        if record.qty:
            self.env['weddingorg.panggung'].search([('id','=',record.panggung_id.id)]).write({'stok':record.panggung_id.stok-record.qty})
        return record

class OrderKursiDetail(models.Model):
    _name = 'weddingorg.orderkursidetail'
    _description = 'New Description'

    orderk_id = fields.Many2one(comodel_name='weddingorg.order', string='Order Kursi')
    kursitamu_id = fields.Many2one(comodel_name='weddingorg.kursitamu', string='Kursi')
    
    name = fields.Selection(string='Name', selection=[('panggung', 'Panggung'), ('kursi tamu', 'Kursi Order'),])
    harga = fields.Integer(compute='_compute_harga', string='Harga Sewa')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga_Satuan')
    
    @api.depends('kursitamu_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan =  record.kursitamu_id.harga
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, vals):
        record = super(OrderKursiDetail, self).create(vals)
        if record.qty:
            self.env['weddingorg.kursitamu'].search([('id','=',record.kursitamu_id.id)]).write({'stok':record.kursitamu_id.stok-record.qty})
        return record