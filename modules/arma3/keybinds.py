from core.module import *
from core.option import *
import core.engines.arma3 as engine

import core.globals as g
import keyboard


class Module(BaseModule):
	__info__ = {
		"name": "keybinds",
		"description": "binds the numpad to certain keybinds",
		"authors": ("aw3"),
		"tags": ("arma"),
	}

	enable = OptBool(True, "Whether to enable/disable keybinds")

	def run(self):
		if not self.enable:
			keyboard.unhook_all()
			return
		keyboard.hook(self.keyboard_event)

	def keyboard_event(self, event):
		scan_codes = {80: self.player_prev, 72: self.player_next, 76: self.run_module}

		if not event.scan_code in scan_codes:
			return

		if not keyboard.is_pressed(event.scan_code):
			return

		scan_codes[event.scan_code]()

	def player_next(self):
		mod = g.current_module
		if not mod or not hasattr(mod, "target"):
			return

		players = engine.get_players()
		if not players or not len(players):
			print("no plrs")
			return

		target = mod.target
		size = len(players)
		i = size

		try:
			i = players.index(mod.target)
		except Exception as e:
			pass
		if i+1 >= size:
			target = players[0]
		else:
			target = players[i+1]
		setattr(mod, "target", target)
		mod.module_attributes["target"][0] = target


	def player_prev(self):
		mod = g.current_module
		if not mod or not hasattr(mod, "target"):
			return
			
		players = engine.get_players()
		if not players or not len(players):
			return

		target = mod.target
		size = len(players)
		i = size

		try:
			i = players.index(mod.target)
		except Exception as e:
			pass
		if i <= 0:
			target = players[-1]
		else:
			target = players[i-1]
		setattr(mod, "target", target)
		mod.module_attributes["target"][0] = target

	def run_module(self):
		mod = g.current_module
		if not mod:
			return
		if mod.check():
			mod.run()