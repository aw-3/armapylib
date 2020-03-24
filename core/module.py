from future.utils import with_metaclass, iteritems
from itertools import chain
from functools import wraps
import os
import core.utils as utils
from core.option import Option

class ModuleOptionsAggregator(type):
	""" Metaclass for base class.
	Metaclass is aggregating all possible Attributes that user can set.
	"""

	def __new__(cls, name, bases, attrs):
		try:
			base_module_attributes = chain([base.module_attributes for base in bases])
		except AttributeError:
			attrs["module_attributes"] = {}
		else:
			attrs["module_attributes"] = {k: v for d in base_module_attributes for k, v in iteritems(d)}

		for key, value in iteritems(attrs.copy()):
			if isinstance(value, Option):
				value.label = key
				attrs["module_attributes"].update({key: [value.display_value, value.description, value.advanced]})
			elif key == "__info__":
				#attrs["_{}{}".format(name, key)] = value
				#del attrs[key]
				pass
			elif key in attrs["module_attributes"]:  # removing module_attributes that was overwritten
				del attrs["module_attributes"][key]  # in the child and is not an Option() instance

		return super(ModuleOptionsAggregator, cls).__new__(cls, name, bases, attrs)

class BaseModuleMeta(metaclass=ModuleOptionsAggregator):
	__info__ = {}
	@property
	def options(self):
		return list(self.module_attributes.keys())

	def __str__(self):
		return self.__module__.split('.', 2).pop().replace('.', os.sep)

	def get_opts(self, *args):
		""" Generator returning module's Option attributes (option_name, option_value, option_description)
		:param args: Option names
		:return:
		"""
		for opt_key in args:
			try:
				opt_description = self.module_attributes[opt_key][1]
				opt_display_value = self.module_attributes[opt_key][0]
				if self.module_attributes[opt_key][2]:
					continue
			except (KeyError, IndexError, AttributeError):
				pass
			else:
				yield opt_key, opt_display_value, opt_description


class BaseModule(BaseModuleMeta):

	def __init__(self):
		pass

	def check(self):
		return True

	def run(self):
		pass