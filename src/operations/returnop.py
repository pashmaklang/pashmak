#
# returnop.py
#
# The Pashmak Project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
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

''' Exits program with exit code '''

import sys

def run(self, op: dict):
    ''' Exits program with exit code '''

    args = op['args']

    exit_code = 0

    if args:
        arg = args[0]

        if arg[0] == '$':
            self.variable_required(arg[1:], op)
            try:
                exit_code = int(self.get_var(arg[1:]))
            except:
                self.raise_error('TypeError', 'return operation gets integer value', op)
        elif arg == '^':
            try:
                exit_code = int(self.get_mem())
            except:
                self.raise_error('TypeError', 'return operation gets integer value', op)
        else:
            try:
                exit_code = int(arg)
            except:
                self.raise_error('TypeError', 'return command gets integer value', op)

    if not self.is_test:
        sys.exit(exit_code)
    else:
        self.current_step = len(self.operations) * 2
        self.exit_code = exit_code
