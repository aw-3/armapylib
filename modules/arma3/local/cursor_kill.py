from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "cursor kill",
		"description": "kills whatever you're looking at (setDamage)",
		"authors": ("aw3"),
		"tags": ("arma,local,cursortarget"),
	}

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("cursorTarget setDamage 1;")