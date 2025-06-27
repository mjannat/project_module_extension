# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectExtendedConfig(http.Controller):
#     @http.route('/project_extended_config/project_extended_config', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_extended_config/project_extended_config/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_extended_config.listing', {
#             'root': '/project_extended_config/project_extended_config',
#             'objects': http.request.env['project_extended_config.project_extended_config'].search([]),
#         })

#     @http.route('/project_extended_config/project_extended_config/objects/<model("project_extended_config.project_extended_config"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_extended_config.object', {
#             'object': obj
#         })
