from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "map teleport",
		"description": "enables alt-clicking on the map to teleport",
		"authors": ("aw3"),
		"tags": ("arma,local,localplayer,teleport"),
	}

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("""player onMapSingleClick "if (_alt) then {vehicle player setPosATL _pos}";""")