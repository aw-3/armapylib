from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "arsenal",
		"description": "opens the virtual arsenal",
		"authors": ("aw3"),
		"tags": ("arma,local,localplayer"),
	}

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("""["Open", [true]] call BIS_fnc_arsenal;""")