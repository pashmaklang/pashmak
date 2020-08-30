# run.py
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


import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

import tcolor

class TestRunner:
    def __init__(self):
        files = os.listdir('tests/items')
        self.tests = []
        for f in files:
            if f[len(f)-3:] == '.py':
                self.tests.append(f)

    def run_once(self , test):
        test_class_name = test[:len(test)-3]
        loaded_test = __import__('items.' + test_class_name)
        test_obj = eval('loaded_test.' + test_class_name + '.' + test_class_name + '()')
        print(test_class_name.replace('_' , ' ') + ': ' , end='' , flush=True)
        test_obj.run()
        print(tcolor.OKGREEN + 'PASS' + tcolor.ENDC)

    def run(self):
        for test in self.tests:
            self.run_once(test)





test_runner = TestRunner()
test_runner.run()



