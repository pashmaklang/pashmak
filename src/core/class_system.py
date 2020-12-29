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
    """ The `obj.__props__` """
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
        self.__props__ = ClassProps(props)
        self.__methods__ = {}
        self.__inheritance_tree__ = []
        self.__classname__ = name

    def __call__(self, *args, **kwargs):
        """ Make new object from class """
        from .current_prog import current_prog
        class_copy = ClassObject(copy.deepcopy(self.__props__), copy.deepcopy(self.__methods__))
        class_copy.__theclass__ = copy.deepcopy(self)
        class_copy.__name__
        class_copy.__inheritance_tree__ = self.__inheritance_tree__
        tmp_is_in_class = False
        try:
            tmp_is_in_class = copy.deepcopy(current_prog.current_class)
            current_prog.current_class = []
        except:
            pass
        if len(args) == 1:
            args = args[0]
        class_copy.__methods__['__init__'](args)
        if tmp_is_in_class:
            current_prog.current_class = tmp_is_in_class
        return class_copy

    def __getattr__(self, attrname):
        from .current_prog import current_prog
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__inheritance_tree__' or attrname == '__classname__':
            return super().__getattr__(attrname)
        try:
            return self.__props__[attrname]
        except KeyError:
            try:
                self.__methods__[attrname].parent_object = self
                return self.__methods__[attrname]
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__inheritance_tree__' or attrname == '__classname__':
            return super().__setattr__(attrname, value)
        self.__props__[attrname] = value

class ClassObject:
    """ Class initiated object """
    def __init__(self, props: ClassProps, methods: dict):
        self.__props__ = props
        self.__methods__ = methods
        for k in self.__methods__:
            self.__methods__[k].parent_object = self

    def __str__(self):
        from .current_prog import current_prog
        str_magic_method = self.__methods__['__str__']
        current_prog.exec_func(str_magic_method.body, True, {'this': self})
        return str(current_prog.get_mem())

    def __getattr__(self, attrname):
        from .current_prog import current_prog
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__theclass__' or attrname == '__inheritance_tree__':
            return super().__getattr__(attrname)
        try:
            return self.__props__[attrname]
        except KeyError:
            try:
                self.__methods__[attrname].parent_object = self
                return self.__methods__[attrname]
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__theclass__' or attrname == '__inheritance_tree__':
            return super().__setattr__(attrname, value)
        self.__props__[attrname] = value
