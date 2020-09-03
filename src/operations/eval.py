# eval.py
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

from syntax import parser

def run(self , op):
    arg = self.one_arg_required('eval command gets a parameter' , op)

    if arg == '^':
        code = self.get_mem()
    else:
        if arg[0] == '%':
            try:
                code = self.variables[arg[1:]]
            except:
                self.raise_variable_error(arg , op)
        else:
            self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)

    # run the code
    code_operations = parser.parse(code)
    for code_op in list(reversed(code_operations)):
        self.operations.insert(self.current_step+1 , code_op)
