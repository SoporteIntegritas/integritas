# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class mx_integritas_proyectos(models.Model):
#     _name = 'mx_integritas_proyectos.mx_integritas_proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100