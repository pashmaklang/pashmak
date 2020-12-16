#
# builtin_functions.py
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

""" Pashmak Builtin functions """

from builtins_func import func as op_func
from builtins_func import classop as op_class
from builtins_func import new as op_new

class BuiltinFunctions:
    """ Builtin functions """
    def run_free(self, op: dict):
        """ Deletes variables """
        args = op['args']
        for arg in args:
            self.arg_should_be_variable_or_mem(arg, op)
            if arg == '^':
                self.mem = None
            else:
                try:
                    del self.all_vars()[arg[1:]]
                except KeyError:
                    pass

    def run_read(self, op: dict):
        """ Reads input from stdin """
        if not self.is_test:
            readed_data = input()
        else:
            readed_data = self.read_data[0]
            self.read_data.pop(0)
        self.mem = readed_data

    def run_endfunc(self, op: dict):
        """ Closes the functon declaration block """
        try:
            del self.current_func
        except AttributeError:
            pass

    def run_goto(self, op: dict):
        """ Changes program current step to a specify section """
        self.require_one_argument(op, 'goto function requires section name argument')
        arg = op['args'][0]
        try:
            section_index = self.sections[arg]
        except KeyError:
            return self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)
        self.states[-1]['current_step'] = section_index-1

    def run_gotoif(self, op: dict):
        """ Changes program current step to a specify section IF mem is True """
        self.require_one_argument(op, 'gotoif function requires section name argument')
        arg = op['args'][0]
        try:
            section_index = self.sections[arg]
        except KeyError:
            return self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)
        if self.mem:
            self.states[-1]['current_step'] = section_index-1

    def run_isset(self, op: dict):
        """ Checks variable(s) exists and puts result to mem """
        args = op['args']
        for arg in args:
            self.arg_should_be_variable(arg, op)
            if not self.variable_exists(arg[1:]):
                self.mem = False
                return
        self.mem = True

    def run_try(self, op: dict):
        """ Starts the try-endtry block """
        self.require_one_argument(op, 'try command requires section name argument')
        arg = op['args'][0]
        try:
            self.sections[arg]
        except KeyError:
            return self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)
        self.try_endtry.append(arg)

    def run_endtry(self, op: dict):
        """ Closes the try-endtry block """
        if self.try_endtry:
            self.try_endtry.pop()

    def run_namespace(self, op: dict):
        """ Starts the namespace block """
        self.require_one_argument(op, 'namespace function requires namespace argument')
        arg = op['args'][0]
        if '.' in arg:
            return self.raise_error(
                'NamespaceContainsDotError', 'name "' + arg + '" for namespace contains `.` character', op
            )
        self.namespaces_tree.append(arg)

    def run_endnamespace(self, op: dict):
        """ Closes the namespace block """
        if self.namespaces_tree:
            self.namespaces_tree.pop()

    def run_use(self, op: dict):
        """ Adds a namespace to used namespaces """
        self.require_one_argument(op, 'use command requires namespace argument')
        arg = op['args'][0]
        self.used_namespaces.append(arg)

    def run_endclass(self, op: dict):
        """ Closes the class declaration block """
        try:
            del self.current_class
        except AttributeError:
            pass

    def run_class(self, op: dict):
        """ run class """
        op_class.run(self, op)

    def run_new(self, op: dict):
        """ run new """
        op_new.run(self, op)

    def run_func(self, op: dict):
        """ run func """
        op_func.run(self, op)
