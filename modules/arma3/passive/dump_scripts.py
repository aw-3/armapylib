import os
from core.module import *
from core.option import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "dump scripts",
		"description": "dumps all scripts running on the client",
		"authors": ("aw3"),
		"tags": ("arma,passive,dump"),
	}

	dump_path = OptString("C:/scriptdump", "Directory for scripts to be written to")

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		scripts = engine.get_running_scripts()

		try:
			os.mkdir(self.dump_path)
		except Exception as e:
			pass

		for i,script in enumerate(scripts):
			if script[0].startswith("A3"):
				continue

			with open(self.dump_path + "/" + str(i) + ".txt", "w") as f:
				f.write("// " + script[0] + "\n\n" + script[1])