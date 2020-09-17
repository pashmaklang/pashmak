# typeof.py
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
    ''' Puts type of a variable in mem '''

    args = op['args']
    for arg in args:
        self.arg_should_be_variable(arg , op)
        self.variable_required(arg[1:] , op)
        var = self.variables[arg[1:]]
        var_type = str(type(var))
        var_type = var_type[8:]
        var_type = var_type[:len(var_type)-2]
        self.mem = var_type
