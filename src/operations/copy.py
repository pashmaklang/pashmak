# copy.py
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

def run(self , op):
    args = op['args_str'].strip().split(' ')

    if len(args) <= 0:
        self.raise_error('ArgumentError' , 'copy command gets two arguments' , op)
        
    if len(args[0]) == 0:
        self.raise_error('SyntaxError' , 'one or more arguments are empty' , op)

    first_var = args[0]

    if len(args) == 1:
        mem = self.get_mem()
        try:
            self.variables[first_var[1:]] = mem
            return
        except:
            self.raise_variable_error(first_var , op)

    if len(args[1]) == 0:
        self.raise_error('SyntaxError' , 'one or more arguments are empty' , op)

    second_var = args[1]

    try:
        if first_var == '^':
            first_var_value = self.get_mem()
        else:
            first_var_value = self.variables[first_var[1:]]
    except:
        self.raise_variable_error(first_var , op)

    try:
        if second_var == '^':
            self.mem = first_var_value
        else:
            self.variables[second_var[1:]] = first_var_value
    except:
        self.raise_variable_error(second_var , op)
