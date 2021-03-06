from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "cursor delete",
		"description": "deletes whatever you're looking at (deleteVehicle)",
		"authors": ("aw3"),
		"tags": ("arma,local,cursortarget"),
	}

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("deleteVehicle cursorTarget;")