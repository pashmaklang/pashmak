# call.py
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
    ''' Calls a alias '''

    self.require_one_argument(op , 'call operation requires alias name argument')
    arg = op['args'][0]

    if arg[0] == '$':
        self.variable_required(arg[1:] , op)
        arg = self.variables[arg[1:]]
    elif arg == '^':
        arg = self.get_mem()

    try:
        alias_body = self.aliases[arg]
    except:
        self.raise_error('AliasError' , 'undefined alias "' + arg + '"' , op)

    i = int(self.current_step)
    for alias_op in alias_body:
        alias_op_parsed = self.set_operation_index(alias_op)
        if alias_op_parsed['command'] == 'section':
            section_name = alias_op_parsed['args_str'].strip().split(' ')[0].strip()
            self.sections[section_name] = i+1
        else:
            self.operations.insert(i+1 , alias_op)
            i += 1
