# TestCore.py
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

from tests import tcolor

class TestCore:
    def __init__(self):
        pass

    def do_assert(self , value , error=''):
        try:
            assert value
        except:
            print(tcolor.FAIL + '\nAssert Error: ' + error)
            raise

    def assert_true(self , value):
        self.do_assert(value , 'asserting that false is true')

    def assert_false(self , value):
        self.do_assert((not value) , 'asserting that true is false')

    def assert_equals(self , first , last):
        self.do_assert((first == last) , '"' + str(first) + '" is not equals "' + str(last) + '"')

    def assert_not_equals(self , first , last):
        self.do_assert((not first == last) , '"' + str(first) + '" is not equals "' + str(last) + '"')