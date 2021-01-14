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
from . import lexer

class Function:
    """ the pashmak function object """
    def __init__(self, name):
        self.name = name
        self.body = []

    def __call__(self, *args, **kwargs):
        from .current_prog import current_prog
        current_prog.mem = args
        if len(current_prog.mem) == 1:
            current_prog.mem = current_prog.mem[0]
        default_vars = {}
        with_frame = True
        try:
            self.parent_object
            default_vars['this'] = self.parent_object
        except:
            if self.name in ['import', 'mem', 'python', 'rmem', 'eval']:
                with_frame = False
        tmp_body = copy.deepcopy(self.body)
        tmp_func_parts = self.name.split('.')
        if len(tmp_func_parts) > 1:
            func_namespace = ''
            for part in tmp_func_parts[:-1]:
                func_namespace += part + '.'
            func_namespace = func_namespace.strip('.')
            tmp_body.insert(0, lexer.parse('use ' + func_namespace)[0])
        current_prog.exec_func(tmp_body, with_frame, default_vars)
        return current_prog.get_mem()
