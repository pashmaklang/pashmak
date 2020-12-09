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


""" Creates a new instance from a struct """

def run(self, op: dict):
    """ Creates a new instance from a struct """

    self.require_one_argument(op, 'new operation requires struct name argument')
    arg = op['args'][0]

    # check struct exists
    struct_real_name = None
    try:
        struct = self.structs[self.current_namespace() + arg]
        struct_real_name = self.current_namespace() + arg
    except KeyError:
        struct = None
        for used_namespace in self.used_namespaces:
            try:
                struct = self.structs[used_namespace + '.' + arg]
                struct_real_name = used_namespace + '.' + arg
            except KeyError:
                pass
        if not struct:
            try:
                struct = self.structs[arg]
                struct_real_name = arg
            except KeyError:
                self.raise_error('StructError', 'undefined struct "' + arg + '"', op)
                return

    self.mem = {'struct': struct_real_name, 'props': dict(struct)}
