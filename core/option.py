import re
import os.path

class Option(object):
    """ attribute that is set by the end user """

    def __init__(self, default, description="", advanced=False):
        self.label = None
        self.description = description

        try:
            self.advanced = bool(advanced)
        except ValueError:
            raise Exception("Invalid value. Cannot cast '{}' to boolean.".format(advanced))

        if default or default == 0:
            self.__set__("", default)
        else:
            self.display_value = ""
            self.value = ""

    def __get__(self, instance, owner):
        return self.value


class OptBool(Option):
    """ Option Bool attribute """

    def __init__(self, default, description="", advanced=False):
        self.description = description

        if default:
            self.display_value = "true"
        else:
            self.display_value = "false"

        self.value = default

        try:
            self.advanced = bool(advanced)
        except ValueError:
            raise Exception("Invalid value. Cannot cast '{}' to boolean.".format(advanced))

    def __set__(self, instance, value):
        if value == "true":
            self.value = True
            self.display_value = value
        elif value == "false":
            self.value = False
            self.display_value = value
        else:
            raise Exception("Invalid value. It should be true or false.")


class OptInteger(Option):
    """ Option Integer attribute """

    def __set__(self, instance, value):
        try:
            self.display_value = str(value)
            self.value = int(value)
        except ValueError:
            try:
                self.value = int(value, 16)
            except ValueError:
                raise Exception("Invalid option. Cannot cast '{}' to integer.".format(value))


class OptFloat(Option):
    """ Option Float attribute """

    def __set__(self, instance, value):
        try:
            self.display_value = str(value)
            self.value = float(value)
        except ValueError:
            raise Exception("Invalid option. Cannot cast '{}' to float.".format(value))


class OptString(Option):
    """ Option String attribute """

    def __set__(self, instance, value):
        try:
            self.value = self.display_value = str(value)
        except ValueError:
            raise Exception("Invalid option. Cannot cast '{}' to string.".format(value))

