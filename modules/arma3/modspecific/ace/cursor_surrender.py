from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "cursor surrender",
		"description": "forces cursortarget to surrender",
		"authors": ("aw3"),
		"tags": ("arma,ace,cba,cursor"),
	}

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("""if (alive cursorTarget) then {["ace_captives_setSurrendered",[cursorTarget , not (captive cursorTarget)]] call CBA_fnc_globalEvent;};""")