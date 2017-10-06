# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ProductOrder(models.Model):

	_name = 'product.order'

	name = fields.Char('Name')
	partner_id = fields.Many2one('res.partner','Customer',required=True)
	order_date = fields.Date('Order Date')
	order_lines = fields.One2many('product.order.lines','order_id','Order Lines')

	@api.model
	def create(self, vals):
		print '======>',vals
		vals['name'] = self.env['ir.sequence'].next_by_code('invoice.name.seq')
		print '======>',vals
		res = super(ProductOrder, self).create(vals)
		return res

class SaleOrderLines(models.Model):
	_name = "product.order.lines"
	_rec_name = 'order_id'

	product_id = fields.Many2one('product.template')
	hsn_no = fields.Char('HSN/SAC')
	qty = fields.Integer('Quantity')
	price = fields.Float('price')
	amount = fields.Float('Taxable Amount')
	gst_per = fields.Float('GST%')
	cgst = fields.Float('CGST')
	sgst = fields.Float('SGST')
	total = fields.Float('Net Amount')
	company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id)
	currency_id = fields.Many2one("res.currency", string="Currency", readonly=True, required=True, default=lambda self: self.env.user.company_id.currency_id)
	order_id = fields.Many2one('product.order',string='order')

	@api.onchange('product_id')
	def change_info(self):
		if self.product_id:
			self.hsn_no = self.product_id.hsn_no
			self.price = self.product_id.list_price
			self.gst_per = self.product_id.gst_per

	@api.onchange('qty')
	def amount_info(self):
		if self.qty:
			gst = self.gst_per / 2
			self.amount = self.price * self.qty
			self.cgst = (self.amount * gst)/100
			self.sgst = (self.amount * gst)/100
			self.total = self.amount + self.cgst + self.sgst

	@api.model
	def create(self, vals):
		print '======>',vals
		res = super(SaleOrderLines, self).create(vals)
		return res
