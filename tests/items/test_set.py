# test_set.py
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

script_content = '''
set $myvar;
set $var1 $var2;
set $v3 $aaa $hoho;
set $var1;
'''

script_content_b = '''
set $myvar; mem 'hello'; copy $myvar;

out $myvar;

set $myvar;

out $myvar;
'''

script_content_c = '''
# syntax error
set $aaa gghg;
'''

class test_set(TestCore):
    def run(self):
        program_vars = self.run_script(script_content)['vars']

        self.assert_equals(program_vars , {
            'myvar': None,
            'var1': None,
            'var2': None,
            'v3': None,
            'aaa': None,
            'hoho': None,
        })

        program_output = self.run_script(script_content_b)['output']
        self.assert_equals(program_output , 'hellohello')

        program_error = self.run_script(script_content_c)['runtime_error']
        self.assert_not_equals(program_error , None)
