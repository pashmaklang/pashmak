#
# class_system.py
#
# The Pashmak Project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
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
from .function import Function

class ClassConstError(Exception):
    pass

class SuperError(Exception):
    pass

class Class:
    """ Class model """
    def __init__(self, name: str):
        self.__props__ = {}
        self.__methods__ = {}
        self.__inheritance_tree__ = []
        self.__classname__ = name

    def __call__(self, *args, **kwargs):
        """ Make new object from class """
        from .current_prog import current_prog
        the_props = []
        the_methods = []
        for item in self.__inheritance_tree__:
            the_props.append(current_prog.classes[item].__props__)
            the_methods.append(current_prog.classes[item].__methods__)
        class_copy = ClassObject(copy.deepcopy(the_props), copy.deepcopy(the_methods))
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
        i = len(class_copy.__methods__)-1
        init_method = None
        while i >= 0:
            try:
                init_method = class_copy.__methods__[i]['__init__']
                break
            except KeyError:
                pass
            i -= 1
        init_method(args)
        if tmp_is_in_class:
            current_prog.current_class = tmp_is_in_class
        return class_copy

    def __getattr__(self, attrname):
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

class ClassPropAndMethodCollection:
    def __init__(self, *args):
        try:
            self.__methods__
            self.__props__
            return self.__methods__['__init__'](args)
        except:
            pass
        self.__methods__ = args[0]
        self.__props__ = args[1]

    def __getattr__(self, attrname):
        if attrname == '__props__' or attrname == '__methods__':
            return super().__getattr__(attrname)
        try:
            return self.__props__[attrname]
        except KeyError:
            try:
                return self.__methods__[attrname]
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname == '__props__' or attrname == '__methods__':
            return super().__setattr__(attrname, value)
        self.__props__[attrname] = value

    def __str__(self):
        return self.__methods__['__str__']()

class ClassObject:
    """ Class initiated object """
    def __init__(self, props: dict, methods: dict):
        self.__props__ = props
        self.__methods__ = methods
        i = 0
        while i < len(self.__methods__):
            for k in self.__methods__[i]:
                self.__methods__[i][k].parent_object = self
            i += 1
        i = 0
        while i < len(self.__props__):
            for k in self.__props__[i]:
                if type(self.__props__[i][k]) == Function:
                    self.__props__[i][k].parent_object = self
            i += 1

    def super(self, name: str):
        i = len(self.__inheritance_tree__)-1
        found_index = False
        is_found = False
        while i >= 0:
            try:
                if self.__inheritance_tree__[i] == name:
                    found_index = i
                    is_found = True
                    break
            except IndexError:
                pass
            i -= 1
        if is_found == False:
            raise SuperError('unknow parent "' + name + '"')
            return
        return ClassPropAndMethodCollection(self.__methods__[found_index], self.__props__[found_index])

    def __get_method__(self, method_name: str):
        """ Returns the method callable object """
        method = None
        i = len(self.__methods__)-1
        while i >= 0:
            try:
                method = self.__methods__[i][method_name]
                break
            except KeyError:
                pass
            i -= 1
        if method != None:
            method.parent_object = self
        return method

    def __str__(self):
        return self.__get_method__('__str__')()

    def __getattr__(self, attrname):
        from .current_prog import current_prog
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__theclass__' or attrname == '__inheritance_tree__':
            return super().__getattr__(attrname)
        try:
            i = len(self.__props__)-1
            while i >= 0:
                try:
                    if type(self.__props__[i][attrname]) == Function:
                        self.__props__[i][attrname].parent_object = self
                    return self.__props__[i][attrname]
                except KeyError:
                    pass
                i -= 1
            raise KeyError()
        except KeyError:
            try:
                tmp_method = self.__get_method__(attrname)
                if tmp_method != None:
                    return tmp_method
                raise KeyError()
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname == '__props__' or attrname == '__methods__' or attrname == '__theclass__' or attrname == '__inheritance_tree__':
            return super().__setattr__(attrname, value)
        try:
            self.__props__[-1][attrname]
            if self.__props__[-1][attrname] != None:
                if attrname[0] == '_':
                    raise ClassConstError('property "' + attrname + '" is const and cannot be changed')
                    return
        except KeyError:
            pass
        self.__props__[-1][attrname] = value
