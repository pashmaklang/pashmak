#
# test_alias.py
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

class test_alias(TestCore):
    def run(self):
        program = self.run_without_error('''
            mem 'starting\\n'; out ^;

            alias myalias;
                mem 'alias runed\\n'; out ^;
                set $somevar; mem 20; copy $somevar;
                mem 'alias finished\\n'; out ^;
            endalias;

            call myalias;

            mem 'finished\\n'; out ^;

            set $alias_name; mem 'myalias'; copy $alias_name;
            call $alias_name;

            mem 'myalias'; call ^;
        ''')
        self.assert_vars(program , {'somevar': 20 , 'alias_name': 'myalias'})
        self.assert_output(program , 'starting\nalias runed\nalias finished\nfinished\nalias runed\nalias finished\nalias runed\nalias finished\n')

        self.assert_has_error(self.run_script(''' call undefined_alias; '''))

        self.assert_has_error(self.run_script(''' call $not_found; '''))

        self.assert_output(self.run_without_error('''
            alias myalias;
            mem 'alias runed\\n'; out ^;
            endalias;
            
            myalias;
        ''') , 'alias runed\n')

        self.assert_output(self.run_without_error('''
            alias myalias;
                out ^;
            endalias;
            
            myalias "hello world";
        ''') , 'hello world')

        self.assert_output(self.run_without_error('''
            alias myalias;
                out ^;
            endalias;
            
            myalias 2*3;
        ''') , '6')

        self.assert_output(self.run_without_error('''
            alias myalias;
                out ^;
            endalias;

            set $var;
            mem 'test'; copy $var;
            
            myalias 'this is ' + $var;
        ''') , 'this is test')

        self.assert_has_error(self.run_script('''
            alias myalias;
                out ^;
            endalias;
            
            myalias hello world;
        '''))

