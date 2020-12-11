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

    def __str__(self):
        return '[PashmakClass name="' + self.__name__ + '"]'

    def __getattr__(self, attrname):
        if attrname == 'props':
            return super().__getattr__(attrname)
        try:
            return self.props[attrname]
        except KeyError:
            raise AttributeError(attrname)
