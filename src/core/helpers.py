#
# helpers.py
#
# The Pashmak Project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
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

"""Partial of program object methods

The following methods in `Helpers` class are used in `program.Program`.
Actually, `program.Program` extends this class.

This is only for that to seprate this methods into other file to don't make `progra.Program` big.

Also this class extends `builtin_functions.BuiltinFunctions`.
Then, all of methods in `builtin_functions.BuiltinFunctions` and `helpers.Helpers`,
will be accessible in `program.Program`.
"""
import sys
from sys import exit
from . import builtin_functions, parser

class VariableError(Exception):
    pass

class Helpers(builtin_functions.BuiltinFunctions):
    """ Partial of program object functions """

    def raise_variable_error(self, varname: str, op=None):
        """ Raise variable not found error """
        return self.raise_error('VariableError', 'undefined variable "' + str(varname) + '"', op)

    def raise_syntax_error(self, string: str, op=None):
        """ Raises syntax error """
        return self.raise_error('SyntaxError', 'unexpected "' + string + '"', op)

    def arg_should_be_variable(self, arg: str, op=None):
        """ Checks argument syntax is variable name """
        if arg[0] != '$':
            self.raise_syntax_error(arg[0], op)

    def arg_should_be_variable_or_mem(self, arg: str, op=None):
        """ Checks argument syntax is variable name or mem """
        if arg[0] != '$' and arg != '^':
            self.raise_syntax_error(arg[0], op)

    def variable_exists(self, varname: str) -> bool:
        """ Checks a variable is exists or not """
        try:
            self.all_vars()[self.current_namespace() + varname]
            return True
        except KeyError:
            for used_namespace in self.frames[-1]['used_namespaces']:
                try:
                    self.all_vars()[used_namespace + '.' + varname]
                    return True
                except KeyError:
                    pass
            try:
                self.all_vars()[varname]
                return True
            except KeyError:
                return False

    def variable_required(self, varname: str):
        """ Raises variable error if variable not exists """
        self.get_var(varname)

    def require_one_argument(self, op: dict, error_message: str):
        """ Checks argument syntax to be variable name """
        if len(op['args']) <= 0:
            self.raise_error('ArgumentError', error_message, op)

    def get_var(self, varname: str, do_not_raise_error=False):
        """ Gets a variable name and returns value of that """
        for frame in list(reversed(self.frames)):
            try:
                return frame['vars'][self.current_namespace() + varname]
            except KeyError:
                for used_namespace in self.frames[-1]['used_namespaces']:
                    try:
                        return frame['vars'][used_namespace + '.' + varname]
                    except KeyError:
                        pass
                try:
                    return frame['vars'][varname]
                except KeyError:
                    do_raise_error = False
                    try:
                        op = self.frames[-1]['commands'][self.frames[-1]['current_step']]
                        do_raise_error = True
                    except:
                        pass
        if do_raise_error and do_not_raise_error == False:
            raise VariableError('undefined variable "' + varname + '"')
            return

    def set_var(self, varname: str, value):
        """ Gets name of a variable and sets value on that """
        if '&' in varname:
            do_raise_error = False
            try:
                if self.all_vars()[self.current_namespace() + varname] != None:
                    op = self.frames[-1]['commands'][self.frames[-1]['current_step']]
                    do_raise_error = True
            except:
                pass
            if do_raise_error:
                self.raise_error('ConstError', '"' + varname + '" is a const and you cannot change that value', op)
                return
        self.all_vars()[self.current_namespace() + varname] = value

    def all_vars(self):
        """ Returns list of all of variables """
        return self.frames[-1]['vars']

    def print(self, obj, file=sys.stdout):
        """ Prints a object """
        if type(obj) == tuple and len(obj) == 1:
            obj_str = str(obj[0])
        else:
            obj_str = str(obj)
        if self.out_started:
            self.out_content += obj_str
            return
        if not self.is_test:
            print(obj_str, end='', flush=True, file=file)
        else:
            self.output += obj_str

    def io_read(self):
        """ Reads input from stdin """
        if not self.is_test:
            readed_data = input()
        else:
            readed_data = self.read_data[0]
            self.read_data.pop(0)
        self.mem = readed_data

    def exit_program(self, exit_code):
        """ Exits the program """
        if not self.is_test:
            exit(exit_code)
        else:
            i = len(self.frames)-1
            while i > 0:
                self.frames.pop()
                i -= 1
            self.frames[-1]['current_step'] = len(self.frames[-1]['commands']) * 2
            self.exit_code = exit_code

    def pashmak_eval(self, code):
        """ Runs the pashmak code from string """
        # run the code
        code_commands = parser.parse(code, filepath='<eval>')
        self.exec_func(code_commands, False)

    def current_namespace(self):
        """ Returns current namespace """
        namespace_prefix = ''
        for ns in self.namespaces_tree:
            namespace_prefix += ns + '.'
        return namespace_prefix

    def signal_handler(self, signal_code, frame):
        """ Raise error when signal exception raised """
        self.raise_error('Signal', str(signal_code), self.frames[-1]['commands'][self.frames[-1]['current_step']])
