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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################

from TestCore import TestCore

script_content = '''
set %myvar; mem 'hello'; copy %myvar;
mem "self.variables['myvar']"; python ^;
out ^;
'''

script_content_b = '''
set %myvar; mem 'hello'; copy %myvar;
set %code;
mem "self.variables['myvar']"; copy %code;
python %code;
out ^;
'''

class test_python(TestCore):
    def run(self):
        program_output = self.run_script(script_content)['output']
        self.assert_equals(program_output , 'hello')

        program_output = self.run_script(script_content_b)['output']
        self.assert_equals(program_output , 'hello')

