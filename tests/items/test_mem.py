# test_mem.py
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


from TestCore import TestCore

script_content = '''
mem 'some thing';
'''

script_content_b = '''
mem 155;
'''

script_content_c = '''
mem 'first' + 'last';
'''

script_content_d = '''
mem 100 > 50;
'''

script_content_e = '''
set $var; mem 'value'; copy $var;
mem $var + 'new';
'''

script_content_f = '''
mem (10 * 5) + 9;
'''

class test_mem(TestCore):
    def run(self):
        program_a = self.run_script(script_content)
        program_b = self.run_script(script_content_b)
        program_c = self.run_script(script_content_c)
        program_d = self.run_script(script_content_d)
        program_e = self.run_script(script_content_e)
        program_f = self.run_script(script_content_f)

        self.assert_equals(program_a['mem'] , 'some thing')
        self.assert_equals(program_b['mem'] , 155)
        self.assert_equals(program_c['mem'] , 'firstlast')
        self.assert_equals(program_d['mem'] , True)
        self.assert_equals(program_e['mem'] , 'valuenew')
        self.assert_equals(program_f['mem'] , 59)

