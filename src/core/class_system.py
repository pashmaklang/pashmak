#
# class_system.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of Pashmak.
#
# Pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pashmak.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################

""" Classes """

import copy
from . import parser

class ClassConstError(Exception):
    pass

class ClassProps(dict):
    """ The `obj.props` """
    def __getattr__(self, attrname):
        try:
            return self[attrname]
        except KeyError:
            raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        try:
            self[attrname]
            if self[attrname] != None:
                if attrname[0] == '_':
                    raise ClassConstError('property "' + attrname + '" is const and cannot be changed')
        except KeyError:
            pass
        self[attrname] = value

class Class:
    """ Class model """
    def __init__(self, name: str, props: dict):
        self.props = ClassProps(props)
        self.methods = {}

    def __call__(self, *args, **kwargs):
        """ Make new object from class """
        class_copy = ClassObject(copy.deepcopy(self.props), copy.deepcopy(self.methods))
        class_copy.__prog__ = self.__prog__
        class_copy.__theclass__ = copy.deepcopy(self)
        class_copy.__name__
        tmp_is_in_class = False
        try:
            tmp_is_in_class = copy.deepcopy(self.__prog__.current_class)
            del self.__prog__.current_class
        except:
            pass
        if len(args) == 1:
            args = args[0]
        class_copy.methods['__init__'](args)
        if tmp_is_in_class:
            self.__prog__.current_class = tmp_is_in_class
        return class_copy

class ClassObject:
    """ Class initiated object """
    def __init__(self, props: ClassProps, methods: dict):
        self.props = props
        self.methods = methods

    def __str__(self):
        str_magic_method = self.methods['__str__']
        self.__prog__.exec_func(str_magic_method.body, True, {'this': self})
        return str(self.__prog__.get_mem())

    def __getattr__(self, attrname):
        if attrname == 'props' or attrname == 'methods' or attrname == '__prog__':
            return super().__getattr__(attrname)
        for k in self.methods:
            self.methods[k].parent_object = self
            self.methods[k].prog = self.__prog__
        for k in self.props:
            if type(self.props[k]) == Class:
                self.props[k].__prog__ = self.__prog__
                self.props[k].__name__
        try:
            if type(self.props[attrname]) == ClassObject:
                self.props[attrname].__prog__ = self.__prog__
            return self.props[attrname]
        except KeyError:
            try:
                return self.methods[attrname]
            except KeyError:
                raise AttributeError(attrname)
