#
# test_args.py
#
# The Pashmak Project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
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

class test_args(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        program = self.run_without_error('''
            mem $argv[0]; out ^;
            mem $argv[1]; out ^;
            out $argc;
        ''', [], ['hi', 'bye'], True)
        self.assert_equals(program['vars']['argv'][0], 'hi')
        self.assert_equals(program['vars']['argv'][1], 'bye')
        self.assert_output(program, 'hibye2')
