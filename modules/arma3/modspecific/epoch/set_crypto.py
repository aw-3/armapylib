from core.module import *
from core.option import *
import core.engines.arma3 as engine



class Module(BaseModule):
	__info__ = {
		"name": "set crypto",
		"description": "sets epoch currency (locally)",
		"authors": ("aw3"),
		"tags": ("arma,epoch"),
	}

	crypto = OptInteger(5000, "How much crypto to set")

	def check(self):
		addons = engine.get_addons()
		epoch_addon = [x for x in addons if "@Epoch" in x]
		if not len(epoch_addon):
			print("Epoch not loaded.")
			return False
		return True

	def run(self):
		engine.execute("EPOCH_playerCrypto = %d;" % self.crypto)