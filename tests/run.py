#!/usr/bin/env python3
#
# run.py
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

''' Runs tests '''

import sys
import os
import time

# add `src/` folder to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'src')

from core import parser
from core import program
from core import modules

class Tcolor:
    ''' Terminal ansi colors '''
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
tcolor = Tcolor()

class TestCore:
    ''' Test core '''
    def __init__(self):
        self.is_test = True
        self.total_asserts = 0

    def with_program_errors(self):
        ''' Enable program error rendering '''
        self.is_test = False

    def run_without_error(self, script_content: str, read_inputs=None, args=None, want_argv=False, stop_after_error=True) -> dict:
        ''' Runs a script and auto assert without error '''
        if read_inputs is None:
            read_inputs = []
        if args is None:
            args = []
        prog = self.run_script(script_content, read_inputs, args, want_argv, stop_after_error)
        self.assert_has_not_error(prog)
        return prog

    def run_script(self, script_content: str, read_inputs=None, args=None, want_argv=False, stop_after_error=True) -> dict:
        ''' Runs a script and returns result '''
        if read_inputs is None:
            read_inputs = []
        if args is None:
            args = []
        script_commands = parser.parse(script_content, filepath='<test>')
        prog = program.Program(is_test=self.is_test, args=args)
        prog.stop_after_error = stop_after_error
        prog.read_data = read_inputs
        prog.set_commands(script_commands)
        prog.start()

        out = {}
        out['vars'] = prog.frames[-1]['vars']
        out['output'] = prog.output
        out['runtime_error'] = prog.runtime_error
        out['mem'] = prog.mem
        try:
            out['exit_code'] = prog.exit_code
        except:
            out['exit_code'] = 0

        del out['vars']['argc']

        if not want_argv:
            del out['vars']['argv']
        try:
            del out['vars']['__file__']
        except:
            pass
        try:
            del out['vars']['__dir__']
        except:
            pass
        try:
            del out['vars']['__ismain__']
        except:
            pass

        return out

    def dump(self, obj):
        ''' Dumps a object and stops testing '''
        import pprint
        pprint.pprint(obj)
        sys.exit()

    def do_assert(self, value, error=''):
        ''' Do assertion on value and show error for assert error '''
        self.total_asserts += 1
        try:
            assert value
        except AssertionError:
            print(tcolor.FAIL + '\nAssert Error: ' + error)
            raise

    def assert_true(self, value):
        ''' Assert true '''
        self.do_assert(value, 'asserting that false is true')

    def assert_false(self, value):
        ''' Assert false '''
        self.do_assert((not value), 'asserting that true is false')

    def assert_equals(self, first, last):
        ''' Assert equals '''
        self.do_assert((first == last), '"' + str(first) + '" is not equals "' + str(last) + '"')

    def assert_not_equals(self, first, last):
        ''' Assert not equals '''
        self.do_assert((not first == last), '"' + str(first) + '" is equals "' + str(last) + '"')

    def assert_vars(self, program_result, variables):
        ''' Assert vars '''
        self.assert_equals(program_result['vars'], variables)

    def assert_mem(self, program_result, mem):
        ''' Assert mem '''
        self.assert_equals(program_result['mem'], mem)

    def assert_output(self, program_result, output):
        ''' Assert output '''
        self.assert_equals(program_result['output'], output)

    def assert_exit_code(self, program_result, exit_code):
        ''' Assert exit code '''
        self.assert_equals(program_result['exit_code'], exit_code)

    def assert_has_error(self, program_result, error_type=None):
        ''' Assert equals '''
        self.assert_not_equals(program_result['runtime_error'], None)
        if error_type:
            self.assert_equals(program_result['runtime_error']['type'], error_type)

    def assert_has_not_error(self, program_result):
        ''' Assert has not error '''
        self.assert_equals(program_result['runtime_error'], None)

class TestRunner:
    ''' Test runner '''
    def __init__(self):
        self.tests = []
        self.load_tests('tests')
        self.tests.sort()
        self.default_classes = ['Object', 'Error']
        self.default_classes_list_str = ''
        for item in self.default_classes:
            self.default_classes_list_str += "'" + item + '\', '
        self.default_classes_list_str = self.default_classes_list_str.strip().strip(',')

    def load_tests(self, path):
        ''' Loads .pashmt tests '''
        for f in os.listdir(path):
            if os.path.isdir(path + '/' + f):
                self.load_tests(path + '/' + f)
            elif os.path.isfile(path + '/' + f):
                if f[len(f)-7:] == '.pashmt':
                    self.tests.append(path + '/' + f)

    def run_once(self, test: str, test_counter: int):
        ''' Run once test '''
        # read test file
        f = open(test, 'r')
        content = f.read()
        f.close()
        sections = {}
        lines = content.split('\n')
        current_section = None
        for line in lines:
            if line.strip()[:2] == '--' and line.strip()[len(line.strip())-2:] == '--':
                current_section = line[2:]
                current_section = current_section[:len(current_section)-2]
                sections[current_section] = ''
            elif current_section != None:
                sections[current_section] += line + '\n'

        try:
            sections['file']
        except:
            print(tcolor.WARNING + 'Warninig: test "' + test + '" has not section "file"' + tcolor.ENDC)
            return

        try:
            sections['test']
        except:
            print(tcolor.WARNING + 'Warninig: test "' + test + '" has not section "test"' + tcolor.ENDC)
            return

        print('\033[94m[' + str(test_counter) + '/' + str(len(self.tests)) + ']\033[0m ' + sections['test'].strip() + ' \033[93m(' + test.strip().replace('\n', ' ').strip() + ')\033[0m...', end='', flush=True)

        # run the test
        read_inputs = []
        cli_args = []
        is_skip = False
        try:
            sections['skip']
            is_skip = True
        except:
            pass

        try:
            sections['cliargs']
            cli_args = True
        except:
            pass
        if cli_args == True:
            cli_args = eval(sections['cliargs'])

        try:
            sections['stdin']
            read_inputs = True
        except:
            pass
        if read_inputs == True:
            read_inputs = eval(sections['stdin'])

        try:
            sections['pyinit']
            exec(sections['pyinit'])
        except:
            pass

        core = TestCore()
        result = core.run_script(sections['file'], read_inputs, cli_args)

        try:
        # run assertions on result
            with_error = False
            try:
                sections['with-error']
                with_error = True
            except:
                pass
            if with_error:
                try:
                    err_type = eval(sections['with-error'])
                except:
                    err_type = None
                core.assert_has_error(result, err_type)
            else:
                core.assert_has_not_error(result)

            variables = False
            try:
                sections['vars']
                variables = True
            except:
                pass
            if variables:
                core.assert_vars(result, eval(sections['vars']))
    
            mem = False
            try:
                sections['mem']
                mem = True
            except:
                pass
            if mem:
                core.assert_mem(result, eval(sections['mem']))
    
            output = False
            try:
                sections['output']
                output = True
            except:
                pass
            if output:
                core.assert_output(result, eval(sections['output']))

            exit_code = False
            try:
                sections['exit-code']
                exit_code = True
            except:
                pass
            if exit_code:
                core.assert_exit_code(result, eval(sections['exit-code']))
        except:
            if is_skip:
                print('\033[31mSkipped.\033[0m')
            else:
                raise

        print(tcolor.OKGREEN + ' PASS' + tcolor.ENDC)

    def run(self):
        ''' Start running tests '''
        print()
        print('Starting testing system...')
        print('--------------------------')

        start_time = time.time()
        default_modules = modules.modules
        test_counter = 1

        for test in self.tests:
            self.run_once(test, test_counter)
            modules.modules = default_modules
            test_counter += 1

        end_time = time.time()

        test_time = end_time - start_time

        print()
        print(
            tcolor.OKGREEN +\
            'All ' + str(len(self.tests)) +\
            ' tests passed successfuly in ' + str(test_time) + ' secounds' +\
            tcolor.ENDC
        )
        print()

if __name__ == '__main__':
    test_runner = TestRunner()
    test_runner.run()
