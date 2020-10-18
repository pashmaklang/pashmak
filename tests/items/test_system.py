#
# test_system.py
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

import random
import os
import tempfile
from TestCore import TestCore

class test_system(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        rand = random.random()
        program = self.run_without_error('''
            mem 'start\\n'; out ^;
            mem 'touch ''' + tempfile.gettempdir().replace('\\', '/') + '/' + '''pashmak-test-created-file-<rand>'; system ^;
        '''.replace('<rand>', str(rand)))
        self.assert_output(program, 'start\n')
        self.assert_mem(program, 0)
        self.assert_true(os.path.isfile(tempfile.gettempdir() + '/' + 'pashmak-test-created-file-' + str(rand)))
        os.remove(tempfile.gettempdir() + '/' + 'pashmak-test-created-file-' + str(rand))

        rand = random.random()
        self.run_without_error(''' set $cmd; mem "touch ''' + tempfile.gettempdir().replace('\\', '/') + '/' + '''pashmak-test-created-file-<rand>"; copy $cmd; system $cmd; '''.replace('<rand>', str(rand)))
        self.assert_true(os.path.isfile(tempfile.gettempdir() + '/' + 'pashmak-test-created-file-' + str(rand)))
        os.remove(tempfile.gettempdir() + '/' + 'pashmak-test-created-file-' + str(rand))

        self.assert_has_error(self.run_script(''' system $notfound; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' system fgfdtyjgh; '''))
