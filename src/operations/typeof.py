#
# typeof.py
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

''' Puts type of a variable in mem '''

def run(self, op: dict):
    ''' Puts type of a variable in mem '''

    args = op['args']
    for arg in args:
        self.arg_should_be_variable(arg, op)
        self.variable_required(arg[1:], op)
        var = self.get_var(arg[1:])
        self.mem = type(var)
