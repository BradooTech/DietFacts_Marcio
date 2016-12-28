# -*- coding: utf-8 -*-

from odoo import models, fields, api, osv, exceptions, _

class Dietfacts_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	
	calories = fields.Integer('Calories')
	serving_size = fields.Float('Serving Size')
	last_updated = fields.Date('Last Updated')
	products_nutrients_id = fields.One2many('product.template.nutrients', 'product_id')
	nutrition_score = fields.Float(string="Nutrition Score", store=True, compute="_calcscore")
	
	@api.one
	@api.depends('products_nutrients_id', 'products_nutrients_id.value')
	def _calcscore(self):
		currentscore = 0
		count = 0
		
		
		for i in self.products_nutrients_id:
			count += 1
				
			if (i.nutrients_id.uom_id.name == "mg"):
				currentscore = currentscore + i.value
			
			elif (i.nutrients_id.uom_id.name == "g"):
				currentscore = currentscore + (i.value * 1000)
			
			elif(i.nutrients_id.uom_id.name == "kg"):
				currentscore = currentscore + (i.value * 1000000)
			
			else:
				raise exceptions.ValidationError(_("Seu burro"))
				count -= 1
			
			
		self.nutrition_score = currentscore #/ count
		
		
class DietFacts_res_users_meal(models.Model):
	_name = 'res.users.meal'
	name = fields.Char("Meal Name")
	meal_date = fields.Datetime("Menu Date")
	item_ids = fields.One2many('res.users.mealitem', 'meal_id')
	user_id = fields.Many2one('res.users', 'Meal User') 
	notes = fields.Text('Meal Notes')
	totalcalories = fields.Integer(string="Total Calories", store=True, compute="_calccalories")
	totalitems = fields.Integer(string="Total Items", store=True, compute="_calcmealitems")
	largemeal = fields.Boolean("Large Meal")
	
	@api.onchange('totalcalories')
	def checkonohange(self):
		if (self.totalcalories > 500):
			self.largemeal = True
		elif (self.calories < 500):
			self.largemeal = False
			
	@api.one
	@api.depends('item_ids', 'item_ids.servings')
	def _calccalories(self):
		currentcalories = 0
		for i in self.item_ids:
			currentcalories = currentcalories + (i.calories * i.servings)
		self.totalcalories = currentcalories
		
		
	@api.one
	@api.depends('item_ids')
	def _calcmealitems(self):
		currentitems = 0
		for i in self.item_ids:
			currentitems += 1
		self.totalitems = currentitems
		
	
class DietFacts_res_users_mealitem(models.Model):
	_name = 'res.users.mealitem'
	meal_id = fields.Many2one('res.users.meal')
	item_id = fields.Many2one('product.template', 'Menu Item')
	servings = fields.Float('Servings')
	calories = fields.Integer(related='item_id.calories', string="Calories Per Serving", store=True, readonly=True)
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
	uom = fields.Char(related='nutrients_id.uom_id.name', string="Units Of Measure", readonly=True)
	

	
	
	
# 	dietitem = fields.Boolean("Diet Item")
#     _name = 'dietfacts.dietfacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
