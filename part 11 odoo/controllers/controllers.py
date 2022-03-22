# -*- coding: utf-8 -*-
# from odoo import http


# class Weddingorganizzer(http.Controller):
#     @http.route('/weddingorganizzer/weddingorganizzer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weddingorganizzer/weddingorganizzer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weddingorganizzer.listing', {
#             'root': '/weddingorganizzer/weddingorganizzer',
#             'objects': http.request.env['weddingorganizzer.weddingorganizzer'].search([]),
#         })

#     @http.route('/weddingorganizzer/weddingorganizzer/objects/<model("weddingorganizzer.weddingorganizzer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weddingorganizzer.object', {
#             'object': obj
#         })
