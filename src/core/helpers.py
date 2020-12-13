#
# helpers.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
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

""" Partial of program object functions """

import os
from sys import exit
from core import commands, modules
import syntax_parser as parser

class Helpers(commands.Commands):
    """ Partial of program object functions """

    def raise_variable_error(self, varname: str, op: dict):
        """ Raise variable not found error """
        return self.raise_error('VariableError', 'undefined variable "' + str(varname) + '"', op)

    def raise_syntax_error(self, string: str, op: dict):
        """ Raises syntax error """
        return self.raise_error('SyntaxError', 'unexpected "' + string + '"', op)

    def arg_should_be_variable(self, arg: str, op: dict):
        """ Checks argument syntax is variable name """
        if arg[0] != '$':
            self.raise_syntax_error(arg[0], op)

    def arg_should_be_variable_or_mem(self, arg: str, op: dict):
        """ Checks argument syntax is variable name or mem """
        if arg[0] != '$' and arg != '^':
            self.raise_syntax_error(arg[0], op)

    def variable_exists(self, varname: str) -> bool:
        """ Checks a variable is exists or not """
        try:
            self.get_var(varname)
            return True
        except KeyError:
            return False

    def variable_required(self, varname: str, op: dict):
        """ Raises variable error if variable not exists """
        if not self.variable_exists(varname):
            self.raise_variable_error(varname, op)

    def require_one_argument(self, op: dict, error_message: str):
        """ Checks argument syntax to be variable name """
        if len(op['args']) <= 0:
            self.raise_error('ArgumentError', error_message, op)

    def get_var(self, varname: str):
        """ Gets a variable name and returns value of that """
        try:
            return self.all_vars()[self.current_namespace() + varname]
        except KeyError:
            for used_namespace in self.used_namespaces:
                try:
                    return self.all_vars()[used_namespace + '.' + varname]
                except KeyError:
                    pass
            return self.all_vars()[varname]

    def set_var(self, varname: str, value):
        """ Gets name of a variable and sets value on that """
        if '&' in varname:
            do_raise_error = False
            try:
                if self.all_vars()[self.current_namespace() + varname] != None:
                    op = self.operations[self.current_step]
                    do_raise_error = True
            except:
                pass
            if do_raise_error:
                self.raise_error('ConstError', '"' + varname + '" is a const and you cannot change that value', op)
        self.all_vars()[self.current_namespace() + varname] = value

    def all_vars(self):
        """ Returns list of all of variables """
        if not self.states:
            return self.variables

        return self.states[-1]['vars']

    def multi_char_split(self, string, seprators):
        """ Splits string by multi seprators """
        result = ['']
        for char in string:
            if char in seprators:
                result.append('')
            else:
                result[-1] += char
        return result

    def print(self, obj):
        """ Prints a object """
        if not self.is_test:
            print(obj, end='', flush=True)
        else:
            self.output += str(obj)

    def exit_program(self, exit_code):
        """ Exits the program """
        if not self.is_test:
            exit(exit_code)
        else:
            self.current_step = len(self.operations) * 2
            self.exit_code = exit_code

    def pashmak_eval(self, code):
        """ Runs the pashmak code from string """
        # run the code
        code_operations = parser.parse(code, filepath='<eval>')
        for code_op in list(reversed(code_operations)):
            self.operations.insert(self.current_step+1, code_op)
            self.update_section_indexes(self.current_step+1)

    def import_script(self, paths):
        """ Imports scripts/modules """
        op = self.operations[self.current_step]

        if type(paths) == str:
            paths = [paths]
        elif type(paths) != list and type(paths) != tuple:
            self.raise_error('ArgumentError', 'invalid argument type', op)

        for path in paths:
            code_location = path
            if path[0] == '@':
                code_location = path
                module_name = path[1:]
                try:
                    namespaces_prefix = ''
                    for part in self.namespaces_tree:
                        namespaces_prefix += part + '.'
                    namespaces_prefix += '@'
                    if not namespaces_prefix + module_name in self.included_modules:
                        content = modules.modules[module_name]
                        # add this module to imported modules
                        self.included_modules.append(namespaces_prefix + module_name)
                    else:
                        return
                except KeyError:
                    self.raise_error('ModuleError', 'undefined module "' + module_name + '"', op)
            else:
                if path[0] != '/':
                    path = os.path.dirname(os.path.abspath(self.main_filename)) + '/' + path
                try:
                    content = open(path, 'r').read()
                    content = '$__file__ = "' + path.replace('\\', '\\\\') + '";\n$__dir__ = "' + os.path.dirname(path).replace('\\', '\\\\') + '"\n' + content
                    content += '\n$__file__ = "' + self.get_var('__file__').replace('\\', '\\\\') + '"'
                    content += '\n$__dir__ = "' + self.get_var('__dir__').replace('\\', '\\\\') + '"'
                    code_location = path
                except FileNotFoundError as ex:
                    self.raise_error('FileError', str(ex), op)
                except PermissionError as ex:
                    self.raise_error('FileError', str(ex), op)

            operations = parser.parse(content, filepath=code_location)
            self.exec_func(operations, False)