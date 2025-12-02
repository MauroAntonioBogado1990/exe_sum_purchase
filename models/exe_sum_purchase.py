# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_cost = fields.Float(
        string='Total de Costo',
        compute='_compute_total_cost',
        store=True,
        readonly=True
    )

    @api.depends('order_line.purchase_price')
    def _compute_total_cost(self):
        for order in self:
            order.total_cost = sum(line.purchase_price for line in order.order_line)