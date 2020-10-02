#
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
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

''' Pashmak program object '''

import sys, os
from syntax import parser
from core import helpers

class Program(helpers.Helpers):
    ''' Pashmak program object '''

    def __init__(self , is_test=False , args=[]):
        self.variables = {}
        self.aliases = {}
        self.operations = []
        self.sections = {}
        self.mem = None
        self.is_test = is_test
        self.output = ''
        self.runtime_error = None
        self.is_in_try = None
        self.runed_aliases = []

        # set argument variables
        self.variables['argv'] = args
        self.variables['argc'] = len(self.variables['argv'])

    def set_operations(self , operations: list):
        # include stdlib before everything
        tmp = parser.parse('mem "@stdlib"; include ^;')
        operations.insert(0 , tmp[0])
        operations.insert(1 , tmp[1])
        # get list of operations and set it on program object
        self.operations = operations

    def set_operation_index(self , op: dict) -> dict:
        ''' Add operation index to operation dictonary '''
        op['index'] = self.current_step
        return op

    def get_mem(self):
        ''' Return memory value and empty that '''
        mem = self.mem
        self.mem = None
        return mem

    def raise_error(self , error_type: str , message: str , op: dict):
        ''' Raise error in program '''
        # check is in try
        if self.is_in_try != None:
            section_index = self.is_in_try
            self.is_in_try = None
            new_step = self.sections[str(section_index)]
            self.current_step = new_step-1

            # put error data in mem
            self.mem = {'type': error_type , 'message': message , 'index': op['index']}
            return
        # raise error
        if self.is_test:
            self.runtime_error = [error_type , message , op]
            return
        print(error_type + ' in ' + str(op['index']) + ':\n\t' + op['str'] + '\n\t' + message)
        sys.exit(1)

    def exec_alias(self , alias_body: list):
        if self.current_step in self.runed_aliases:
            return
        self.runed_aliases.append(self.current_step)
        i = int(self.current_step)
        for alias_op in alias_body:
            alias_op_parsed = self.set_operation_index(alias_op)
            if alias_op_parsed['command'] == 'section':
                section_name = alias_op_parsed['args'][0]
                self.sections[section_name] = i+1
            else:
                self.operations.insert(i+1 , alias_op)
                i += 1

    def run(self , op: dict):
        ''' Run once operation '''

        op = self.set_operation_index(op)
        op_name = op['command']

        if op_name == 'endalias':
            self.run_endalias(op)
            return

        # if a alias is started, append current operation to the alias body
        try:
            tmp = self.current_alias
            self.aliases[self.current_alias].append(op)
            return
        except:
            pass

        if op_name == 'set':
            self.run_set(op)
            return
        elif op_name == 'free':
            self.run_free(op)
            return
        elif op_name == 'copy':
            self.run_copy(op)
            return
        elif op_name == 'mem':
            self.run_mem(op)
            return
        elif op_name == 'out':
            self.run_out(op)
            return
        elif op_name == 'read':
            self.run_read(op)
            return
        elif op_name == 'return':
            self.run_return(op)
            return
        elif op_name == 'alias':
            self.run_alias(op)
            return
        elif op_name == 'required':
            self.run_required(op)
            return
        elif op_name == 'typeof':
            self.run_typeof(op)
            return
        elif op_name == 'system':
            self.run_system(op)
            return
        elif op_name == 'include':
            self.run_include(op)
            return
        elif op_name == 'goto':
            self.run_goto(op)
            return
        elif op_name == 'gotoif':
            self.run_gotoif(op)
            return
        elif op_name == 'fread':
            self.run_fread(op)
            return
        elif op_name == 'fwrite':
            self.run_fwrite(op)
            return
        elif op_name == 'chdir':
            self.run_chdir(op)
            return
        elif op_name == 'cwd':
            self.run_cwd(op)
            return
        elif op_name == 'isset':
            self.run_isset(op)
            return
        elif op_name == 'try':
            self.run_try(op)
            return
        elif op_name == 'endtry':
            self.run_endtry(op)
            return
        elif op_name == 'eval':
            self.run_eval(op)
            return
        elif op_name == 'arraypush':
            self.run_arraypush(op)
            return
        elif op_name == 'arraypop':
            self.run_arraypop(op)
            return
        elif op_name == 'python':
            self.run_python(op)
            return
        elif op_name == 'pass':
            return



        # check alias exists
        try:
            alias_body = self.aliases[op_name]
        except:
            self.raise_error('SyntaxError' , 'undefined operation "' + op_name + '"' , op)
            return

        # run alias
        try:
            # put argument in the mem
            if op['args_str'] != '':
                args = op['args_str']
                code = '(' + args + ')'
                # replace variable names with value of them
                for k in self.variables:
                    code = code.replace('$' + k , 'self.variables["' + k + '"]')
                self.mem = eval(code)
            else:
                self.mem = ''
            
            # execute alias body
            self.exec_alias(alias_body)
            return
        except Exception as ex:
            self.raise_error('RuntimeError' , str(ex) , op)

        

    def start(self):
        ''' Start running the program '''

        is_in_alias = False
        self.current_step = 0
        
        # load the sections
        i = 0
        while i < len(self.operations):
            current_op = self.set_operation_index(self.operations[i])
            if current_op['command'] == 'section':
                if not is_in_alias:
                    arg = current_op['args'][0]
                    self.sections[arg] = i+1
                    self.operations[i] = parser.parse('pass')[0]
            elif current_op['command'] == 'alias':
                is_in_alias = True
            elif current_op['command'] == 'endalias':
                is_in_alias = False
            i += 1

        self.current_step = 0
        while self.current_step < len(self.operations):
            try:
                self.run(self.operations[self.current_step])
            except Exception as ex:
                self.raise_error('RuntimeError' , str(ex) , self.set_operation_index(self.operations[self.current_step]))
            self.current_step += 1
