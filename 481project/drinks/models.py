from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from google.appengine.ext import ndb
from django.utils.text import slugify

@python_2_unicode_compatible
class Drink(ndb.Model):
    drink_name = ndb.StringProperty()
    drink_garnish = ndb.StringProperty()
    drink_inst = ndb.StringProperty()
    drink_glass = ndb.StringProperty()
    drink_slug = ndb.StringProperty()
    ingredients= ndb.JsonProperty()

    def __str__(self):
        return self.drink_name

 
class AllIngredients(ndb.Model):
    list= ndb.JsonProperty()
		 
class User(ndb.Model):
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	def __str__(self):
		return self.username

@python_2_unicode_compatible
class Ingredients(ndb.Model):
    ing_name = ndb.StringProperty()
    ing_amount = ndb.StringProperty()
    def __str__(self):
        return self.ing_name		
		
class DrinkLink(ndb.Model):
	user_key= ndb.KeyProperty()
	drink_key= ndb.KeyProperty()
	
class UserIng(ndb.Model):
	ing_list=ndb.JsonProperty()
	
class DrinkType(ndb.Model):
	drink_type=ndb.StringProperty()
	def __str__(self):
		return slugify(self.drink_type)
	
# Create your models here.
