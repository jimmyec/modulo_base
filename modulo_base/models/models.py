# -*- coding: utf-8 -*-
# Copyright 2020 AndesaSoft

from odoo import api, fields, models, _


# class modulo_base(models.Model):
#     _name = 'modulo_base.modulo_base'
#     _description = 'modulo_base.modulo_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
