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

""" Declares a struct """

import copy
from core.struct import Struct

def run(self, op: dict):
    """ Declares a struct """
    self.require_one_argument(op, 'struct operation requires struct name argument')
    arg = op['args_str']
    arg = arg.split('<', 1)
    parent = None
    if len(arg) > 1:
        parent = arg[1].strip()
    arg = arg[0].strip()

    if '.' in arg:
        self.raise_error(
            'StructNameContainsDotError', 'name "' + arg + '" for struct contains `.` character', op
        )

    # check parent exists
    parent_real_name = None
    if parent != None:
        try:
            parent_obj = self.structs[self.current_namespace() + parent]
            parent_real_name = self.current_namespace() + parent
        except KeyError:
            parent_obj = None
            for used_namespace in self.used_namespaces:
                try:
                    parent_obj = self.structs[used_namespace + '.' + parent]
                    parent_real_name = used_namespace + '.' + parent
                except KeyError:
                    pass
            if not parent_obj:
                try:
                    parent_obj = self.structs[parent]
                    parent_real_name = parent
                except KeyError:
                    self.raise_error('StructError', 'undefined struct "' + parent + '"', op)
                    return

    # check struct already declared
    try:
        self.structs[self.current_namespace() + arg]
        self.raise_error(
            'StructError',
            'struct "' + self.current_namespace() + arg + '" already declared',
            op
        )
    except KeyError:
        pass

    if parent_real_name != None:
        self.structs[self.current_namespace() + arg] = copy.deepcopy(self.structs[parent_real_name])
        self.structs[self.current_namespace() + arg].props['__parent__'] = parent_real_name
        self.structs[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
    else:
        if self.current_namespace() + arg != 'Object':
            self.structs[self.current_namespace() + arg] = copy.deepcopy(self.structs['Object'])
            self.structs[self.current_namespace() + arg].props['__parent__'] = 'Object'
            self.structs[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
        else:
            self.structs[self.current_namespace() + arg] = copy.deepcopy(Struct(self.current_namespace() + arg, {}))
            self.structs[self.current_namespace() + arg].props['__parent__'] = None
            self.structs[self.current_namespace() + arg].props['__name__'] = 'Object'
    self.current_struct = self.current_namespace() + arg
