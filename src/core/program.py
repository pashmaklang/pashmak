#
# program.py
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

""" Pashmak program Exceutor """

import sys
import os
import signal
import copy
from pathlib import Path
from . import helpers, version, modules, jit, parser, current_prog
from .class_system import Class, ClassObject
from .function import Function

import hashlib, time, random, datetime, base64, json, http, http.cookies, http.server, http.client, http.cookiejar, socket, socketserver, math, pprint

class Program(helpers.Helpers):
    """ Pashmak program object """
    def __init__(self, is_test=False, args=[]):
        self.threads = [{
            'current_step': 0,
            'commands': [parser.parse('pass')[0]],
            'used_namespaces': [],
            'vars': {
                'argv': args,
                'argc': len(args)
            }
        }] # list of threads
        self.functions = {
            "mem": Function(name='mem'), # mem is a empty function just for save mem in code
            "rmem": Function(name='rmem'),
        } # declared functions <function-name>:[<list-of-body-commands>]
        self.sections = {} # list of declared sections <section-name>:<index-of-command-to-jump>
        self.classes = {} # list of declared classes
        self.imported_files = [] # list of imported files
        self.mem = None # memory temp value
        self.is_test = is_test # program is in testing state
        self.output = '' # program output (for testing state)
        self.runtime_error = None # program raised error (for testing state)
        self.try_endtry = [] # says program is in try-endtry block
        self.namespaces_tree = [] # namespaces tree
        self.included_modules = [] # list of included modules to stop repeating imports

        self.allowed_pashmak_extensions = ['pashm']

        self.threads[-1]['current_step'] = 0
        self.stop_after_error = True
        self.main_filename = os.getcwd() + '/__main__'

        # set argument variables
        self.set_var('argv', args)
        self.set_var('argc', len(self.get_var('argv')))

        self.out_started = False
        self.out_content = ''

        self.current_func = []
        self.current_class = []

        self.func_depth = 0

        current_prog.current_prog = self

    def import_script(self, paths, import_once=False):
        """ Imports scripts/modules """
        op = self.threads[-1]['commands'][self.threads[-1]['current_step']]

        if type(paths) == str:
            paths = [paths]
        elif type(paths) != tuple:
            return self.raise_error('ArgumentError', 'invalid argument type', op)

        for path in paths:
            code_location = path
            commands = []
            if path[0] == '@':
                code_location = path
                module_name = path[1:]
                try:
                    namespaces_prefix = self.current_namespace()
                    namespaces_prefix += '@'
                    if not namespaces_prefix + module_name in self.included_modules:
                        content = modules.modules[module_name]
                        commands = parser.parse(content, filepath=code_location)
                        # add this module to imported modules
                        self.included_modules.append(namespaces_prefix + module_name)
                    else:
                        return
                except KeyError:
                    return self.raise_error('ModuleError', 'undefined module "' + module_name + '"', op)
            else:
                if path[0] != '/':
                    path = os.path.dirname(os.path.abspath(self.main_filename)) + '/' + path
                if os.path.abspath(path) in self.imported_files and import_once:
                    return
                try:
                    code_location = path
                    commands = jit.load(path, code_location, self)
                    self.imported_files.append(os.path.abspath(code_location))
                except FileNotFoundError as ex:
                    return self.raise_error('FileError', str(ex), op)
                except PermissionError as ex:
                    return self.raise_error('FileError', str(ex), op)

            self.exec_func(commands, False)

    def set_commands(self, commands: list):
        """ Set commands list """
        # setup environment
        self.set_var('__file__', os.path.abspath(self.main_filename))
        self.set_var('__dir__', os.path.dirname(os.path.abspath(self.main_filename)))
        self.set_var('__ismain__', True)
        self.import_script('@stdlib')
        # set commands on program object
        self.threads[-1]['commands'] = commands

    def get_mem(self):
        """ Return memory value and empty that """
        mem = self.mem
        self.mem = None
        return mem

    def raise_error(self, error_type: str, message: str, op=None):
        """ Raise error in program """
        if op == None:
            op = self.threads[-1]['commands'][self.threads[-1]['current_step']]
        # check is in try
        if self.try_endtry:
            section_index = self.try_endtry[-1]
            self.try_endtry.pop()
            new_step = self.sections[str(section_index)]
            while True:
                try:
                    if self.threads[-1]['commands'][new_step-1]['command'] == 'pass':
                        self.threads[-1]['current_step'] = new_step-1
                        break
                    else:
                        self.threads.pop()
                except:
                    self.threads.pop()

            # put error data in mem
            self.mem = copy.deepcopy(self.classes['Error'])
            self.mem.type = error_type
            self.mem.message = message
            self.mem.file_path = op['file_path']
            self.mem.line_number = op['line_number']
            return
        # raise error
        if self.is_test:
            self.runtime_error = {'type': error_type, 'message': message}
            if self.stop_after_error:
                self.threads = self.threads[:1]
                self.threads[-1]['current_step'] = len(self.threads[-1]['commands'])*2
            return

        # render error
        print(error_type + ': ' + message + ':')
        last_thread = self.threads[0]
        for thread in self.threads[1:]:
            try:
                if last_thread:
                    tmp_op = last_thread['commands'][last_thread['current_step']]
                else:
                    tmp_op = thread['commands'][0]
                print(
                    '\tin ' + tmp_op['file_path'] + ':' + str(tmp_op['line_number'])\
                    + ': ' + tmp_op['str']
                )
            except KeyError:
                pass
            last_thread = thread
        print('\tin ' + op['file_path'] + ':' + str(op['line_number']) + ': ' + op['str'])
        sys.exit(1)

    def exec_func(self, func_body: list, with_thread=True, default_variables={}):
        """ Gets a list from commands and runs them as function or included script """
        old_dir = self.get_var('__dir__')
        old_file = self.get_var('__file__')
        # create new thread for this call
        if with_thread:
            thread_vars = dict(self.threads[-1]['vars'])
        else:
            thread_vars = self.threads[-1]['vars']

        for k in default_variables:
            thread_vars[k] = default_variables[k]
        if len(func_body) > 0:
            thread_vars['__file__'] = os.path.abspath(func_body[0]['file_path'])
            if os.path.isfile(thread_vars['__file__']):
                thread_vars['__dir__'] = os.path.dirname(thread_vars['__file__'])
        used_namespaces = []
        if not with_thread:
            used_namespaces = self.threads[-1]['used_namespaces']
        self.threads.append({
            'current_step': 0,
            'commands': func_body,
            'vars': thread_vars,
            'used_namespaces': used_namespaces,
        })

        # run function
        self.start_thread()

        self.set_var('__dir__', old_dir)
        self.set_var('__file__', old_file)

    def get_func_real_name(self, name: str):
        """ Returns function real name """
        real_name = False
        try:
            func_body = self.functions[self.current_namespace() + name]
            real_name = self.current_namespace() + name
        except KeyError:
            func_body = False
            for used_namespace in self.threads[-1]['used_namespaces']:
                try:
                    func_body = self.functions[used_namespace + '.' + name]
                    real_name = used_namespace + '.' + name
                except KeyError:
                    pass
            if not func_body:
                try:
                    func_body = self.functions[name]
                    real_name = name
                except KeyError:
                    real_name = False
        return real_name

    def get_class_real_name(self, name: str):
        """ Returns class real name """
        real_name = False
        try:
            class_body = self.classes[self.current_namespace() + name]
            real_name = self.current_namespace() + name
        except KeyError:
            class_body = False
            for used_namespace in self.threads[-1]['used_namespaces']:
                try:
                    class_body = self.classes[used_namespace + '.' + name]
                    real_name = used_namespace + '.' + name
                except KeyError:
                    pass
            if not class_body:
                try:
                    class_body = self.classes[name]
                    real_name = name
                except KeyError:
                    real_name = False
        return real_name

    def eval(self, command, only_parse=False, varname_as_dict=False, only_str_parse=False, dont_check_vars=False):
        """ Runs eval on command """
        command_parts = parser.parse_string(command)

        if only_str_parse:
            return command_parts

        full_op = ''
        opened_inline_calls_count = 0
        for code in command_parts:
            if code[0] == False:
                code = code[1]
                # replace variable names with value of them
                literals = parser.literals
                code_words = self.multi_char_split(code, literals)
                for word in code_words:
                    if word:
                        if word[0] == '$':
                            if dont_check_vars == False:
                                self.variable_required(word[1:], self.threads[-1]['commands'][self.threads[-1]['current_step']])
                            if varname_as_dict:
                                code = code.replace('$' + word[1:], 'self.all_vars()["' + word[1:] + '"]', 1)
                            else:
                                code = code.replace('$' + word[1:], 'self.get_var("' + word[1:] + '")', 1)
                        else:
                            func_real_name = self.get_func_real_name(word)
                            if func_real_name != False:
                                tmp_counter = 0
                                while tmp_counter < len(code):
                                    tmp_index = code.find(word, tmp_counter)
                                    if tmp_index < 0:
                                        tmp_counter = (+tmp_counter) + 1
                                    else:
                                        tmp_counter = tmp_index + 1
                                    if code[tmp_index-2:tmp_index] != '->':
                                        if code[tmp_index-1:tmp_index] in literals:
                                            if code[tmp_index+len(word):tmp_index+len(word)+1] in literals:
                                                code = code.replace(code[tmp_index-2:tmp_index] + word + code[tmp_index+len(word):tmp_index+len(word)+1], code[tmp_index-2:tmp_index] + 'self.functions["' + func_real_name + '"]' + code[tmp_index+len(word):tmp_index+len(word)+1], 1)
                                                break
                            else:
                                # This is a class
                                class_real_name = self.get_class_real_name(word)
                                if class_real_name != False:
                                    tmp_counter = 0
                                    while tmp_counter < len(code):
                                        tmp_index = code.find(word, tmp_counter)
                                        if tmp_index < 0:
                                            tmp_counter = (+tmp_counter) + 1
                                        else:
                                            tmp_counter = tmp_index + 1
                                        if code[tmp_index-2:tmp_index] != '->':
                                            if code[tmp_index-1:tmp_index] in literals:
                                                if code[tmp_index+len(word):tmp_index+len(word)+1] in literals:
                                                    code = code.replace(code[tmp_index-2:tmp_index] + word + code[tmp_index+len(word):tmp_index+len(word)+1], code[tmp_index-2:tmp_index] + 'self.classes["' + class_real_name + '"]' + code[tmp_index+len(word):tmp_index+len(word)+1], 1)
                                                    break

                code = code.replace('->', '.')
                code = code.replace('^', 'self.get_mem()')
            else:
                code = code[1]
            full_op += code
        if only_parse:
            return full_op
        return eval(full_op)

    def run(self, op: dict):
        """ Run once command """

        op_name = op['command']

        if op_name == 'func':
            self.func_depth += 1

        if op_name == 'endfunc':
            if self.func_depth <= 1:
                self.run_endfunc(op)
                self.func_depth -= 1
                return
            self.func_depth -= 1

        # if a function is started, append current command to the function body
        if len(self.current_func) > 0:
            if len(self.current_class) > 0:
                self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].body.append(op)
            else:
                self.functions[self.current_func[-1]].body.append(op)
            return

        if op_name == 'endclass':
            self.run_endclass(op)
            return

        # list of commands
        commands_dict = {
            'free': self.run_free,
            'func': self.run_func,
            'goto': self.run_goto,
            'gotoif': self.run_gotoif,
            'isset': self.run_isset,
            'try': self.run_try,
            'endtry': self.run_endtry,
            'namespace': self.run_namespace,
            'ns': self.run_namespace,
            'endnamespace': self.run_endnamespace,
            'use': self.run_use,
            'class': self.run_class,
            'endclass': self.run_endclass,
            'return': self.run_return,
            'while': self.run_while,
            'endwhile': self.run_endwhile,
            'break': self.run_break,
            'continue': self.run_continue,
            'pass': None,
            'if': None,
            'elif': None,
            'else': None,
            'endif': None,
        }

        # check op_name is a valid command
        op_func = 0
        try:
            op_func = commands_dict[op_name]
        except:
            pass

        # if op_name is a valid command, run the function
        if op_func != 0:
            if op_func != None:
                op_func(op)
            return

        if op['str'][0] == '$':
            # if a class is started, append current command as a property to class
            is_in_class = False
            if len(self.current_class) > 0:
                is_in_class = True
            parts = self.split_by_equals(op['str'].strip())
            if len(parts) <= 1:
                if '->' in op['str'] or '(' in op['str'] or ')' in op['str']:
                    self.mem = self.eval(op['str'])
                    return
            varname = parts[0].strip()
            full_varname = varname
            varname = varname.split('->', 1)
            is_class_setting = False
            if len(varname) > 1:
                is_class_setting = varname[1].replace('->', '.')
            varname = varname[0]
            if len(parts) <= 1:
                if is_in_class:
                    self.classes[self.current_class[-1]].__props__[varname[1:]] = None
                else:
                    self.set_var(varname[1:], None)
                return
            value = None
            if True:
                value = self.eval(parts[1].strip())
            if is_class_setting != False:
                tmp_real_var = self.eval(varname)
                exec('tmp_real_var.' + is_class_setting + ' = value')
            else:
                if is_in_class:
                    self.classes[self.current_class[-1]].__props__[varname[1:]] = value
                else:
                    if '[' in varname or ']' in varname:
                        the_target = self.eval(varname, only_parse=True)
                        exec(the_target + ' = value')
                    else:
                        self.set_var(varname[1:], value)
            return

        parts = self.split_by_equals(op['str'].strip())
        if len(parts) > 1:
            part1 = self.eval(parts[0], only_parse=True)
            part2 = self.eval(parts[1], only_parse=True)
            exec(part1 + ' = ' + part2)
            return

        # check function exists
        func_real_name = self.get_func_real_name(op_name)
        if func_real_name == False:
            self.mem = self.eval(op['str'])
            return
        func_body = self.functions[func_real_name]

        # run function
        try:
            # put argument in the mem
            if op['args_str'] != '' and op['args_str'].strip() != '()':
                if op['command'] == 'rmem':
                    self.eval(op['args_str'])
                    return
                else:
                    func_arg = self.eval(op['args_str'])
            else:
                func_arg = None

            # execute function body
            self.mem = func_arg
            if op_name in ['import', 'mem', 'python', 'rmem', 'eval']:
                self.exec_func(func_body.body, False)
            else:
                self.mem = func_body(self.mem)
            return
        except Exception as ex:
            raise

    def bootstrap_modules(self):
        """ Loads modules from module paths in environment variable """
        try:
            os.environ['PASHMAKPATH']
        except:
            os.environ['PASHMAKPATH'] = ''
        home_directory = str(Path.home())
        os.environ['PASHMAKPATH'] = '/usr/lib/pashmak_modules:' + home_directory + '/.local/lib/pashmak_modules:' + os.environ['PASHMAKPATH']
        pashmak_module_paths = os.environ['PASHMAKPATH']
        paths = pashmak_module_paths.strip().split(':')
        paths = [path.strip() for path in paths if path.strip() != '']
        for path in paths:
            try:
                path_files = os.listdir(path)
            except:
                continue
            for f in path_files:
                module_name = None
                if os.path.isdir(path + '/' + f):
                    if os.path.isfile(path + '/' + f + '/__init__.pashm'):
                        module_name = f.split('/')[-1].split('.')[0]
                        f = path + '/' + f + '/__init__.pashm'
                    else:
                        f = path + '/' + f
                else:
                    f = path + '/' + f

                if f.split('.')[-1] in self.allowed_pashmak_extensions:
                    if os.path.isfile(f):
                        # check module exists
                        f_name = f.split('/')[-1]
                        if module_name == None:
                            module_name = f_name.split('.')[0]
                        try:
                            modules.modules[module_name]
                        except:
                            # module not found, we can add this
                            try:
                                fo = open(f, 'r')
                                content = fo.read()
                                fo.close()
                                content = '$__file__ = "' + os.path.abspath(f).replace('\\', '\\\\') + '";\n$__dir__ = "' + os.path.dirname(os.path.abspath(f)).replace('\\', '\\\\') + '";\n' + content
                                modules.modules[module_name] = content
                            except:
                                raise
                                pass

    def start_thread(self):
        """ Start running last thread """
        is_in_func = False
        self.threads[-1]['current_step'] = 0

        # load the sections
        i = 0
        while i < len(self.threads[-1]['commands']):
            current_op = self.threads[-1]['commands'][i]
            if current_op['command'] == 'section':
                if not is_in_func:
                    arg = current_op['args'][0]
                    self.sections[arg] = i+1
                    self.threads[-1]['commands'][i] = parser.parse('pass', filepath='<system>')[0]
            elif current_op['command'] == 'func':
                is_in_func = True
            elif current_op['command'] == 'endfunc':
                is_in_func = False
            i += 1

        self.threads[-1]['current_step'] = 0
        while self.threads[-1]['current_step'] < len(self.threads[-1]['commands']):
            try:
                self.run(self.threads[-1]['commands'][self.threads[-1]['current_step']])
            except Exception as ex:
                try:
                    self.threads[-1]['commands'][self.threads[-1]['current_step']]
                except:
                    break
                self.raise_error(
                    ex.__class__.__name__,
                    str(ex),
                    self.threads[-1]['commands'][self.threads[-1]['current_step']]
                )
            self.threads[-1]['current_step'] += 1

        if len(self.threads) > 1:
            self.threads.pop()

    def start(self):
        """ Start running the program """

        signal.signal(signal.SIGINT, self.signal_handler)

        self.bootstrap_modules()

        self.start_thread()
