#
# test_copy.py
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

class test_copy(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_vars(self.run_without_error('''
            set $name $family $age;
            mem 'parsa'; copy $name;
            copy $name $family;
        '''), {
            'name': 'parsa',
            'family': 'parsa',
            'age': None
        })
