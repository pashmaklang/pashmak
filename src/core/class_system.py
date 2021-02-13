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
from .function import Function

class ClassConstError(Exception):
    """ Will be raised when changing a const property """
    pass

class SuperError(Exception):
    """ Will be raised when trying to access a parent that does not in the inheritance tree """
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
        if attrname in ['__props__', '__methods__', '__inheritance_tree__', '__classname__']:
            return super().__getattr__(attrname)
        try:
            return self.__props__[attrname]
        except KeyError:
            try:
                return self.__methods__[attrname]
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname in ['__props__', '__methods__', '__inheritance_tree__', '__classname__']:
            return super().__setattr__(attrname, value)
        self.__props__[attrname] = value

class ClassPropAndMethodCollection:
    """ Only a object to handle properties and methods (Used by `super`) """
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
        if attrname in ['__props__', '__methods__']:
            return super().__getattr__(attrname)
        try:
            return self.__props__[attrname]
        except KeyError:
            try:
                return self.__methods__[attrname]
            except KeyError:
                raise AttributeError(attrname)

    def __setattr__(self, attrname, value):
        if attrname in ['__props__', '__methods__']:
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
                if isinstance(self.__props__[i][k], Function):
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

    def __getattr__(self, attrname):
        from .current_prog import current_prog
        if attrname in ['__props__', '__methods__', '__theclass__', '__inheritance_tree__']:
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
        if attrname in ['__props__', '__methods__', '__theclass__', '__inheritance_tree__']:
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

    # Magic methods start #

    def __str__(self):
        method = self.__get_method__('__str__')
        if method is None:
            return super().__str__()
        return method()

    def __eq__(self, other):
        method = self.__get_method__('__eq__')
        if method is None:
            return super().__eq__(other)
        return method(other)

    def __ne__(self, other):
        method = self.__get_method__('__ne__')
        if method is None:
            return super().__ne__(other)
        return method(other)

    def __lt__(self, other):
        method = self.__get_method__('__lt__')
        if method is None:
            return super().__lt__(other)
        return method(other)

    def __gt__(self, other):
        method = self.__get_method__('__gt__')
        if method is None:
            return super().__gt__(other)
        return method(other)

    def __le__(self, other):
        method = self.__get_method__('__le__')
        if method is None:
            return super().__le__(other)
        return method(other)

    def __ge__(self, other):
        method = self.__get_method__('__ge__')
        if method is None:
            return super().__ge__(other)
        return method(other)

    def __pos__(self):
        method = self.__get_method__('__pos__')
        if method is None:
            return super().__pos__()
        return method()

    def __neg__(self):
        method = self.__get_method__('__neg__')
        if method is None:
            return super().__neg__()
        return method()

    def __abs__(self):
        method = self.__get_method__('__abs__')
        if method is None:
            return super().__abs__()
        return method()

    def __invert__(self):
        method = self.__get_method__('__invert__')
        if method is None:
            return super().__invert__()
        return method()

    def __round__(self, n):
        method = self.__get_method__('__round__')
        if method is None:
            return super().__round__(n)
        return method(n)

    def __floor__(self):
        method = self.__get_method__('__floor__')
        if method is None:
            return super().__floor__()
        return method()

    def __ceil__(self):
        method = self.__get_method__('__ceil__')
        if method is None:
            return super().__ceil__()
        return method()

    def __trunc__(self):
        method = self.__get_method__('__trunc__')
        if method is None:
            return super().__trunc__()
        return method()

    def __add__(self, other):
        method = self.__get_method__('__add__')
        if method is None:
            return super().__add__(other)
        return method(other)

    def __sub__(self, other):
        method = self.__get_method__('__sub__')
        if method is None:
            return super().__sub__(other)
        return method(other)

    def __mul__(self, other):
        method = self.__get_method__('__mul__')
        if method is None:
            return super().__mul__(other)
        return method(other)

    def __floordiv__(self, other):
        method = self.__get_method__('__floordiv__')
        if method is None:
            return super().__floordiv__(other)
        return method(other)

    def __div__(self, other):
        method = self.__get_method__('__div__')
        if method is None:
            return super().__div__(other)
        return method(other)

    def __truediv__(self, other):
        method = self.__get_method__('__truediv__')
        if method is None:
            return super().__truediv__(other)
        return method(other)

    def __mod__(self, other):
        method = self.__get_method__('__mod__')
        if method is None:
            return super().__mod__(other)
        return method(other)

    def __divmod__(self, other):
        method = self.__get_method__('__divmod__')
        if method is None:
            return super().__divmod__(other)
        return method(other)

    def __pow__(self):
        method = self.__get_method__('__pow__')
        if method is None:
            return super().__pow__()
        return method()

    def __lshift__(self, other):
        method = self.__get_method__('__lshift__')
        if method is None:
            return super().__lshift__(other)
        return method(other)
        
    def __rshift__(self, other):
        method = self.__get_method__('__rshift__')
        if method is None:
            return super().__rshift__(other)
        return method(other)
        
    def __and__(self, other):
        method = self.__get_method__('__and__')
        if method is None:
            return super().__and__(other)
        return method(other)
        
    def __or__(self, other):
        method = self.__get_method__('__or__')
        if method is None:
            return super().__or__(other)
        return method(other)
        
    def __xor__(self, other):
        method = self.__get_method__('__xor__')
        if method is None:
            return super().__xor__(other)
        return method(other)

    def __radd__(self, other):
        method = self.__get_method__('__radd__')
        if method is None:
            return super().__radd__(other)
        return method(other)

    def __rsub__(self, other):
        method = self.__get_method__('__rsub__')
        if method is None:
            return super().__rsub__(other)
        return method(other)

    def __rmul__(self, other):
        method = self.__get_method__('__rmul__')
        if method is None:
            return super().__rmul__(other)
        return method(other)

    def __rfloordiv__(self, other):
        method = self.__get_method__('__rfloordiv__')
        if method is None:
            return super().__rfloordiv__(other)
        return method(other)

    def __rdiv__(self, other):
        method = self.__get_method__('__rdiv__')
        if method is None:
            return super().__rdiv__(other)
        return method(other)

    def __rtruediv__(self, other):
        method = self.__get_method__('__rtruediv__')
        if method is None:
            return super().__rtruediv__(other)
        return method(other)

    def __rmod__(self, other):
        method = self.__get_method__('__rmod__')
        if method is None:
            return super().__rmod__(other)
        return method(other)

    def __rdivmod__(self, other):
        method = self.__get_method__('__rdivmod__')
        if method is None:
            return super().__rdivmod__(other)
        return method(other)

    def __rpow__(self):
        method = self.__get_method__('__rpow__')
        if method is None:
            return super().__rpow__()
        return method()

    def __rlshift__(self, other):
        method = self.__get_method__('__rlshift__')
        if method is None:
            return super().__rlshift__(other)
        return method(other)

    def __rrshift__(self, other):
        method = self.__get_method__('__rrshift__')
        if method is None:
            return super().__rrshift__(other)
        return method(other)

    def __rand__(self, other):
        method = self.__get_method__('__rand__')
        if method is None:
            return super().__rand__(other)
        return method(other)

    def __ror__(self, other):
        method = self.__get_method__('__ror__')
        if method is None:
            return super().__ror__(other)
        return method(other)

    def __rxor__(self, other):
        method = self.__get_method__('__rxor__')
        if method is None:
            return super().__rxor__(other)
        return method(other)

    def __repr__(self):
        method = self.__get_method__("__repr__")
        if method is None:
            return super().__repr__()
        return method()
    
    def __unicode__(self):
        method = self.__get_method__("__unicode__")
        if method is None:
            return super().__unicode__()
        return method()
    
    def __format__(self, formatstr):
        method = self.__get_method__("__format__")
        if method is None:
            return super().__format__(formatstr)
        return method(formatstr)
    
    def __hash__(self):
        method = self.__get_method__("__hash__")
        if method is None:
            return super().__hash__()
        return method()
    
    def __nonzero__(self):
        method = self.__get_method__("__nonzero__")
        if method is None:
            return super().__nonzero__()
        return method()
    
    def __dir__(self):
        method = self.__get_method__("__dir__")
        if method is None:
            return super().__dir__()
        return method()
    
    def __sizeof__(self):
        method = self.__get_method__("__sizeof__")
        if method is None:
            return super().__sizeof__()
        return method()

    # Magic methods end #
