#
# eval.py
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

''' Runs pashmak code from string '''

from syntax import parser

def run(self, op: dict):
    ''' Runs pashmak code from string '''

    self.require_one_argument(op, 'eval operation requires argument')
    arg = op['args'][0]
    self.arg_should_be_variable_or_mem(arg, op)

    if arg == '^':
        code = self.get_mem()
    else:
        self.variable_required(arg[1:], op)
        code = self.get_var(arg[1:])

    # run the code
    code_operations = parser.parse(code, filepath='<eval>')
    for code_op in list(reversed(code_operations)):
        self.operations.insert(self.current_step+1, code_op)
        self.update_section_indexes(self.current_step+1)
