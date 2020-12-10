#
# struct.py
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

""" Structs """

class StructConstError(Exception):
    pass

class StructProps(dict):
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
                    raise StructConstError('property "' + attrname + '" is const and cannot be changed')
        except KeyError:
            pass
        self[attrname] = value

class Struct:
    """ Struct model """
    def __init__(self, name: str, props: dict):
        self.props = StructProps(props)
        self.name = name

    def __str__(self):
        return '[PashmakStruct name="' + self.name + '"]'
