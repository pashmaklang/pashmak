# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# test_out.py															#
#																		#
# the pashmak project                                                   #
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>                       #
#                                                                       #
# This file is part of pashmak.                                         #
#                                                                       #
# pashmak is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# pashmak is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##################################################

''' The test '''

from TestCore import TestCore

class test_out(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(self.run_without_error('''
            mem 'hi there'; out ^;
            mem 'hello world\\n'; out ^;
            set $name; mem 'pashmak'; copy $name;
            out $name;
        '''), 'hi therehello world\npashmak')

        self.assert_has_error(self.run_script(''' out $not_found_var; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' out; '''), 'ArgumentError')

        self.assert_has_error(self.run_script(''' out gdhfyyuy; '''))
