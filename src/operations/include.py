#
# include.py
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

''' Includes another script file to program '''

import os
from syntax import parser
from core import modules

def run(self, op: dict):
    ''' Includes another script file to program '''

    self.require_one_argument(op, 'include operation requires argument')
    arg = op['args'][0]
    self.arg_should_be_variable_or_mem(arg, op)

    content = ''

    if arg == '^':
        path = self.get_mem()
    else:
        self.variable_required(arg[1:], op)
        path = self.get_var(arg[1:])

    if not path:
        return

    if path[0] == '@':
        module_name = path[1:]
        try:
            if not module_name in self.included_modules:
                content = modules.modules[module_name]
                # add this module to imported modules
                self.included_modules.append(module_name)
            else:
                return
        except KeyError:
            self.raise_error('ModuleError', 'undefined module "' + module_name + '"', op)
    else:
        if path[0] != '/':
            path = os.path.dirname(os.path.abspath(self.main_filename)) + '/' + path
        try:
            content = open(path, 'r').read()
            content = '$__file__ = "' + path + '";\n$__dir__ = "' + os.path.dirname(path) + '"\n' + content
        except FileNotFoundError as ex:
            self.raise_error('FileError', str(ex), op)
        except PermissionError as ex:
            self.raise_error('FileError', str(ex), op)

    operations = parser.parse(content)
    self.exec_func(operations, False)
