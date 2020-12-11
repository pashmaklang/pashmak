#
# new.py
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

""" Creates a new instance from a class """

import copy
from core.class_system import Class

def run(self, op: dict):
    """ Creates a new instance from a class """

    self.require_one_argument(op, 'new operation requires class name argument')
    arg = op['args'][0]

    # check class exists
    class_real_name = None
    try:
        aclass = self.classes[self.current_namespace() + arg]
        class_real_name = self.current_namespace() + arg
    except KeyError:
        aclass = None
        for used_namespace in self.used_namespaces:
            try:
                aclass = self.classes[used_namespace + '.' + arg]
                class_real_name = used_namespace + '.' + arg
            except KeyError:
                pass
        if not aclass:
            try:
                aclass = self.classes[arg]
                class_real_name = arg
            except KeyError:
                self.raise_error('ClassError', 'undefined class "' + arg + '"', op)
                return

    class_copy = copy.deepcopy(aclass)
    self.mem = class_copy
