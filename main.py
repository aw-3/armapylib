from cmd import Cmd
import os

import core.constants as constants
import core.globals as g
import core.utils as utils
from core.winutils import *

# testing
import core.engines.arma3 as a3

class armapylib(Cmd):
	engines = utils.index_engines()

	modules = utils.index_modules()
	
	search_results = None

	prompt = "APL > \033[33m"
	intro = constants.BANNER % (color_text.yellow("armapylib v" + constants.VERSION),
		color_text.red(str(len(engines)) + " engine"),
		color_text.magenta(str(len(modules)) + " modules"))

	ruler = "#"

	__hiden_methods = ('do_EOF',)

	def get_names(self):
		return [n for n in dir(self.__class__) if n not in self.__hiden_methods]

	def do_exit(self, input):
		'''exits'''
		print("\033[0m", end = '')
		return True

	do_EOF = do_exit

	def do_search(self, input):
		'''search for a module'''

		self.search_results = []

		print("MODULE" + " "*54 + "DESCRIPTION")
		print()

		i = 0
		for mod,modpath in utils.iter_modules():
			if input in modpath:
				self.search_results.append([mod,modpath])
				print(str(i) + " " + modpath + " "*(60-len(modpath)) + mod.__info__["description"])
				i += 1

	def do_show(self, input):
		'''show [engines|modules|all]'''
		try:
			getattr(self, "_show_{}".format(input))()
		except AttributeError:
			print("Unknown show sub-command '%s'" % input)

	def _show_engines(self):
		print("ENGINE")
		print()

		for x in self.engines:
			print(utils.humanize_path(x))

	def _show_modules(self):
		self.do_search("")

	_show_mods = _show_modules
	def _show_all(self):
		self._show_engines()
		print()
		self._show_modules()

	def do_use(self, input):
		'''selects a given module'''

		try:
			i = int(input)
			g.current_module = self.search_results[i][0]()
			self.prompt = "APL module(" + color_text.red(self.search_results[i][1]) + ") > \033[33m"
			return
		except Exception as e:
			pass

		for mod,modpath in utils.iter_modules():
			if input in modpath:
				g.current_module = mod()
				self.prompt = "APL module(" + color_text.red(modpath) + ") > \033[33m"
				return
		print("no module found")

	do_select = do_use

	def do_info(self, input):
		'''show info for selected module'''
		if not g.current_module:
			return

		print("-"*64)
			
		utils.pprint_dict_in_order(g.current_module.__info__,
			("name", "description"))

		print("\nOptions: ")
		opts = g.current_module.options
		utils.print_table(["Name", "Value", "Description"], *g.current_module.get_opts(*opts))

	def do_set(self, input):
		'''set module option'''
		if not g.current_module:
			return

		key, _, value = input.partition(" ")
		if key in g.current_module.options:
			setattr(g.current_module, key, value)
			g.current_module.module_attributes[key][0] = value

	def do_run(self,input):
		'''runs selected module'''
		if not g.current_module:
			print("no module selected")
			return

		if not g.current_module.check():
			print("module check failed - running this module may be unsafe. aborting..")
			return
		
		print("running module..")

		try:
			g.current_module.run()
			print("module completed")
		except Exception as e:
			print("Error running module: %s" % str(e))

	def do_test(self, input):
		a = a3.aob()
		for x in a:
			print(hex(x))

	def precmd(self, line):
		print("\033[0m", end = '')
		return Cmd.precmd(self, line)

	def emptyline(self):
		pass

elevate()

os.system("cls")
os.system("color")
armapylib().cmdloop()