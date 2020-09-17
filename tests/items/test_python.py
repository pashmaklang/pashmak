# test_python.py
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
mem "self.variables['myvar'] = 'the value'"; python ^;
'''

script_content_b = '''
set $code;
mem "self.variables['myvar'] = 'the value'"; copy $code;
python $code;
'''

script_content_c = '''
python $not_found;
'''

script_content_d = '''
python ffgdhfghf;
'''

class test_python(TestCore):
    def run(self):
        program_data = self.run_script(script_content)
        self.assert_equals(program_data['vars']['myvar'] , 'the value')

        program_data = self.run_script(script_content_b)
        self.assert_equals(program_data['vars']['myvar'] , 'the value')

        program_error = self.run_script(script_content_c)['runtime_error']
        self.assert_not_equals(program_error , None)

        program_error = self.run_script(script_content_d)['runtime_error']
        self.assert_not_equals(program_error , None)

