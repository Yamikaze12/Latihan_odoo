# -*- coding: utf-8 -*-
# from odoo import http


# class Wedding(http.Controller):
#     @http.route('/wedding/wedding/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wedding/wedding/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wedding.listing', {
#             'root': '/wedding/wedding',
#             'objects': http.request.env['wedding.wedding'].search([]),
#         })

#     @http.route('/wedding/wedding/objects/<model("wedding.wedding"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wedding.object', {
#             'object': obj
#         })
