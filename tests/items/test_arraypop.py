#
# test_arraypop.py
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

''' The test '''

from TestCore import TestCore

class test_arraypop(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_vars(self.run_without_error('''
            set $names;
            mem ['pashmak', 'parsa']; copy $names;

            mem 1; arraypop $names ^;
        '''),
        {'names': [
            'pashmak'
        ]})

        self.assert_vars(self.run_without_error('''
            set $names;
            mem ['pashmak', 'parsa']; copy $names;

            set $index; mem 1; copy $index;
            arraypop $names $index;

            free $index;
        '''),
        {'names': [
            'pashmak'
        ]})
