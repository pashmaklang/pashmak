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

def run(self, op: dict):
    """ Declares a struct """
    self.require_one_argument(op, 'struct operation requires struct name argument')
    arg = op['args'][0]

    if '.' in arg:
        self.raise_error(
            'StructNameContainsDotError', 'name "' + arg + '" for struct contains `.` character', op
        )

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

    self.structs[self.current_namespace() + arg] = {}
    self.current_struct = self.current_namespace() + arg
