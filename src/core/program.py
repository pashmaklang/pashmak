#
# program.py
#
# The Pashmak Project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
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

''' Pashmak program object '''

import sys
import os
import signal
from syntax import parser
from core import helpers, version, modules

class Program(helpers.Helpers):
    ''' Pashmak program object '''

    def __init__(self, is_test=False, args=[]):
        self.variables = {} # main state variables
        self.states = [] # list of states
        self.functions = {
            "mem": [] # mem is a empty function just for save mem in code
        } # declared functions <function-name>:[<list-of-body-operations>]
        self.operations = [] # list of operations
        self.sections = {} # list of declared sections <section-name>:<index-of-operation-to-jump>
        self.mem = None # memory temp value
        self.is_test = is_test # program is in testing state
        self.output = '' # program output (for testing state)
        self.runtime_error = None # program raised error (for testing state)
        self.try_endtry = [] # says program is in try-endtry block
        self.runed_functions = [] # runed functions for stop function multi calling in one operation
        self.namespaces_tree = [] # namespaces tree
        self.used_namespaces = [] # list of used namespaces
        self.included_modules = [] # list of included modules to stop repeating imports
        self.bootstrap_operations_count = 0

        self.allowed_pashmak_extensions = ['pashm'] # TODO : add more extensions

        self.current_step = 0
        self.stop_after_error = True
        self.main_filename = os.getcwd() + '/__main__'

        # set argument variables
        self.set_var('argv', args)
        self.set_var('argc', len(self.get_var('argv')))

    def current_namespace(self):
        ''' Returns current namespace '''
        namespace_prefix = ''
        for ns in self.namespaces_tree:
            namespace_prefix += ns + '.'
        return namespace_prefix

    def set_operations(self, operations: list):
        ''' Set operations list '''
        # include stdlib before everything
        tmp = parser.parse('''
        $__file__ = "''' + os.path.abspath(self.main_filename) + '''";
        $__dir__ = "''' + os.path.dirname(os.path.abspath(self.main_filename)) + '''";
        mem "@stdlib"; include ^; py "self.bootstrap_operations_count = len(self.operations)-4";'
        ''')
        operations.insert(0, tmp[0])
        operations.insert(1, tmp[1])
        operations.insert(2, tmp[2])
        operations.insert(3, tmp[3])
        operations.insert(4, tmp[4])

        # set operations on program object
        self.operations = operations

    def set_operation_index(self, op: dict) -> dict:
        ''' Add operation index to operation dictonary '''
        op['index'] = self.current_step
        return op

    def get_mem(self):
        ''' Return memory value and empty that '''
        mem = self.mem
        self.mem = None
        return mem

    def update_section_indexes(self, after_index):
        '''
        When a new operation inserted in operations list,
        this function add 1 to section indexes to be
        sync with new operations list
        '''
        for k in self.sections:
            if self.sections[k] > after_index:
                self.sections[k] = self.sections[k] + 1
        i = 0
        while i < len(self.runed_functions):
            if self.runed_functions[i] > after_index:
                self.runed_functions[i] = self.runed_functions[i] + 1
            i += 1

    def raise_error(self, error_type: str, message: str, op: dict):
        ''' Raise error in program '''
        # check is in try
        if self.try_endtry:
            section_index = self.try_endtry[-1]
            self.try_endtry.pop()
            new_step = self.sections[str(section_index)]
            self.current_step = new_step-1

            # put error data in mem
            self.mem = {'type': error_type, 'message': message, 'index': op['index']}
            return
        # raise error
        if self.is_test:
            self.runtime_error = {'type': error_type, 'message': message, 'index': op['index']}
            if self.stop_after_error:
                self.current_step = len(self.operations)*2
            return

        # render error
        print(error_type + ': ' + message + ':')
        for state in self.states:
            try:
                tmp_op = self.operations[state['entry_point']]
                print(
                    '\tin ' + str(tmp_op['index']-self.bootstrap_operations_count)\
                    + ': ' + tmp_op['str']
                )
            except KeyError:
                pass
        print('\tin ' + str(op['index']-self.bootstrap_operations_count) + ': ' + op['str'])
        sys.exit(1)

    def exec_func(self, func_body: list, with_state=True):
        ''' Gets a list from operations and runs them as function or included script '''
        # create new state for this call
        if with_state:
            self.states.append({
                'entry_point': self.current_step,
                'vars': dict(self.variables),
            })

        # check function already called in this point
        if self.current_step in self.runed_functions and with_state:
            return

        # add this point to runed functions (for stop repeating call in loops)
        if with_state:
            self.runed_functions.append(self.current_step)

        # run function
        i = int(self.current_step)
        is_in_func = False
        for func_op in func_body:
            func_op_parsed = self.set_operation_index(func_op)
            if func_op_parsed['command'] == 'section' and not is_in_func:
                section_name = func_op_parsed['args'][0]
                self.sections[section_name] = i+1
            else:
                if func_op_parsed['command'] == 'func':
                    is_in_func = True
                elif func_op_parsed['command'] == 'endfunc':
                    is_in_func = False
                self.operations.insert(i+1, func_op)
                self.update_section_indexes(i+1)
                i += 1

        if with_state:
            self.operations.insert(i+1, parser.parse('popstate')[0])
            self.update_section_indexes(i+1)

    def eval(self, operation):
        ''' Runs eval on operation '''
        code = '(' + operation + ')'
        # replace variable names with value of them
        for k in self.all_vars():
            code = code.replace('$' + k, 'self.get_var("' + k + '")')
            for used_namespace in self.used_namespaces:
                if k[:len(used_namespace)+1] == used_namespace + '.':
                    tmp = k[len(used_namespace)+1:]
                    code = code.replace('$' + tmp, 'self.get_var("' + k + '")')

        return eval(code)

    def run(self, op: dict):
        ''' Run once operation '''

        op = self.set_operation_index(op)
        op_name = op['command']

        if op_name == 'endfunc':
            self.run_endfunc(op)
            return

        if op_name == 'popstate':
            if self.states:
                self.states.pop()
            return

        # if a function is started, append current operation to the function body
        try:
            self.current_func
            self.functions[self.current_func].append(op)
            return
        except NameError:
            pass
        except KeyError:
            pass
        except AttributeError:
            pass

        # list of operations
        operations_dict = {
            'set': self.run_set,
            'free': self.run_free,
            'copy': self.run_copy,
            'read': self.run_read,
            'return': self.run_return,
            'func': self.run_func,
            'required': self.run_required,
            'typeof': self.run_typeof,
            'system': self.run_system,
            'include': self.run_include,
            'goto': self.run_goto,
            'gotoif': self.run_gotoif,
            'fread': self.run_fread,
            'fwrite': self.run_fwrite,
            'chdir': self.run_chdir,
            'cwd': self.run_cwd,
            'isset': self.run_isset,
            'out': self.run_out,
            'try': self.run_try,
            'endtry': self.run_endtry,
            'eval': self.run_eval,
            'arraypush': self.run_arraypush,
            'arraypop': self.run_arraypop,
            'python': self.run_python,
            'namespace': self.run_namespace,
            'endnamespace': self.run_endnamespace,
            'use': self.run_use,
            'pass': None,
        }

        # check op_name is a valid operation
        op_func = 0
        try:
            op_func = operations_dict[op_name]
        except:
            pass

        # if op_name is a valid operation, run the function
        if op_func != 0:
            if op_func != None:
                op_func(op)
            return

        # check operation syntax is variable value setting
        if op['str'][0] == '$':
            parts = op['str'].strip().split('=', 1)
            varname = parts[0].strip()
            if len(parts) <= 1:
                self.set_var(varname[1:], None)
                return
            value = None
            if parts[1].strip()[0] == '^' and len(parts[1].strip()) > 1:
                cmd = parts[1].strip()[1:].strip()
                # insert cmd after current operation
                self.operations.insert(self.current_step+1, parser.parse(cmd)[0])
                self.update_section_indexes(self.current_step+1)
                self.operations.insert(self.current_step+2, parser.parse(varname + ' = ^')[0])
                self.update_section_indexes(self.current_step+2)
                return
            elif parts[1].strip() == '^':
                value = self.get_mem()
            else:
                value = self.eval(parts[1].strip())
            self.set_var(varname[1:], value)
            return

        # check function exists
        try:
            func_body = self.functions[self.current_namespace() + op_name]
        except KeyError:
            func_body = None
            for used_namespace in self.used_namespaces:
                try:
                    func_body = self.functions[used_namespace + '.' + op_name]
                except KeyError:
                    pass
            if not func_body:
                try:
                    func_body = self.functions[op_name]
                except KeyError:
                    self.raise_error('SyntaxError', 'undefined operation "' + op_name + '"', op)
                    return

        # run function
        try:
            # put argument in the mem
            if op['args_str'] != '':
                self.mem = self.eval(op['args_str'])
            else:
                self.mem = ''

            # execute function body
            self.exec_func(func_body)
            return
        except Exception as ex:
            self.raise_error('RuntimeError', str(ex), op)

    def signal_handler(self, signal_code, frame):
        ''' Raise error when signal exception raised '''
        self.raise_error('Signal', str(signal_code), self.operations[self.current_step])

    def bootstrap_modules(self):
        """ Loads modules from module paths in environment variable """
        try:
            pashmak_module_paths = os.environ['PASHMAKPATH']
        except:
            return
        paths = pashmak_module_paths.strip().split(':')
        paths = [path.strip() for path in paths if path.strip() != '']
        for path in paths:
            try:
                path_files = os.listdir(path)
            except:
                continue
            for f in path_files:
                if f.split('.')[-1] in self.allowed_pashmak_extensions:
                    if os.path.isfile(path + '/' + f):
                        # check module exists
                        f_name = f.split('/')[-1]
                        module_name = f.split('.')[0]
                        try:
                            modules.modules[module_name]
                        except:
                            # module not found, we can add this
                            try:
                                f = open(path + '/' + f, 'r')
                                content = f.read()
                                f.close()
                                content = '$__file__ = "' + os.path.abspath(path + '/' + f) + '";\n$__dir__ = "' + os.path.dirname(os.path.abspath(path + '/' + f)) + '";\n' + content
                                modules.modules[module_name] = content
                            except:
                                pass

    def start(self):
        ''' Start running the program '''

        signal.signal(signal.SIGINT, self.signal_handler)

        self.bootstrap_modules()

        is_in_func = False
        self.current_step = 0

        # load the sections
        i = 0
        while i < len(self.operations):
            current_op = self.set_operation_index(self.operations[i])
            if current_op['command'] == 'section':
                if not is_in_func:
                    arg = current_op['args'][0]
                    self.sections[arg] = i+1
                    self.operations[i] = parser.parse('pass')[0]
            elif current_op['command'] == 'func':
                is_in_func = True
            elif current_op['command'] == 'endfunc':
                is_in_func = False
            i += 1

        self.current_step = 0
        while self.current_step < len(self.operations):
            try:
                self.run(self.operations[self.current_step])
            except Exception as ex:
                try:
                    self.set_operation_index(self.operations[self.current_step])
                except:
                    break
                self.raise_error(
                    'RuntimeError',
                    str(ex),
                    self.set_operation_index(self.operations[self.current_step])
                )
            self.current_step += 1
