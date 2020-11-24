#
# test_stdlib.py
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

''' The test '''

import os
import tempfile
import platform
from TestCore import TestCore

class test_stdlib(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(self.run_without_error('''
        print "hello world";
        '''), 'hello world')

        self.assert_output(self.run_without_error('''
        println "hello world";
        '''), 'hello world\n')

        self.assert_output(self.run_without_error('''
        printl "hello world";
        '''), 'hello world\n')

        self.assert_output(self.run_without_error('''
        import "examples''' + '/' + '''will_be_include.pashm";
        '''), 'i am included\n')

        self.assert_exit_code(self.run_without_error('''
        exit 5;
        '''), 5)

        self.assert_exit_code(self.run_without_error('''
        exit;
        '''), 0)

        self.assert_mem(self.run_without_error('''
        py "self.mem = 'hi'";
        '''), 'hi')

        cwd = os.getcwd()
        self.run_without_error('''
        std.chdir "''' + tempfile.gettempdir().replace('\\', '/') + '''";
        ''')
        self.assert_equals(os.getcwd(), tempfile.gettempdir())
        os.chdir(cwd)

        self.assert_output(self.run_without_error('''
        std.eval "mem 'output from eval'\\; out ^\\;";
        '''), 'output from eval')

        self.assert_output(self.run_without_error('''
        set $name;
        mem 'parsa'; copy $name;
        print 'hello ' + $name;
        '''), 'hello parsa')

        self.assert_output(self.run_without_error('''
        print str(2*2) + ' is sum';
        '''), '4 is sum')

        self.assert_has_error(self.run_script('''
        print 'hello ' + $name;
        '''), 'RuntimeError')

        program = self.run_script('''
        raise ['SomeError', 'this is error'];
        ''')
        self.assert_has_error(program, 'SomeError')
        self.assert_equals(program['runtime_error']['type'], 'SomeError')
        self.assert_equals(program['runtime_error']['message'], 'this is error')

        self.assert_has_error(self.run_script('''
        assert 2 == 3;
        '''), 'AssertError')

        self.assert_has_error(self.run_script('''
        assert 1 > 10;
        '''), 'AssertError')

        self.assert_has_error(self.run_script('''
        assert False;
        '''), 'AssertError')

        self.assert_has_error(self.run_script('''
        set $age; mem 18; copy $age;
        assert $age > 30;
        '''), 'AssertError')

        self.run_without_error('''
        assert True;
        ''')

        self.run_without_error('''
        assert 2 == 2;
        ''')

        self.run_without_error('''
        assert 10 > 5;
        ''')

        self.run_without_error('''
        set $age; mem 40; copy $age;
        assert $age > 30;
        ''')

        self.assert_output(self.run_without_error('''
        set $name; mem 'parsa\\n'; copy $name;

        func myfunc;
        	out $name;
        	gset ['name', 'pashmak\\n'];
        endfunc;

        myfunc;

        out $name;

        '''), 'parsa\npashmak\n')

        self.assert_output(self.run_without_error('''
        $i = 0;
        loop;
            println 'hello world';
            $i = $i + 1;
        while $i < 10;
        '''), 'hello world\n' * 10)
