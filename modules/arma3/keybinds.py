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

		scan_codes[event.scan_code]()

	def player_next(self):
		mod = g.current_module
		if not mod or not hasattr(mod, "target"):
			return
		players = engine.get_players()

		try:
			size = len(players)
			i = players.index(mod.target)
			if i+1 >= size:
				mod.target = players[0]
			else:
				mod.target = players[i+1]
		except Exception as e:
			return


	def player_prev(self):
		mod = g.current_module
		if not mod or not hasattr(mod, "target"):
			return
		players = engine.get_players()

		i = 0

		try:
			i = players.index(mod.target)
		except Exception as e:
			i = 0

		try:
			size = len(players)
			if i <= 0:
				mod.target = players[-1]
			else:
				mod.target = players[i-1]
		except Exception as e:
			print(e)
			return

	def run_module(self):
		mod = g.current_module
		if not mod:
			return
		if mod.check():
			mod.run()