from core.module import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "toggle recoil",
		"description": "toggles recoil coefficient and sway",
		"authors": ("aw3"),
		"tags": ("arma,local,localplayer"),
	}

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute("""if (unitRecoilCoefficient player != 0) then {
	player setUnitRecoilCoefficient 0;
	player setCustomAimCoef 0;
}
else {
	player setUnitRecoilCoefficient 1;
	player setCustomAimCoef 1;
}
			""")