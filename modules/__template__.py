from core.module import *
from core.option import *
import core.engines.arma3 as engine



class Module(BaseModule):
	__info__ = {
		"name": "the name of your module",
		"description": "short description",
		"authors": ("author1", "author2"),
		"tags": ("seperate,tags,with,comma"),
	}

	string_option = OptString("default_val", "Option description")
	bool_option = OptBool(True, "Option description")

	def __init__(self):
		# This function is executed when your module is loaded
		pass

	def check(self):
		''' This function is executed before the user runs your module
			Any prerequists for your module should be checked in this function
			Return: Boolean - Can the module run safely?
		'''
		return True

	def run(self):
		# This function is executed when the user runs your module
		pass