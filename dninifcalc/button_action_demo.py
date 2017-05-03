# -*- coding: utf-8 -*-
from openerp import models, fields, api

#Non-odoo library
import random
from random import randint
import string

class button_action_demo(models.Model):
    _name = 'button.demo'
    name = fields.Integer()
    password = fields.Char()
    
    


    @api.multi
    @api.depends('name')
    def generate_record_password(self):
	 
	letras = 'TRWAGMYFPDXBNJZSQVHLCKE'	
	resto = int(self.name) % 23
	self.ensure_one()
	#Generates a random password between 12 and 15 characters long and writes it to the record.
	self.write({
	    'password': letras[resto]
	})

    @api.multi
    def clear_record_data(self):
	self.ensure_one()
	self.write({
	    'name': '',
	    'password': ''
	})
