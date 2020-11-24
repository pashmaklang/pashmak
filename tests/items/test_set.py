#
# test_set.py
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

''' The test '''

from TestCore import TestCore

class test_set(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_vars(self.run_without_error('''
            set $myvar;
            set $var1 $var2;
            set $v3 $aaa $hoho;
            set $var1;
        '''), {
            'myvar': None,
            'var1': None,
            'var2': None,
            'v3': None,
            'aaa': None,
            'hoho': None,
        })

        self.assert_output(self.run_without_error('''
            set $myvar; mem 'hello'; copy $myvar;
            out $myvar; set $myvar; out $myvar;
        '''), 'hellohello')

        self.assert_has_error(self.run_script(''' set $aaa gghg; '''), 'SyntaxError')

        # tests for new variable value assigning way
        self.assert_vars(self.run_without_error('''
            $myvar = 'the value';
        '''), {
            'myvar': 'the value',
        })

        self.assert_vars(self.run_without_error('''
            $myvar;
        '''), {
            'myvar': None,
        })

        self.assert_output(self.run_without_error('''
            $name = 'parsa';
            $msg = 'hello ' + $name + '\\n';
            out $msg;
        '''), 'hello parsa\n')

        self.assert_output(self.run_without_error('''
            $myvar = 'num is ' + str(2*5);
            out $myvar;
        '''), 'num is 10')

        self.assert_output(self.run_without_error('''
            mem 'hello world';
            $myvar = ^;
            out $myvar;
        '''), 'hello world')

        self.assert_output(self.run_without_error('''
            mem 'hello world';
            $myvar =    ^ ;
            out $myvar;
        '''), 'hello world')

        self.assert_output(self.run_without_error('''
            func get_data;
                mem 'hi';
            endfunc;

            $var = ^ get_data;
            println $var;
        '''), 'hi\n')

        self.assert_output(self.run_without_error('''
            func say_hello;
                $name = ^;
                mem 'hello ' + $name;
            endfunc;

            $msg = ^ say_hello "parsa";
            println $msg;
        '''), 'hello parsa\n')
