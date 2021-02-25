#
# function.py
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

""" Pashmak function system """

import copy
from . import parser

class Function:
    """ the pashmak function object """
    BUILTIN_WITHOUT_FRAME_ISOLATION_FUNCTIONS = ['import', 'import_once', 'import_run', 'import_run_once', 'mem', 'python', 'rmem', 'eval', 'debug']
    def __init__(self, name):
        self.name = name
        self.body = []
        self.args = []
        self.return_type = None

    def __validate_argument_type__(self, value, arg_type_full: str) -> bool:
        """ Gets a object and type defination string and validates object type """
        from .current_prog import current_prog
        # split the arg_type_full string by `|`
        bracket_counter = 0
        arg_parts = ['']
        for ch in arg_type_full:
            if ch == '|' and bracket_counter <= 0:
                arg_parts.append('')
            else:
                arg_parts[-1] += ch
                if ch == '[': bracket_counter += 1
                elif ch == ']': bracket_counter -= 1
        arg_parts = [item for item in arg_parts if item != '']
        for arg_type in arg_parts:
            item_parts = arg_type.split('[', 1)
            arg_type = item_parts[0]
            if len(item_parts) > 1:
                if item_parts[1][-1] == ']':
                    item_parts[1] = item_parts[1][:-1]
            the_class = current_prog.get_class_real_name(arg_type)
            if the_class != False:
                if type(value).__name__ != 'ClassObject':
                    return False
                res = value.isinstanceof(the_class)
                if res == True:
                    return True
                else:
                    return None
            arg_type_obj = current_prog.eval(arg_type)
            result =  type(value) == arg_type_obj
            if result:
                if len(item_parts) > 1:
                    # check the items in the list
                    for item in value:
                        if not self.__validate_argument_type__(item, item_parts[-1]):
                            result = False
                            break
                if result: # if still result is True, return True
                    return result
        return False

    def __call__(self, *args, **kwargs):
        from .current_prog import current_prog
        if self.args:
            tmp_args = list(args)
            if len(tmp_args) == 1:
                if type(tmp_args[0]) == tuple:
                    tmp_args = list(tmp_args[0])
        tmp_is_in_class = False
        try:
            tmp_is_in_class = copy.deepcopy(current_prog.current_class)
            current_prog.current_class = []
        except:
            pass
        current_prog.mem = args
        if len(current_prog.mem) == 1:
            current_prog.mem = current_prog.mem[0]
        default_vars = {}
        with_frame = True
        try:
            self.parent_object
            default_vars['this'] = self.parent_object
        except:
            if self.name in self.BUILTIN_WITHOUT_FRAME_ISOLATION_FUNCTIONS:
                with_frame = False

        # handle arguments
        if self.args:
            for arg in self.args:
                arg_name = arg[0].split(' ', 1)
                if len(arg_name) > 1:
                    arg_type = arg_name[0]
                    arg_name = arg_name[1]
                else:
                    arg_name = arg_name[0]
                if arg_name != '':
                    try:
                        default_vars[arg_name[1:]] = kwargs[arg_name[1:]]
                    except KeyError:
                        if len(arg) > 1:
                            default_vars[arg_name[1:]] = current_prog.eval(arg[1])

            for arg in self.args:
                arg_name = arg[0].split(' ', 1)
                arg_type = None
                if len(arg_name) > 1:
                    arg_type = arg_name[0]
                    arg_name = arg_name[1]
                else:
                    arg_name = arg_name[0]
                if arg_name != '':
                    if len(tmp_args) == 0:
                        try:
                            default_vars[arg_name[1:]]
                        except:
                            current_prog.raise_error('ArgumentError', 'too few arguments passed to function "' + self.name + '"')
                            return
                    else:
                        default_vars[arg_name[1:]] = tmp_args[0]
                        tmp_args.pop(0)
                    if arg_type != None and default_vars[arg_name[1:]] != None:
                        res = self.__validate_argument_type__(default_vars[arg_name[1:]], arg_type)
                        if not res:
                            if res is None:
                                what_given = default_vars[arg_name[1:]].__theclass__.__name__
                            else:
                                what_given = str(type(default_vars[arg_name[1:]]))
                            current_prog.raise_error('InvalidArgument', 'invalid argument type passed to "' + self.name + '" as "' + arg_name + '", it should be ' + arg_type + ', but ' + what_given + ' given')
                            return

        tmp_body = copy.deepcopy(self.body)
        tmp_func_parts = self.name.split('.')
        if len(tmp_func_parts) > 1:
            func_namespace = ''
            for part in tmp_func_parts[:-1]:
                func_namespace += part + '.'
            func_namespace = func_namespace.strip('.')
            tmp_body.insert(0, parser.parse('use ' + func_namespace)[0])
        current_prog.exec_func(tmp_body, with_frame, default_vars)
        if tmp_is_in_class:
            current_prog.current_class = tmp_is_in_class
        result = current_prog.get_mem()
        if self.return_type != None:
            if not self.__validate_argument_type__(result, self.return_type):
                # return value type is not valid. raise the error
                what_given = str(type(result))
                return current_prog.raise_error('InvalidReturnType',
                    'invalid value returned by "' + self.name + '", it should be ' + self.return_type + ', but ' + what_given + ' returned'
                )
        return result
