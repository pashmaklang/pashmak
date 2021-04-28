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
from . import helpers, version, modules, jit, parser, current_prog, lexer
from .class_system import Class, ClassObject
from .function import Function

import hashlib, time, random, datetime, base64, json
import http, http.cookies, http.server, http.client, http.cookiejar, socket, socketserver
import math, pprint, subprocess, sqlite3, sqlite3.dump, sqlite3.dbapi2
import urllib, urllib.error, urllib.parse, urllib.request, urllib.response
import urllib.robotparser, platform, mimetypes, re, pickle, io

def free(name):
    from . import current_prog
    try:
        del current_prog.current_prog.all_vars()[name]
    except KeyError:
        pass

class Program(helpers.Helpers):
    """ Pashmak program object """
    def __init__(self, is_test=False, args=[]):
        self.frames = [{
            'current_step': 0,
            'commands': [parser.parse('pass')[0]],
            'used_namespaces': [],
            'imported_modules': [],
            'vars': {
                'argv': args,
                'argc': len(args)
            }
        }] # list of frames
        self.functions = {
            "mem": Function(name='mem'), # mem is a empty function just for save mem in code
            "rmem": Function(name='rmem'),
        } # declared functions <function-name>:[<list-of-body-commands>]
        self.labels = {} # list of declared label <label-name>:<index-of-command-to-jump>
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

        self.stop_after_error = True
        self.main_filename = os.getcwd() + '/__main__'

        self.out_started = False
        self.out_content = ''

        self.current_func = []
        self.current_class = []

        self.func_depth = 0

        self.module_path = []

        self.last_docstring = ''

        self.shutdown_event = []

        self.defines = {}

        current_prog.current_prog = self

    def import_script(self, paths, import_once=False, ismain_default=False):
        """ Imports scripts/modules """
        op = self.frames[-1]['commands'][self.frames[-1]['current_step']]

        if type(paths) == str:
            paths = [paths]
        elif type(paths) != tuple and type(paths) != list:
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
                    is_currently_imported = False
                    z = len(self.frames)-1
                    while z >= 0:
                        if namespaces_prefix + module_name in self.frames[z]['imported_modules']:
                            is_currently_imported = True
                            z = -1
                        z -= 1
                    if not is_currently_imported:
                        try:
                            # search modules from builtin modules
                            commands = [parser.parse('$__ismain__ = ' + str(ismain_default),
                                                     filepath='@' + module_name)[0], 
                                                    *modules.modules[module_name],
                                                     parser.parse('$__ismain__ = ' + str(self.get_var('__ismain__')),
                                                     filepath='@' + module_name)[0]]
                        except KeyError:
                            # find modules from path
                            commands = False
                            for path in self.module_path:
                                path = os.path.abspath(path)
                                full_path = path + '/' + module_name.replace('.', '/')
                                full_path = os.path.abspath(full_path)
                                if os.path.isfile(full_path + '.pashm'):
                                    commands = jit.load(os.path.abspath(full_path + '.pashm'), os.path.abspath(full_path + '.pashm'), self, ismain_default=ismain_default)
                                elif os.path.isdir(full_path):
                                    if os.path.isfile(os.path.abspath(full_path + '/__init__.pashm')):
                                        commands = jit.load(os.path.abspath(full_path + '/__init__.pashm'), os.path.abspath(full_path + '/__init__.pashm'), self, ismain_default=ismain_default)
                            if commands == False:
                                raise KeyError()
                        # add this module to imported modules
                        self.frames[-1]['imported_modules'].append(namespaces_prefix + module_name)
                    else:
                        return
                except KeyError:
                    return self.raise_error('ModuleError', 'undefined module "' + module_name + '"', op)
            else:
                namespaces_prefix = self.current_namespace() + '@'
                is_currently_imported = False
                z = len(self.frames) - 1
                while z >= 0:
                    if namespaces_prefix + os.path.abspath(path) in self.frames[z]['imported_modules']:
                        is_currently_imported = True
                        z = -1
                    z -= 1
                if is_currently_imported and import_once:
                    return
                if os.path.isdir(path):
                    path += '/__init__.pashm'
                try:
                    code_location = path
                    commands = jit.load(path, code_location, self, ismain_default=ismain_default)
                    self.frames[-1]['imported_modules'].append(namespaces_prefix + os.path.abspath(path))
                except FileNotFoundError as ex:
                    return self.raise_error('FileError', str(ex), op)
                except PermissionError as ex:
                    return self.raise_error('FileError', str(ex), op)

            self.exec_func(commands, False)
        return self.get_mem()

    def set_commands(self, commands: list):
        """ Set commands list """
        # setup environment
        self.set_var('__file__', os.path.abspath(self.main_filename))
        self.set_var('__dir__', os.path.dirname(os.path.abspath(self.main_filename)))
        self.set_var('__ismain__', True)
        self.import_script('@stdlib')
        # set commands on program object
        self.frames[-1]['commands'] = commands

    def get_mem(self):
        """ Return memory value and empty that """
        mem = self.mem
        self.mem = None
        return mem

    def raise_error(self, error_type: str, message: str, op=None):
        """ Raise error in program """
        if op is None:
            op = self.frames[-1]['commands'][self.frames[-1]['current_step']]
        # check is in try
        if self.try_endtry:
            label_index = self.try_endtry[-1]
            self.try_endtry.pop()
            new_step = self.labels[str(label_index)]
            while True:
                try:
                    if self.frames[-1]['commands'][new_step-1]['command'] == 'pass':
                        self.frames[-1]['current_step'] = new_step-1
                        break
                    else:
                        self.frames.pop()
                except:
                    self.frames.pop()

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
                self.frames = self.frames[:1]
                self.frames[-1]['current_step'] = len(self.frames[-1]['commands'])*2
            return

        # check HIDE_ERRORS config
        hide_errors = False
        try:
            if self.defines['HIDE_ERRORS']:
                hide_errors = True
        except:
            pass

        # render error
        if not hide_errors:
            try:
                self.defines['WEB_INITED']
                print('<pre style="background-color: #cdcdcd; padding: 10px; border-radius: 10px;">')
            except:
                pass
            print(error_type + ': ' + message + ':')
            last_frame = self.frames[0]
            for frame in self.frames[1:]:
                try:
                    if last_frame:
                        tmp_op = last_frame['commands'][last_frame['current_step']]
                    else:
                        tmp_op = frame['commands'][0]
                    print(
                        '  in ' + tmp_op['file_path'] + ':' + str(tmp_op['line_number'])\
                        + ':\n\t' + tmp_op['str']
                    )
                except KeyError:
                    pass
                last_frame = frame
            print('  in ' + op['file_path'] + ':' + str(op['line_number']) + ':\n\t' + op['str'])
            if self.frames[1:]:
                print(error_type + ': ' + message + '.')
            try:
                self.defines['WEB_INITED']
                print('</pre>')
            except:
                pass
        sys.exit(1)

    def exec_func(self, func_body: list, with_frame=True, default_variables={}):
        """ Gets a list from commands and runs them as function or included script """
        old_dir = self.get_var('__dir__')
        old_file = self.get_var('__file__')
        # create new frame for this call
        if with_frame:
            frame_vars = dict(self.frames[0]['vars'])
            for k in self.all_vars():
                if k in ['argv', 'argc', '__file__', '__dir__', '__ismain__']:
                    frame_vars[k] = copy.deepcopy(self.get_var(k))
            imported_modules = []
        else:
            frame_vars = self.frames[-1]['vars']
            imported_modules = self.frames[-1]['imported_modules']

        for k in default_variables:
            frame_vars[k] = default_variables[k]
        if func_body:
            frame_vars['__file__'] = os.path.abspath(func_body[0]['file_path'])
            if os.path.isfile(frame_vars['__file__']):
                frame_vars['__dir__'] = os.path.dirname(frame_vars['__file__'])
        used_namespaces = []
        if not with_frame:
            used_namespaces = self.frames[-1]['used_namespaces']
        self.frames.append({
            'current_step': 0,
            'commands': func_body,
            'vars': frame_vars,
            'used_namespaces': used_namespaces,
            'imported_modules': imported_modules,
        })

        # run function
        self.start_frame()

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
            for used_namespace in self.frames[-1]['used_namespaces']:
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
            for used_namespace in self.frames[-1]['used_namespaces']:
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

    def eval(self, command, only_parse=False, dont_check_vars=False):
        """ Runs eval on command """
        if type(command) == str:
            result = lexer.parse_eval(command)
        else:
            result = command

        for i in range(0, len(result)):
            if result[i][0] == 'o':
                func_name = self.get_func_real_name(result[i][-1])
                if func_name != False:
                    result[i][-1] = 'self.functions["' + func_name + '"]'
                else:
                    class_name = self.get_class_real_name(result[i][-1])
                    if class_name != False:
                        result[i][-1] = 'self.classes["' + class_name + '"]'
                    else:
                        try:
                            self.defines[result[i][-1]]
                            result[i][-1] = 'self.defines["' + result[i][-1] + '"]'
                        except:
                            pass

        py_op = ''
        for item in result:
            if item[0] in ('n', 'o', 'v'):
                py_op += item[-1] + ' '
            else:
                py_op += item[-1]

        if only_parse:
            return py_op

        for item in result:
            if item[0] == 'v':
                self.variable_required(item[1])

        # set aliases
        true = True
        false = False
        null = None
        string = str
        integer = int
        array = list

        return eval(py_op)

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
        if self.current_func:
            if self.current_class:
                self.classes[self.current_class[-1]].__methods__[self.current_func[-1]].body.append(op)
            else:
                self.functions[self.current_func[-1]].body.append(op)
            return

        if op_name == 'endclass':
            self.run_endclass(op)
            return

        # list of commands
        commands_dict = {
            'func': self.run_func,
            'goto': self.run_goto,
            'gotoif': self.run_gotoif,
            'try': self.run_try,
            'endtry': self.run_endtry,
            'namespace': self.run_namespace,
            'ns': self.run_namespace,
            'endnamespace': self.run_endnamespace,
            'endns': self.run_endnamespace,
            'use': self.run_use,
            'class': self.run_class,
            'endclass': self.run_endclass,
            'return': self.run_return,
            'while': self.run_while,
            'endwhile': self.run_endwhile,
            'break': self.run_break,
            'continue': self.run_continue,
            '@doc': self.run_atdoc,
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
            if self.current_class:
                is_in_class = True
            parts = parser.split_by_equals(op['strings'])
            if len(parts) <= 1:
                if '->' in op['str'] or '(' in op['str'] or ')' in op['str']:
                    self.mem = self.eval(op['eval'])
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
                is_class_setting = self.eval('->' + is_class_setting, only_parse=True)[1:]
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

        parts = parser.split_by_equals(op['strings'])
        if len(parts) > 1:
            part1 = self.eval(parts[0], only_parse=True)
            part2 = self.eval(parts[1], only_parse=True)
            exec(part1 + ' = ' + part2)
            return

        # check function exists
        func_real_name = self.get_func_real_name(op_name)
        if func_real_name == False:
            self.mem = self.eval(op['eval'])
            return
        func_body = self.functions[func_real_name]

        # run function
        try:
            # execute function body
            if op_name in Function.BUILTIN_WITHOUT_FRAME_ISOLATION_FUNCTIONS:
                # put argument in the mem
                if op['args_str'] != '' and op['args_str'].strip() != '()':
                    if op['command'] == 'rmem':
                        self.eval(op['args_eval'])
                        return
                    else:
                        func_arg = self.eval(op['args_eval'])
                else:
                    func_arg = None
                self.mem = func_arg
                self.exec_func(func_body.body, False)
            else:
                args_str = op['args_str'].strip()
                if args_str:
                    if args_str[0] != '(':
                        args_str = '(' + args_str + ')'
                else:
                    args_str = '()'

                self.mem = self.eval(op['command'] + args_str)
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
        os.environ['PASHMAKPATH'] = '/usr/lib/pashmak_modules;' + home_directory + '/.local/lib/pashmak_modules;' + os.environ['PASHMAKPATH']
        pashmak_module_paths = os.environ['PASHMAKPATH']
        paths = pashmak_module_paths.strip().split(';')
        paths = [path.strip() for path in paths if path.strip() != '']
        self.module_path = paths

    def start_frame(self):
        """ Start running last frame """
        is_in_func = False
        self.frames[-1]['current_step'] = 0

        # load the labels
        i = 0
        while i < len(self.frames[-1]['commands']):
            current_op = self.frames[-1]['commands'][i]
            if current_op['command'] == 'label':
                if not is_in_func:
                    arg = current_op['args'][0]
                    self.labels[arg] = i+1
                    self.frames[-1]['commands'][i] = parser.parse('pass', filepath='<system>')[0]
            elif current_op['command'] == 'func':
                is_in_func = True
            elif current_op['command'] == 'endfunc':
                is_in_func = False
            i += 1

        while self.frames[-1]['current_step'] < len(self.frames[-1]['commands']):
            try:
                self.run(self.frames[-1]['commands'][self.frames[-1]['current_step']])
            except Exception as ex:
                try:
                    self.frames[-1]['commands'][self.frames[-1]['current_step']]
                except:
                    break
                if ex.__class__.__name__ == 'RecursionError':
                    msg = 'maximum recursion depth ' + str(len(self.frames)) + ' exceeded'
                else:
                    msg = str(ex)
                self.raise_error(
                    ex.__class__.__name__,
                    msg,
                    self.frames[-1]['commands'][self.frames[-1]['current_step']]
                )
            self.frames[-1]['current_step'] += 1

        if len(self.frames) > 1:
            self.frames.pop()
        else:
            # run shutdown events
            self.run_shutdown_events()

    def start(self):
        """ Start running the program """

        signal.signal(signal.SIGINT, self.signal_handler)

        self.bootstrap_modules()

        self.start_frame()
