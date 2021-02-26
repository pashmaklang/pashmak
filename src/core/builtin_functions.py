#
# builtin_functions.py
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

""" Pashmak Builtin functions """

from .class_system import Class
from . import parser
from .function import Function
from . import lexer

class BuiltinFunctions:
    """ Builtin functions """
    def run_endfunc(self, op: dict):
        """ Closes the functon declaration block """
        if self.current_func:
            self.current_func.pop()
        else:
            self.raise_error('SyntaxError', 'unexpected "endfunc" when function block is not opened', op)

    def run_goto(self, op: dict):
        """ Changes program current step to a specify label """
        self.require_one_argument(op, 'goto function requires label name argument')
        arg = op['args'][0]
        try:
            label_index = self.labels[arg]
        except KeyError:
            return self.raise_error('LabelError', 'undefined label "' + str(arg) + '"', op)
        self.frames[-1]['current_step'] = label_index-1

    def run_gotoif(self, op: dict):
        """ Changes program current step to a specify label IF mem is True """
        self.require_one_argument(op, 'gotoif function requires label name argument')
        arg = op['args'][0]
        try:
            label_index = self.labels[arg]
        except KeyError:
            return self.raise_error('LabelError', 'undefined label "' + str(arg) + '"', op)
        if self.mem:
            self.frames[-1]['current_step'] = label_index-1

    def run_try(self, op: dict):
        """ Starts the try-endtry block """
        self.require_one_argument(op, 'try command requires label name argument')
        arg = op['args'][0]
        try:
            self.labels[arg]
        except KeyError:
            return self.raise_error('LabelError', 'undefined label "' + str(arg) + '"', op)
        self.try_endtry.append(arg)

    def run_endtry(self, op: dict):
        """ Closes the try-endtry block """
        if self.try_endtry:
            self.try_endtry.pop()
        else:
            self.raise_error('SyntaxError', 'unexpected "endtry" when try block is not opened', op)

    def run_namespace(self, op: dict):
        """ Starts the namespace block """
        self.require_one_argument(op, 'namespace function requires namespace argument')
        arg = op['args'][0]
        for ch in lexer.literals + '.':
            if ch in arg:
                return self.raise_error(
                    'SyntaxError', 'unexpected "' + ch + '"', op
                )
        self.namespaces_tree.append(arg)

    def run_endnamespace(self, op: dict):
        """ Closes the namespace block """
        if self.namespaces_tree:
            # delete unused variables before end namespace
            current_namespace = self.current_namespace()
            try:
                del self.all_vars()[current_namespace + '__dir__']
            except KeyError:
                pass
            try:
                del self.all_vars()[current_namespace + '__file__']
            except KeyError:
                pass
            try:
                del self.all_vars()[current_namespace + '__ismain__']
            except KeyError:
                pass

            self.namespaces_tree.pop()
        else:
            self.raise_error('SyntaxError', 'unexpected "endnamespace" when namespace block is not opened', op)

    def run_use(self, op: dict):
        """ Adds a namespace to used namespaces """
        self.require_one_argument(op, 'use command requires namespace argument')
        arg = op['args'][0]
        self.frames[-1]['used_namespaces'].append(arg)

    def run_endclass(self, op: dict):
        """ Closes the class declaration block """
        if self.current_class:
            self.current_class.pop()
        else:
            self.raise_error('SyntaxError', 'unexpected "endclass" when class block is not opened', op)

    def run_class(self, op: dict):
        """ Starts the class declaration block """
        self.require_one_argument(op, 'missing class name')
        arg = op['args_str']
        arg = arg.split('<', 1)
        parent = None
        if len(arg) > 1:
            parent = arg[1].strip()
        arg = arg[0].strip()
        for ch in lexer.literals + '.':
            if ch in arg:
                return self.raise_error(
                    'SyntaxError', 'unexpected "' + ch + '"', op
                )
        # check parent exists
        parent_real_name = None
        if parent != None:
            try:
                parent_obj = self.classes[self.current_namespace() + parent]
                parent_real_name = self.current_namespace() + parent
            except KeyError:
                parent_obj = None
                for used_namespace in self.frames[-1]['used_namespaces']:
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
        if parent_real_name != None:
            self.classes[self.current_namespace() + arg] = Class(self.current_namespace() + arg)
            self.classes[self.current_namespace() + arg].__props__['__parent__'] = parent_real_name
            self.classes[self.current_namespace() + arg].__props__['__name__'] = self.current_namespace() + arg
            self.classes[self.current_namespace() + arg].__inheritance_tree__ = [*self.classes[parent_real_name].__inheritance_tree__, self.classes[self.current_namespace() + arg].__props__['__name__']]
            self.classes[self.current_namespace() + arg].__docstring__ = self.last_docstring
            self.last_docstring = ''
        else:
            if self.current_namespace() + arg != 'Object':
                self.classes[self.current_namespace() + arg] = Class(self.current_namespace() + arg)
                self.classes[self.current_namespace() + arg].__props__['__parent__'] = 'Object'
                self.classes[self.current_namespace() + arg].__props__['__name__'] = self.current_namespace() + arg
                self.classes[self.current_namespace() + arg].__inheritance_tree__ = ['Object', self.classes[self.current_namespace() + arg].__props__['__name__']]
                self.classes[self.current_namespace() + arg].__docstring__ = self.last_docstring
                self.last_docstring = ''
            else:
                self.classes[self.current_namespace() + arg] = Class(self.current_namespace() + arg)
                self.classes[self.current_namespace() + arg].__props__['__parent__'] = None
                self.classes[self.current_namespace() + arg].__props__['__name__'] = 'Object'
                self.classes[self.current_namespace() + arg].__inheritance_tree__ = ['Object']
                self.classes[self.current_namespace() + arg].__docstring__ = self.last_docstring
                self.last_docstring = ''
        self.current_class.append(self.current_namespace() + arg)

    def run_func(self, op: dict):
        """ Starts function declaration block """
        self.require_one_argument(op, 'missing function name')
        arg = lexer.multi_char_split(op['args_str'], ' (', 1)[0]

        # sperate return type and name
        return_type = None
        tmp = arg.split('::', 1)
        if len(tmp) > 1:
            arg = tmp[1]
            return_type = tmp[0]
        else:
            arg = tmp[0]

        for ch in lexer.literals + '.':
            if ch in arg:
                return self.raise_error(
                    'SyntaxError', 'unexpected "' + ch + '"', op
                )
        # declare function
        is_method = False
        if self.current_class:
            self.current_func.append(arg)
            self.classes[self.current_class[-1]].__methods__[self.current_func[-1]] = Function(name=self.current_func[-1])
            self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].__docstring__ = self.last_docstring
            self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].return_type = return_type
            self.last_docstring = ''
            is_method = True
        else:
            self.current_func.append(self.current_namespace() + arg)
            self.functions[self.current_func[-1]] = Function(name=self.current_func[-1])
            self.functions[self.current_func[-1]].__docstring__ = self.last_docstring
            self.functions[self.current_func[-1]].return_type = return_type
            self.last_docstring = ''
        # check for argument variable
        if len(op['args_str'].split('(', 1)) > 1:
            arg_var = op['args_str'].split('(', 1)[-1].strip()
            if arg_var != '':
                if arg_var[-1] == ')':
                    arg_var = arg_var[:len(arg_var)-1]
            if arg_var != '':
                if arg_var[0] == '*':
                    arg_var = arg_var[1:]
                    self.arg_should_be_variable(arg_var, op)
                    if is_method:
                        self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].body.append(parser.parse(arg_var + ' = ^', '<system>')[0])
                    else:
                        self.functions[self.current_func[-1]].body.append(parser.parse(arg_var + ' = ^', '<system>')[0])
                else:
                    parsed_string = lexer.parse_string(arg_var)
                    arg_parts = ['']
                    for part in parsed_string:
                        if part[0] == False:
                            arg_parts = [*arg_parts, *part[1].split(',')]
                        else:
                            arg_parts[-1] += part[1]
                    if arg_parts[0] == '':
                        arg_parts.pop(0)
                    if arg_parts:
                        if arg_parts[-1] == '':
                            arg_parts.pop(-1)
                    i = 0
                    while i < len(arg_parts):
                        arg_parts[i] = arg_parts[i].strip().split('=', 1)
                        arg_parts[i][0] = arg_parts[i][0].strip()
                        if len(arg_parts[i]) > 1:
                            arg_parts[i][1] = arg_parts[i][1].strip()
                        i += 1
                    if is_method:
                        self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].args = arg_parts
                    else:
                        self.functions[self.current_func[-1]].args = arg_parts

    def run_return(self, op: dict):
        """ Returns a value in function """
        value = op['args_str'].strip()
        if value == '':
            value = None
        else:
            value = self.eval(op['args_eval'])
        self.mem = value
        if len(self.frames) > 1:
            self.frames[-1]['current_step'] = len(self.frames[-1]['commands']) * 2
        else:
            self.exit_program(value)

    def run_while(self, op: dict):
        """ The while block start """
        condition_result = self.eval(op['args_eval'])
        if condition_result:
            return
        # condition is not True, loop should be breaked
        i = self.frames[-1]['current_step']+1
        loop_depth = 0
        while i < len(self.frames[-1]['commands']):
            if self.frames[-1]['commands'][i]['command'] == 'while':
                loop_depth += 1
            elif self.frames[-1]['commands'][i]['command'] == 'endwhile':
                if loop_depth > 0:
                    loop_depth -= 1
                else:
                    self.frames[-1]['current_step'] = i
                    return
            i += 1

    def run_endwhile(self, op: dict):
        """ The While block end """
        # Back to first of loop
        i = self.frames[-1]['current_step']-1
        loop_depth = 0
        while i >= 0:
            if self.frames[-1]['commands'][i]['command'] == 'endwhile':
                loop_depth += 1
            elif self.frames[-1]['commands'][i]['command'] == 'while':
                if loop_depth > 0:
                    loop_depth -=1
                else:
                    self.frames[-1]['current_step'] = i-1
                    return
            i -= 1

    def run_break(self, op: dict):
        """ Breaks the loop """
        tmp_op = dict(op)
        op['args_str'] = 'False'
        op['args_eval'] = [['n', 'False']]
        self.run_while(op)

    def run_continue(self, op: dict):
        """ Continues the loop """
        self.run_endwhile(op)

    def run_atdoc(self, op: dict):
        """ @doc sets last docstring """
        docstr = str(self.eval(op['args_eval'])).strip()
        self.last_docstring = docstr
