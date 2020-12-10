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

''' Partial of program object functions '''

from core import commands

class Helpers(commands.Commands):
    ''' Partial of program object functions '''

    def raise_variable_error(self, varname: str, op: dict):
        ''' Raise variable not found error '''
        return self.raise_error('VariableError', 'undefined variable "' + str(varname) + '"', op)

    def raise_syntax_error(self, string: str, op: dict):
        ''' Raises syntax error '''
        return self.raise_error('SyntaxError', 'unexpected "' + string + '"', op)

    def arg_should_be_variable(self, arg: str, op: dict):
        ''' Checks argument syntax is variable name '''
        if arg[0] != '$':
            self.raise_syntax_error(arg[0], op)

    def arg_should_be_variable_or_mem(self, arg: str, op: dict):
        ''' Checks argument syntax is variable name or mem '''
        if arg[0] != '$' and arg != '^':
            self.raise_syntax_error(arg[0], op)

    def variable_exists(self, varname: str) -> bool:
        ''' Checks a variable is exists or not '''
        try:
            self.get_var(varname)
            return True
        except KeyError:
            return False

    def variable_required(self, varname: str, op: dict):
        ''' Raises variable error if variable not exists '''
        if not self.variable_exists(varname):
            self.raise_variable_error(varname, op)

    def require_one_argument(self, op: dict, error_message: str):
        ''' Checks argument syntax to be variable name '''
        if len(op['args']) <= 0:
            self.raise_error('ArgumentError', error_message, op)

    def get_var(self, varname: str):
        ''' Gets a variable name and returns value of that '''
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
        ''' Gets name of a variable and sets value on that '''
        if '&' in varname:
            try:
                self.all_vars()[self.current_namespace() + varname]
                op = self.operations[self.current_step]
                self.raise_error('ConstError', '"' + varname + '" is a const and you cannot change that value', op)
            except:
                pass
        self.all_vars()[self.current_namespace() + varname] = value

    def all_vars(self):
        ''' Returns list of all of variables '''
        if not self.states:
            return self.variables

        return self.states[-1]['vars']
