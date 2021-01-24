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
    BUILTIN_WITHOUT_FRAME_ISOLATION_FUNCTIONS = ['import', 'import_once', 'import_run', 'import_run_once', 'mem', 'python', 'rmem', 'eval', 'set', 'get', 'free']
    def __init__(self, name):
        self.name = name
        self.body = []
        self.args = []

    def __call__(self, *args, **kwargs):
        from .current_prog import current_prog
        if len(self.args) > 0:
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
        if len(self.args) > 0:
            for arg in self.args:
                if arg[0] != '':
                    try:
                        default_vars[arg[0][1:]] = kwargs[arg[0][1:]]
                    except KeyError:
                        if len(arg) > 1:
                            default_vars[arg[0][1:]] = current_prog.eval(arg[1])
            for arg in self.args:
                if arg[0] != '':
                    if len(tmp_args) == 0:
                        try:
                            default_vars[arg[0][1:]]
                        except:
                            current_prog.raise_error('ArgumentError', 'too few arguments passed to function "' + self.name + '"')
                            return
                    else:
                        default_vars[arg[0][1:]] = tmp_args[0]
                        tmp_args.pop(0)

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
        return current_prog.get_mem()
