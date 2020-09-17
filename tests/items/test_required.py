# test_required.py
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
set $v1 $name $n;

required $v1 $name;
required $n;
'''

script_content_b = '''
set $v1 $name;

required $v1 $name;
required $n;
'''

script_content_c = '''
required ffdggd $sgdfg;
'''

class test_required(TestCore):
    def run(self):
        program_error = self.run_script(script_content)['runtime_error']
        self.assert_equals(program_error , None)

        program_error = self.run_script(script_content_b)['runtime_error']
        self.assert_not_equals(program_error , None)

        program_error = self.run_script(script_content_c)['runtime_error']
        self.assert_not_equals(program_error , None)
