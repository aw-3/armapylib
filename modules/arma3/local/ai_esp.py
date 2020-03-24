from core.module import *
from core.option import *
import core.engines.arma3 as engine

class Module(BaseModule):
	__info__ = {
		"name": "ai esp",
		"description": "ESP for _enemy_ NPCs",
		"authors": ("aw3"),
		"tags": ("arma,local,esp"),
	}

	max_distance = OptInteger(3000, "Max render distance")

	def __init__(self):
		pass

	def check(self):
		return len(engine.get_players())

	def run(self):
		engine.execute(("""apl_ai_md = %d;""" % self.max_distance) + """
str addMissionEventHandler ["Draw3D", {	
	{		
		if ((alive _x)) then {
			if ( !isPlayer _x and (side group _x != side group player) ) then {
				_dist = round(player distance _x);
				if(_dist <= apl_ai_md) then {
					_color = [1,0.5,0,1];
					_text = format["%1 : %2m", "AI", str _dist];
					_pos = [visiblePosition _x select 0, visiblePosition _x select 1, visiblePosition _x select 2];
					if () then {
						_color = [0,0,1,1];
					};
					drawIcon3D ["", _color, _pos, 0, 0, 0, _text, 1, 0.020, "TahomaB"];
				}
			}
		}
	} foreach (allUnits);
}] call BIS_fnc_addStackedEventHandler;
			""")