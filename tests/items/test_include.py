# test_include.py
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
mem 'before include\\n'; out ^;

mem 'examples/will_be_include.pashm'; include ^;

mem 'after include\\n'; out ^;

call testalias;
'''

script_content_b = '''
set $path;
mem 'examples/will_be_include.pashm'; copy $path;
include $path;
'''

script_content_c = '''
include $not_found;
'''

script_content_d = '''
include hhghgjghj;
'''

class test_include(TestCore):
    def run(self):
        program_data = self.run_script(script_content)
        self.assert_equals(program_data['output'] , 'before include\ni am included\nafter include\ni am included alias\n')
        self.assert_equals(program_data['vars'] , {'included_var': 'included value'})

        program_data = self.run_script(script_content_b)
        self.assert_equals(program_data['output'] , 'i am included\n')

        program_error = self.run_script(script_content_c)['runtime_error']
        self.assert_not_equals(program_error , None)

        program_error = self.run_script(script_content_d)['runtime_error']
        self.assert_not_equals(program_error , None)

