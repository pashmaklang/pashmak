# program.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################

import sys
import os
from syntax import parser
from core import commands

class Program(commands.Commands):
    def __init__(self):
        self.variables = {}
        self.aliases = {}
        self.operations = []
        self.sections = {}
        self.mem = None

    def set_operations(self , operations):
        # get list of operations and set it on program object
        self.operations = operations

    def parse_op(self , op_str):
        # parse a operation from string to the object
        op = {}
        op['str'] = op_str
        op_parts = op_str.split(' ')
        op['command'] = op_parts[0]
        op_parts.pop(0)
        op['args_str'] = ''
        for op_part in op_parts:
            for ch in op_part:
                op['args_str'] += ch
            op['args_str'] += ' '
        op['index'] = self.current_step
        return op

    def get_mem(self):
        # return memory value and after empty that
        mem = self.mem
        self.mem = None
        return mem

    def raise_error(self , error_type , message , op):
        # raise error
        print(error_type + ' in ' + str(op['index']) + ':\n\t' + op['str'] + '\n\t' + message)
        sys.exit(1)

    # run once operation
    def run(self , operation_str):
        op = self.parse_op(operation_str)
        op_name = op['command']

        if op_name == 'endalias':
            self.run_endalias(op)
            return

        # if a alias is started, append current operation to the alias body
        try:
            tmp = self.current_alias
            self.aliases[self.current_alias].append(operation_str)
            return
        except:
            pass

        if op_name == 'set':
            self.run_set(op)
            return

        if op_name == 'free':
            self.run_free(op)
            return

        if op_name == 'copy':
            self.run_copy(op)
            return

        if op_name == 'mem':
            self.run_mem(op)
            return

        if op_name == 'out':
            self.run_out(op)
            return

        if op_name == 'read':
            self.run_read(op)
            return

        if op_name == 'return':
            self.run_return(op)
            return

        if op_name == 'alias':
            self.run_alias(op)
            return

        if op_name == 'call':
            self.run_call(op)
            return

        if op_name == 'required':
            self.run_required(op)
            return

        if op_name == 'typeof':
            self.run_typeof(op)
            return

        if op_name == 'system':
            self.run_system(op)
            return

        if op_name == 'include':
            self.run_include(op)
            return

        if op_name == 'goto':
            self.run_goto(op)
            return

        if op_name == 'gotoif':
            self.run_gotoif(op)
            return

        self.raise_error('SyntaxError' , 'undefined operation "' + op_name + '"' , op)

    def start(self):
        # start running operations

        is_in_alias = False
        self.current_step = 0
        
        # load the sections
        i = 0
        while i < len(self.operations):
            current_op = self.parse_op(self.operations[i])
            if current_op['command'] == 'section':
                if not is_in_alias:
                    arg = current_op['args_str'].strip().split(' ')[0].strip()
                    self.sections[arg] = i
                    self.operations.pop(i)
            elif current_op['command'] == 'alias':
                is_in_alias = True
            elif current_op['command'] == 'endalias':
                is_in_alias = False
            i += 1

        self.current_step = 0
        while self.current_step < len(self.operations):
            self.run(self.operations[self.current_step])
            self.current_step += 1
