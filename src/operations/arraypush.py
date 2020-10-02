#
# arraypush.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

def run(self , op: dict):
    ''' Pushes new item to array '''
    args = op['args']

    if len(args) <= 1:
        self.raise_error('ArgumentError' , 'arraypush command gets two arguments' , op)

    first_var = args[0]
    second_var = args[1]

    try:
        first_var_value = self.variables[first_var[1:]]
        if type(first_var_value) != list:
            self.raise_error('TypeError' , 'arraypush command first argument should be a array' , op)
    except:
        self.raise_variable_error(first_var , op)

    try:
        if second_var == '^':
            second_var_value = self.get_mem()
        else:
            second_var_value = self.variables[second_var[1:]]
    except:
        self.raise_variable_error(second_var , op)

    # push to array
    self.variables[first_var[1:]].append(second_var_value)
