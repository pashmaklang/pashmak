#
# TestCore.py
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

''' Test core '''

import sys
import tcolor
from syntax import parser
from core import program

class TestCore:
    ''' Test core '''

    def __init__(self):
        self.is_test = True
        self.total_asserts = 0

    def with_program_errors(self):
        ''' Enable program error rendering '''
        self.is_test = False

    def run_file(self, file_path: str, read_inputs=[]) -> dict:
        ''' Runs a script from file '''
        f = open(file_path, 'r')
        content = f.read()
        f.close()
        return self.run_script(content, read_inputs)

    def run_without_error(self, script_content: str, read_inputs=[], args=[], want_argv=False, stop_after_error=True) -> dict:
        ''' Runs a script and auto assert without error '''
        prog = self.run_script(script_content, read_inputs, args, want_argv, stop_after_error)
        self.assert_has_not_error(prog)
        return prog

    def run_script(self, script_content: str, read_inputs=[], args=[], want_argv=False, stop_after_error=True) -> dict:
        ''' Runs a script and returns result '''
        script_operations = parser.parse(script_content)
        prog = program.Program(is_test=self.is_test, args=args)
        prog.stop_after_error = stop_after_error
        prog.read_data = read_inputs
        prog.set_operations(script_operations)
        prog.start()

        out = {}
        out['vars'] = prog.variables
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
        del out['vars']['pashmakinfo']
        try:
            del out['vars']['__file__']
        except:
            pass
        try:
            del out['vars']['__dir__']
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
