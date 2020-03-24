from core.module import *
from core.option import *
import core.engines.arma3 as engine



class Module(BaseModule):
	__info__ = {
		"name": "run code",
		"description": "execute user defined script",
		"authors": ("aw3"),
		"tags": ("arma,dangerous"),
	}

	text = OptString('systemchat "test";', "Script to execute")
	remote = OptBool(False, "Run on server")

	def run(self):
		if not self.remote:
			engine.execute(self.text)
		else:
			engine.execute_remote(self.text, True)