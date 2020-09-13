# test_return.py
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
mem 'first'; out ^;

return;

mem 'last'; out ^;
'''

script_content_b = '''
mem 'first'; out ^;

return 126;

mem 'last'; out ^;
'''

class test_return(TestCore):
    def run(self):
        program_data = self.run_script(script_content)

        self.assert_equals(program_data['output'] , 'first')
        self.assert_equals(program_data['exit_code'] , 0)

        # next script

        program_data = self.run_script(script_content_b)

        self.assert_equals(program_data['output'] , 'first')
        self.assert_equals(program_data['exit_code'] , 126)

