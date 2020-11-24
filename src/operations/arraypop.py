#
# arraypop.py
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

''' Pops a index from array '''

def run(self, op: dict):
    ''' Pops a index from array '''
    args = op['args']

    if len(args) <= 1:
        self.raise_error('ArgumentError', 'arraypop command gets two arguments', op)

    first_var = args[0]
    second_var = args[1]

    try:
        first_var_value = self.get_var(first_var[1:])
        if not isinstance(first_var_value, list):
            self.raise_error('TypeError', 'arraypop operation first argument should be a array', op)
    except KeyError:
        self.raise_variable_error(first_var, op)

    try:
        if second_var == '^':
            second_var_value = self.get_mem()
        else:
            second_var_value = self.get_var(second_var[1:])
    except KeyError:
        self.raise_variable_error(second_var, op)

    # pop from array
    self.all_vars()[first_var[1:]].pop(second_var_value)
