#
# test_arraypush.py
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

class test_arraypush(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_vars(self.run_without_error('''
            set $names;
            mem ['pashmak', 'parsa']; copy $names;

            mem 'newname'; arraypush $names ^;
        '''), {'names': [
            'pashmak', 'parsa', 'newname'
        ]})

        self.assert_vars(self.run_without_error('''
            set $names;
            mem ['pashmak', 'parsa']; copy $names;

            set $new_item; mem 'newname'; copy $new_item;
            arraypush $names $new_item;

            free $new_item;
        '''), {'names': [
            'pashmak', 'parsa', 'newname'
        ]})
