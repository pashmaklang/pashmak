#
# classop.py
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

""" Declares a class """

import copy
from core.class_system import Class

def run(self, op: dict):
    """ Declares a class """
    self.require_one_argument(op, 'class operation requires class name argument')
    arg = op['args_str']
    arg = arg.split('<', 1)
    parent = None
    if len(arg) > 1:
        parent = arg[1].strip()
    arg = arg[0].strip()

    if '.' in arg:
        self.raise_error(
            'ClassNameContainsDotError', 'name "' + arg + '" for class contains `.` character', op
        )

    # check parent exists
    parent_real_name = None
    if parent != None:
        try:
            parent_obj = self.classes[self.current_namespace() + parent]
            parent_real_name = self.current_namespace() + parent
        except KeyError:
            parent_obj = None
            for used_namespace in self.used_namespaces:
                try:
                    parent_obj = self.classes[used_namespace + '.' + parent]
                    parent_real_name = used_namespace + '.' + parent
                except KeyError:
                    pass
            if not parent_obj:
                try:
                    parent_obj = self.classes[parent]
                    parent_real_name = parent
                except KeyError:
                    self.raise_error('ClassError', 'undefined class "' + parent + '"', op)
                    return

    # check class already declared
    try:
        self.classes[self.current_namespace() + arg]
        self.raise_error(
            'ClassError',
            'class "' + self.current_namespace() + arg + '" already declared',
            op
        )
    except KeyError:
        pass

    if parent_real_name != None:
        self.classes[self.current_namespace() + arg] = copy.deepcopy(self.classes[parent_real_name])
        self.classes[self.current_namespace() + arg].props['__parent__'] = parent_real_name
        self.classes[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
    else:
        if self.current_namespace() + arg != 'Object':
            self.classes[self.current_namespace() + arg] = copy.deepcopy(self.classes['Object'])
            self.classes[self.current_namespace() + arg].props['__parent__'] = 'Object'
            self.classes[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
        else:
            self.classes[self.current_namespace() + arg] = copy.deepcopy(Class(self.current_namespace() + arg, {}))
            self.classes[self.current_namespace() + arg].props['__parent__'] = None
            self.classes[self.current_namespace() + arg].props['__name__'] = 'Object'
    self.current_class = self.current_namespace() + arg
