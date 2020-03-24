from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "arsenal",
		"description": "opens the ace3 arsenal",
		"authors": ("aw3"),
		"tags": ("arma,local,localplayer"),
	}

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("[player, player, true] call ace_arsenal_fnc_openBox;")