# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProductTemplateInvoice(models.Model):

	_inherit = 'product.template'

	hsn_no = fields.Char('HSN/SAC')
	gst_per = fields.Float('GST%')