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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################


from TestCore import TestCore

script_content = '''
set %myvar;
set %var1 %var2;
set %v3 %aaa %hoho
set %var1;
'''

class test_set(TestCore):
    def run(self):
        program_vars = self.run_script(script_content)['vars']

        try:
            self.assert_equals(program_vars['myvar'] , None)
            self.assert_equals(program_vars['var1'] , None)
            self.assert_equals(program_vars['var2'] , None)
            self.assert_equals(program_vars['v3'] , None)
            self.assert_equals(program_vars['aaa'] , None)
            self.assert_equals(program_vars['hoho'] , None)
        except:
            self.assert_true(False)
