#
# test_function.py
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

from TestCore import TestCore

class test_function(TestCore):
    def run(self):
        program = self.run_without_error('''
            mem 'starting\\n'; out ^;

            func myfunc;
                mem 'func runed\\n'; out ^;
                mem 'func finished\\n'; out ^;
            endfunc;

            myfunc;

            mem 'finished\\n'; out ^;
        ''')
        self.assert_output(program, 'starting\nfunc runed\nfunc finished\nfinished\n')

        self.assert_has_error(self.run_script(''' undefined_func; '''), 'SyntaxError')

        self.assert_output(self.run_without_error('''
            func myfunc;
                mem 'func runed\\n'; out ^;
            endfunc;
            
            myfunc;
        '''), 'func runed\n')

        self.assert_output(self.run_without_error('''
            func myfunc;
                out ^;
            endfunc;
            
            myfunc "hello world";
        '''), 'hello world')

        self.assert_output(self.run_without_error('''
            func myfunc;
                out ^;
            endfunc;
            
            myfunc 2*3;
        '''), '6')

        self.assert_output(self.run_without_error('''
            func myfunc;
                out ^;
            endfunc;

            set $var;
            mem 'test'; copy $var;
            
            myfunc 'this is ' + $var;
        '''), 'this is test')

        self.assert_has_error(self.run_script('''
            func myfunc;
                out ^;
            endfunc;
            
            myfunc hello world;
        '''), 'RuntimeError')

        self.assert_output(self.run_without_error('''
        set $n; mem 'parsa\\n'; copy $n;

        func myfunc;
            out $n;
            set $n; mem 'myfunc\\n'; copy $n;
            out $n;
        endfunc;

        func tststs;
            out $n;
            set $n; mem 'tststs\\n'; copy $n;
            myfunc;
            out $n;
        endfunc;

        out $n;
        tststs;
        out $n;
        '''), 'parsa\nparsa\nparsa\nmyfunc\ntststs\nparsa\n')

        self.assert_has_error(self.run_script('''
        func myfunc;
            print 'hello\n';
        endfunc;

        func myfunc;
            print 'something\n';
        endfunc;
        '''), 'FunctionError')

        self.assert_output(self.run_without_error('''
        func say_hi $name;
            println $name;
        endfunc;

        say_hi 'parsa';
        '''), 'parsa\n')

        self.assert_output(self.run_without_error('''
        func say_hi ($name);
            println $name;
        endfunc;

        say_hi 'parsa';
        '''), 'parsa\n')
