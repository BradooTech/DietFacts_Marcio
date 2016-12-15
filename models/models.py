# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	
	calories = fields.Integer('Calories')
	serving_size = fields.Float('Serving Size')
	last_updated = fields.Date('Last Updated')
	
class DietFacts_res_users_meal(models.Model):
	_name = 'res.users.meal'
	name = fields.Char("Meal Name")
	meal_date = fields.Datetime("Menu Date")
	#item_ids = fields.One2many()
	user_id = fields.Many2one('res.users','Meal User') 
	notes = fields.Text('Meal Notes')
	
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
