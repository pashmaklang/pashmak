# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# test_isset.py															#
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

class test_isset(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_mem(self.run_without_error(''' set $var; isset $var; '''), True)

        self.assert_mem(self.run_without_error(''' isset $var; '''), False)

        self.assert_mem(self.run_without_error(''' set $two; isset $two $one; '''), False)

        self.assert_mem(self.run_without_error(''' set $two $one; isset $two $one; '''), True)
