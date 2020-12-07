#
# run_pashmt.py
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

''' Runs tests '''

import sys
import os
from random import shuffle

# add `src/` folder to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'src')

import tcolor
from TestCore import TestCore

class TestRunner:
    ''' Test runner '''
    def __init__(self):
        self.tests = []
        self.load_tests('tests')
        shuffle(self.tests)

    def load_tests(self, path):
        ''' Loads .pashmt tests '''
        for f in os.listdir(path):
            if os.path.isdir(path + '/' + f):
                self.load_tests(path + '/' + f)
            elif os.path.isfile(path + '/' + f):
                if f[len(f)-7:] == '.pashmt':
                    self.tests.append(path + '/' + f)

    def run_once(self, test: str):
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

        print(sections['test'].strip() + ' (' + test.strip().replace('\n', ' ').strip() + ')', end='', flush=True)

        # run the test
        read_inputs = []
        cli_args = []

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

        core = TestCore()
        result = core.run_script(sections['file'], read_inputs, cli_args)

        # run assertions on result
        with_error = False
        try:
            sections['with-error']
            with_error = True
        except:
            pass
        if with_error:
            core.assert_has_error(result)
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

        print(tcolor.OKGREEN + ' PASS' + tcolor.ENDC)

    def run(self):
        ''' Start running tests '''
        print()
        print('Starting testing system...')
        print('--------------------------')

        for test in self.tests:
            self.run_once(test)

        print()
        print(
            tcolor.OKGREEN +\
            'All ' + str(len(self.tests)) +\
            ' tests passed successfuly' +\
            tcolor.ENDC
        )
        print()

if __name__ == '__main__':
    test_runner = TestRunner()
    test_runner.run()
