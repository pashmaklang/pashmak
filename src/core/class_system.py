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
        from .current_prog import current_prog
        class_copy = ClassObject(copy.deepcopy(self.props), copy.deepcopy(self.methods))
        class_copy.__theclass__ = copy.deepcopy(self)
        class_copy.__name__
        tmp_is_in_class = False
        try:
            tmp_is_in_class = copy.deepcopy(current_prog.current_class)
            del current_prog.current_class
        except:
            pass
        if len(args) == 1:
            args = args[0]
        class_copy.methods['__init__'](args)
        if tmp_is_in_class:
            current_prog.current_class = tmp_is_in_class
        return class_copy

class ClassObject:
    """ Class initiated object """
    def __init__(self, props: ClassProps, methods: dict):
        self.props = props
        self.methods = methods
        for k in self.methods:
            self.methods[k].parent_object = self

    def __str__(self):
        from .current_prog import current_prog
        str_magic_method = self.methods['__str__']
        current_prog.exec_func(str_magic_method.body, True, {'this': self})
        return str(current_prog.get_mem())

    def __getattr__(self, attrname):
        from .current_prog import current_prog
        if attrname == 'props' or attrname == 'methods':
            return super().__getattr__(attrname)
        try:
            return self.props[attrname]
        except KeyError:
            try:
                self.methods[attrname].parent_object = self
                return self.methods[attrname]
            except KeyError:
                raise AttributeError(attrname)
