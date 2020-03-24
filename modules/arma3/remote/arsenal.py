from core.module import *
from core.option import *
import core.engines.arma3 as engine



class Module(BaseModule):
	__info__ = {
		"name": "remote arsenal",
		"description": "opens the virtual arsenal for selected player",
		"authors": ("aw3"),
		"tags": ("arma,remote,dangerous"),
	}

	target = OptString("", "Target player name")

	def check(self):
		return self.target in engine.get_players()

	def run(self):
		engine.execute_remote_player('["Open", [true]] call BIS_fnc_arsenal;', self.target)