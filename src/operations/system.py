# system.py
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

import os

def run(self , op):
    args = op['args_str'].strip().split(' ')

    if len(args) <= 0:
        self.raise_error('SyntaxError' , 'system command gets a parameter' , op)

    arg = args[0]

    if arg != '':
        if arg == '^':
            cmd = self.get_mem()
        else:
            if arg[0] == '%':
                try:
                    cmd = self.variables[arg[1:]]
                except:
                    self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
            
        self.mem = os.system(cmd)
    else:
        self.raise_error('SyntaxError' , 'system command gets a parameter' , op)
