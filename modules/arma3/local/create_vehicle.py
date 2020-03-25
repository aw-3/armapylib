from core.module import *
from core.option import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "map teleport",
		"description": "spawn a vehicle via createVehicle",
		"authors": ("aw3"),
		"tags": ("arma,dangerous"),
	}

	vehicle = OptString("B_Heli_Transport_03_F", "Vehicle classname (CfgVehicles)")

	def check(self):
		# should check if vehicle classname exists within cfgvehicles-- need api access
		return len(engine.get_players())

	def run(self):
		engine.execute(f"createVehicle ['{self.vehicle}', position player, [], 0, 'NONE'];")