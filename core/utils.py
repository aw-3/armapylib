from __future__ import print_function
from __future__ import absolute_import

import threading
import re
import os
import importlib
import string
import random
from functools import wraps



import modules as _modules
import core.engines as _engines

MODULES_DIR = _modules.__path__[0]
ENGINES_DIR = _engines.__path__[0]

def index_modules(modules_directory: str = MODULES_DIR) -> list:
    """ Returns list of all modules
    :param str modules_directory: path to modules directory
    :return list: list of found modules
    """

    modules = []
    for root, dirs, files in os.walk(modules_directory):
        _, package, root = root.rpartition("\\modules")
        root = root.replace(os.sep, ".")
        files = filter(lambda x: not x.startswith("__") and x.endswith(".py"), files)
        modules.extend(map(lambda x: ".".join((root, os.path.splitext(x)[0])), files))
    modules = ["".join(["modules",mod]) for mod in modules]
    return modules


def import_module(path: str):
    """ Imports module
    :param str path: absolute path to module e.g. modules.multi.godmode
    :return: module or error
    """

    try:
        module = importlib.import_module(path)
        if hasattr(module, "Module"):
            return getattr(module, "Module")
        else:
            raise ImportError("No module named '{}'".format(path))

    except (ImportError, AttributeError, KeyError) as err:
        raise Exception(
            "Error during loading '{}'\n\n"
            "Error: {}\n\n"
            "It should be valid path to the module. "
            "Use <tab> key multiple times for completion.".format(humanize_path(path), err)
        )

def iter_modules(modules_directory: str = MODULES_DIR) -> list:
    modules = index_modules(modules_directory)
    #modules = map(lambda x: "".join(["modules", x]), modules)
    for path in modules:
        yield import_module(path), humanize_path(path)

def pythonize_path(path: str) -> str:
    return path.replace("/", ".")


def humanize_path(path: str) -> str:
    return path.replace(".", "/")


def index_engines(modules_directory: str = ENGINES_DIR) -> list:
    engines = []
    for root, dirs, files in os.walk(modules_directory):
        _, package, root = root.rpartition("\\engines")
        root = root.replace(os.sep, ".")
        files = filter(lambda x: not x.startswith("__") and x.endswith(".py"), files)
        engines.extend(map(lambda x: ".".join((root, os.path.splitext(x)[0])), files))
    engines = ["".join(["engines",eng]) for eng in engines]
    return engines


def __cprint(*args, **kwargs):
    if not kwargs.pop("verbose", True):
        return

    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")

    print(*args, sep=sep, end=end)


def print_error(*args, **kwargs) -> None:
    # Print error message prefixing it with [-]
    __cprint("\033[91m[-]\033[0m", *args, **kwargs)


def print_status(*args, **kwargs) -> None:
    # Print status message prefixing it with [-]
    __cprint("\033[94m[*]\033[0m", *args, **kwargs)


def print_success(*args, **kwargs) -> None:
    # Print success message prefixing it with [-]
    __cprint("\033[92m[+]\033[0m", *args, **kwargs)


def print_info(*args, **kwargs) -> None:
    # Print info message prefixing it with [-]
    __cprint(*args, **kwargs)

def pprint_dict_in_order(dictionary, order=None) -> None:
    order = order or ()

    def prettyprint(title, body):
        print_info("\n{}:".format(title.capitalize()))
        if not isinstance(body, str):
            for value_element in body:
                print_info("- ", value_element)
        else:
            print_info(body)

    keys = list(dictionary.keys())
    for element in order:
        try:
            key = keys.pop(keys.index(element))
            value = dictionary[key]
        except (KeyError, ValueError):
            pass
        else:
            prettyprint(element, value)

    for rest_keys in keys:
        prettyprint(rest_keys, dictionary[rest_keys])

def print_table(headers, *args, **kwargs) -> None:
    extra_fill = kwargs.get("extra_fill", 5)
    header_separator = kwargs.get("header_separator", "-")

    if not all(map(lambda x: len(x) == len(headers), args)):
        print_error("Headers and table rows tuples should be the same length.")
        return

    def custom_len(x):
        try:
            return len(x)
        except TypeError:
            return 0

    fill = []
    headers_line = '   '
    headers_separator_line = '   '
    for idx, header in enumerate(headers):
        column = [custom_len(arg[idx]) for arg in args]
        column.append(len(header))

        current_line_fill = max(column) + extra_fill
        fill.append(current_line_fill)
        headers_line = "".join((headers_line, "{header:<{fill}}".format(header=header, fill=current_line_fill)))
        headers_separator_line = "".join((
            headers_separator_line,
            "{:<{}}".format(header_separator * len(header), current_line_fill)
        ))

    print_info()
    print_info(headers_line)
    print_info(headers_separator_line)
    for arg in args:
        content_line = "   "
        for idx, element in enumerate(arg):
            content_line = "".join((
                content_line,
                "{:<{}}".format(element, fill[idx])
            ))
        print_info(content_line)

    print_info()


