#
# test_modules.py
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

import random
import os
import tempfile
from TestCore import TestCore

class test_modules(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''

        tmp_file = tempfile.gettempdir().replace('\\', '/') + '/' + 'pashmak-test-file-' + str(random.random())
        self.assert_output(self.run_without_error('''
        import '@file';

        file.open ["''' + tmp_file + '''", 'w'];
        set $file; copy $file;
        file.write [$file, "content of file"];
        file.close $file;

        file.open ["''' + tmp_file + '''", 'r'];
        copy $file;
        file.read $file; out ^;
        '''), 'content of file')

        try:
            os.remove(tmp_file)
        except:
            pass
