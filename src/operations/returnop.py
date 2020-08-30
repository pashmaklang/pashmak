# returnop.py
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

import sys

def run(self , op):
    arg = op['args_str'].strip().split(' ')[0].strip()

    exit_code = 0
    tmp = None

    if arg != '':
        if arg[0] == '%':
            try:
                tmp = self.variables[arg[1:]]

                try:
                    tmp = int(tmp)
                    exit_code = tmp
                except:
                    self.raise_error('TypeError' , 'return command gets integer value' , op)
            except:
                self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
        else:
            try:
                exit_code = int(arg)
            except:
                self.raise_error('TypeError' , 'return command gets integer value' , op)

    sys.exit(exit_code)
