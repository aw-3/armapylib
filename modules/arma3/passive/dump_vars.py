import os
from core.module import *
from core.option import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "dump vars",
		"description": "dumps all variables in the mission namespace",
		"authors": ("aw3"),
		"tags": ("arma,passive,dump"),
	}

	var_substr = OptString("", "Variable substring")

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		for var in engine.get_mission_variables():
			if not self.var_substr in var:
				continue
			print(var)