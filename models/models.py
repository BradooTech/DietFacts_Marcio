# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	
	calories = fields.Integer('Calories')
	serving_size = fields.Float('Serving Size')
	last_updated = fields.Date('Last Updated')
	products_nutrients_id = fields.One2many('product.template.nutrients','product_id')
	
	
class DietFacts_res_users_meal(models.Model):
	_name = 'res.users.meal'
	name = fields.Char("Meal Name")
	meal_date = fields.Datetime("Menu Date")
	item_ids = fields.One2many('res.users.mealitem','meal_id')
	user_id = fields.Many2one('res.users','Meal User') 
	notes = fields.Text('Meal Notes')
	totalcalories = fields.Integer(string="Total Calories", store=True, compute="_calccalories")
	totalitems = fields.Integer(string="Total Items", store=True, compute="_calcmealitems")
		
	@api.one
	@api.depends('item_ids','item_ids.servings')
	def _calccalories(self):
		currentcalories=0
		for i in self.item_ids:
			currentcalories = currentcalories + (i.calories * i.servings)
		self.totalcalories = currentcalories
		
		
	@api.one
	@api.depends('item_ids')
	def _calcmealitems(self):
		currentitems=0
		for i in self.item_ids:
			currentitems += 1
		self.totalitems = currentitems
		
	
class DietFacts_res_users_mealitem(models.Model):
	_name = 'res.users.mealitem'
	meal_id = fields.Many2one('res.users.meal')
	item_id = fields.Many2one('product.template','Menu Item')
	servings = fields.Float('Servings')
	calories = fields.Integer(related='item_id.calories', string = "Calories Per Serving", store = True, readonly=True)
	notes = fields.Text('Meal item notes')
	
class DietFacts_product_nutrients(models.Model):
	_name = 'product.nutrients'
	
	name = fields.Char("Nutrient Name")
	uom_id = fields.Many2one('product.uom', 'Unit Of Measure')
	description = fields.Text("Description")
	
class DietFacts_product_template_nutrients(models.Model):
	_name = 'product.template.nutrients'
	
	nutrients_id = fields.Many2one('product.nutrients')
	product_id = fields.Many2one('product.template')
	value = fields.Float("Value")
	dailypercent = fields.Float("Daily Percentage")
	uom = fields.Char(related='nutrients_id.uom_id.name', string = "Units Of Measure", readonly=True)
	


	
	
	
#	dietitem = fields.Boolean("Diet Item")
#     _name = 'dietfacts.dietfacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
