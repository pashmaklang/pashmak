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

import time, os

from TestCore import TestCore

class test_system(TestCore):
    def run(self):
        rand = time.time()
        program = self.run_without_error('''
            mem 'start\\n'; out ^;
            mem 'touch /tmp/pashmak-test-created-file-<rand>'; system ^;
        '''.replace('<rand>', str(rand)))
        self.assert_output(program, 'start\n')
        self.assert_mem(program, 0)
        self.assert_true(os.path.isfile('/tmp/pashmak-test-created-file-' + str(rand)))
        os.remove('/tmp/pashmak-test-created-file-' + str(rand))

        rand = time.time()
        self.run_without_error(''' set $cmd; mem "touch /tmp/pashmak-test-created-file-<rand>"; copy $cmd; system $cmd; '''.replace('<rand>', str(rand)))
        self.assert_true(os.path.isfile('/tmp/pashmak-test-created-file-' + str(rand)))
        os.remove('/tmp/pashmak-test-created-file-' + str(rand))

        self.assert_has_error(self.run_script(''' system $notfound; '''))

        self.assert_has_error(self.run_script(''' system fgfdtyjgh; '''))
