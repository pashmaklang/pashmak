#
# new.py
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

""" Creates a new instance from a class """

import copy
import random
from core.class_system import Class
from core import parser

def run(self, op: dict):
    """ Creates a new instance from a class """

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
