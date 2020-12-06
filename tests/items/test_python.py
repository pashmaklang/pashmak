#
# test_python.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of Pashmak.
#
# Pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pashmak.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################

''' The test '''

from TestCore import TestCore

class test_python(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_equals(self.run_without_error('''
            mem "self.all_vars()['myvar'] = 'the value'"; python ^;
        ''')['vars']['myvar'], 'the value')

        self.assert_equals(self.run_script('''
            set $code;
            mem "self.all_vars()['myvar'] = 'the value'"; copy $code;
            python $code;
        ''')['vars']['myvar'], 'the value')

        self.assert_has_error(self.run_script(''' python $not_found; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' python ffgdhfghf; '''))
