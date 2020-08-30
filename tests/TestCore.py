# TestCore.py
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

import tcolor

from syntax import parser
from core import program

class TestCore:
    def __init__(self):
        pass

    def run_script_file(self , file_path , read_inputs=[]):
        f = open(file_path , 'r')
        content = f.read()
        f.close()
        return self.run_script(content , read_inputs)

    def run_script(self , script_content , read_inputs=[]):
        script_operations = parser.parse(script_content)
        prog = program.Program(is_test=True)
        prog.read_data = read_inputs
        prog.set_operations(script_operations)
        try:
            prog.start()
        except:
            print(tcolor.FAIL + 'Program runtime error')
            raise
        
        out = {}
        out['vars'] = prog.variables
        out['output'] = prog.output
        out['runtime_error'] = prog.runtime_error
        out['mem'] = prog.mem
        try:
            out['exit_code'] = prog.exit_code
        except:
            out['exit_code'] = 0

        return out

    def dump(self , obj):
        import pprint
        pprint.pprint(obj)
        sys.exit()

    def do_assert(self , value , error=''):
        try:
            assert value
        except:
            print(tcolor.FAIL + '\nAssert Error: ' + error)
            raise
            sys.exit(1)

    def assert_true(self , value):
        self.do_assert(value , 'asserting that false is true')

    def assert_false(self , value):
        self.do_assert((not value) , 'asserting that true is false')

    def assert_equals(self , first , last):
        self.do_assert((first == last) , '"' + str(first) + '" is not equals "' + str(last) + '"')

    def assert_not_equals(self , first , last):
        self.do_assert((not first == last) , '"' + str(first) + '" is equals "' + str(last) + '"')