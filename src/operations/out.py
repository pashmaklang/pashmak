# out.py
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
    ''' Prints a value on screen '''

    self.require_one_argument(op , 'out operation requires argument')
    arg = op['args'][0]
    self.arg_should_be_variable_or_mem(arg , op)

    out = None
    if arg == '^':
        out = self.get_mem()
    else:
        self.variable_required(arg[1:] , op)
        out = self.variables[arg[1:]]
    
    if not self.is_test:
        print(out , end='' , flush=True)
    else:
        self.output += str(out)
