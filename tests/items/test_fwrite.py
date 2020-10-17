#
# test_fwrite.py
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

class test_fwrite(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        rand = str(random.random())
        self.run_without_error('''
            set $value; mem 'hello world'; copy $value;
            mem "''' + tempfile.gettempdir().replace('\\', '/') + '/' + '''pashmak-test-file-<rand>"; fwrite ^ $value;
        '''.replace('<rand>', rand))

        f_content = open(tempfile.gettempdir() + '/' + 'pashmak-test-file-' + rand, 'r').read()
        self.assert_equals(f_content, 'hello world')

        os.remove(tempfile.gettempdir() + '/' + 'pashmak-test-file-' + rand)
