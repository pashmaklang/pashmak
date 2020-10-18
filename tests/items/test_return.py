#
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

''' The test '''

from TestCore import TestCore

class test_return(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        program = self.run_without_error('''
            mem 'first'; out ^;
            return;
            mem 'last'; out ^;
        ''')
        self.assert_output(program, 'first')
        self.assert_exit_code(program, 0)

        program = self.run_without_error('''
            mem 'first'; out ^;
            return 126;
            mem 'last'; out ^;
        ''')
        self.assert_output(program, 'first')
        self.assert_exit_code(program, 126)

        self.assert_exit_code(self.run_without_error(''' mem 126; return ^; '''), 126)

        self.assert_exit_code(self.run_without_error(''' set $exitcode; mem 126; copy $exitcode; return $exitcode; '''), 126)

        self.assert_has_error(self.run_script(''' return $notfound; '''), 'TypeError')

        self.assert_has_error(self.run_script(''' return fgfdgdg; '''), 'TypeError')
