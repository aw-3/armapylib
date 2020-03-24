from core.module import *
from core.option import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "stamina",
		"description": "stamina bar",
		"authors": ("aw3"),
		"tags": ("arma,local,localplayer"),
	}

	enable = OptBool(False, "Enable/Disable stamina")

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("enableFatigue %s" % (self.enable and "true;" or "false;"))