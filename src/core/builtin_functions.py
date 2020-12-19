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

from core.class_system import Class
from core import parser
import copy
import random

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
        """ Starts the class declaration block """
        self.require_one_argument(op, 'missing class name')
        arg = op['args_str']
        arg = arg.split('<', 1)
        parent = None
        if len(arg) > 1:
            parent = arg[1].strip()
        arg = arg[0].strip()

        if '.' in arg:
            return self.raise_error(
                'ClassNameContainsDotError', 'name "' + arg + '" for class contains `.` character', op
            )

        # check parent exists
        parent_real_name = None
        if parent != None:
            try:
                parent_obj = self.classes[self.current_namespace() + parent]
                parent_real_name = self.current_namespace() + parent
            except KeyError:
                parent_obj = None
                for used_namespace in self.used_namespaces:
                    try:
                        parent_obj = self.classes[used_namespace + '.' + parent]
                        parent_real_name = used_namespace + '.' + parent
                    except KeyError:
                        pass
                if not parent_obj:
                    try:
                        parent_obj = self.classes[parent]
                        parent_real_name = parent
                    except KeyError:
                        return self.raise_error('ClassError', 'undefined class "' + parent + '"', op)

        # check class already declared
        try:
            self.classes[self.current_namespace() + arg]
            return self.raise_error(
                'ClassError',
                'class "' + self.current_namespace() + arg + '" already declared',
                op
            )
        except KeyError:
            pass

        if parent_real_name != None:
            self.classes[self.current_namespace() + arg] = copy.deepcopy(self.classes[parent_real_name])
            self.classes[self.current_namespace() + arg].props['__parent__'] = parent_real_name
            self.classes[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
        else:
            if self.current_namespace() + arg != 'Object':
                self.classes[self.current_namespace() + arg] = copy.deepcopy(self.classes['Object'])
                self.classes[self.current_namespace() + arg].props['__parent__'] = 'Object'
                self.classes[self.current_namespace() + arg].props['__name__'] = self.current_namespace() + arg
            else:
                self.classes[self.current_namespace() + arg] = copy.deepcopy(Class(self.current_namespace() + arg, {}))
                self.classes[self.current_namespace() + arg].props['__parent__'] = None
                self.classes[self.current_namespace() + arg].props['__name__'] = 'Object'
        self.current_class = self.current_namespace() + arg


    def run_new(self, op: dict):
        """ Creates a object from class """
        self.require_one_argument(op, 'missing class name')
        arg = op['args'][0]
        # check class exists
        class_real_name = None
        try:
            aclass = self.classes[self.current_namespace() + arg]
            class_real_name = self.current_namespace() + arg
        except KeyError:
            aclass = None
            for used_namespace in self.used_namespaces:
                try:
                    aclass = self.classes[used_namespace + '.' + arg]
                    class_real_name = used_namespace + '.' + arg
                except KeyError:
                    pass
            if not aclass:
                try:
                    aclass = self.classes[arg]
                    class_real_name = arg
                except KeyError:
                    return self.raise_error('ClassError', 'undefined class "' + arg + '"', op)
        class_copy = copy.deepcopy(aclass)
        init_args = op['args_str'].split(' ', 1)
        if len(init_args) > 1:
            init_args = init_args[-1].strip()
        else:
            init_args = ''
        if init_args == '':
            init_args = 'None'
        # run the constructor
        tmp_variable = 'the_temp_variable_for_class_init_' + str(random.random()).replace('.', '')
        while self.variable_exists(tmp_variable):
            tmp_variable = tmp_variable + str(random.random()).replace('.', '')
        class_copy.__prog__ = self
        self.mem = class_copy
        code_commands = """
        $""" + tmp_variable + """ = ^
        $""" + self.current_namespace() + tmp_variable + """@__init__ """ + init_args + """
        mem $""" + self.current_namespace() + tmp_variable + """
        free $""" + self.current_namespace() + tmp_variable + """
        """
        tmp_is_in_class = False
        try:
            tmp_is_in_class = copy.deepcopy(self.current_class)
            del self.current_class
        except:
            pass
        self.exec_func(parser.parse(code_commands), False)
        if tmp_is_in_class:
            self.current_class = tmp_is_in_class

    def run_func(self, op: dict):
        """ Starts function declaration block """
        self.require_one_argument(op, 'missing function name')
        arg = self.multi_char_split(op['args_str'], ' (', 1)[0]
        if '.' in arg:
            return self.raise_error(
                'FunctionNameContainsDotError', 'name "' + arg + '" for function contains `.` character', op
            )
        # check function already declared
        try:
            self.functions[self.current_namespace() + arg]
            return self.raise_error(
                'FunctionError',
                'function "' + self.current_namespace() + arg + '" already declared',
                op
            )
        except KeyError:
            pass
        # declare function
        is_method = False
        try:
            self.current_class
            self.current_func = arg
            self.classes[self.current_class].methods[self.current_func] = []
            is_method = True
        except:
            self.current_func = self.current_namespace() + arg
            self.functions[self.current_func] = []
        # check for argument variable
        if len(self.multi_char_split(op['args_str'], ' (', 1)) > 1:
            arg_var = self.multi_char_split(op['args_str'], ' (', 1)[1].strip(')').strip('(').strip()
            self.arg_should_be_variable(arg_var, op)
            if is_method:
                self.classes[self.current_class].methods[self.current_func].append(parser.parse(arg_var + ' = ^', '<system>')[0])
            else:
                self.functions[self.current_func].append(parser.parse(arg_var + ' = ^', '<system>')[0])

    def run_return(self, op: dict):
        """ Returns a value in function """
        value = op['args_str'].strip()
        if value == '':
            value = None
        else:
            value = self.eval(value)

        self.mem = value
        if len(self.states) > 1:
            self.states[-1]['current_step'] = len(self.states[-1]['commands']) * 2
        else:
            self.exit_program(value)