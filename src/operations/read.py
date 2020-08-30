# read.py
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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################

def run(self , op):
    arg = op['args_str'].split(' ')[0]

    if len(arg) <= 0:
        self.raise_error('SyntaxError' , 'read command required variable argument' , op)

    out = None
    if arg == '^':
        pass
    else:
        if arg[0] == '%':
            try:
                tmp = self.variables[arg[1:]]
                del tmp
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        else:
            self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
        
    readed_data = input()

    if out == '^':
        self.mem = readed_data
    else:
        self.variables[arg[1:]] = readed_data
