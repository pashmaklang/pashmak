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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################


import time, os

from TestCore import TestCore

script_content = '''
set $value; mem 'hello world'; copy $value;
mem '/tmp/pashmak-test-file-<rand>'; fwrite ^ $value;
'''

class test_fwrite(TestCore):
    def run(self):
        rand = str(time.time())
        program_output = self.run_script(script_content.replace('<rand>' , rand))['output']

        f_content = open('/tmp/pashmak-test-file-' + rand , 'r').read()
        self.assert_equals(f_content , 'hello world')

        os.remove('/tmp/pashmak-test-file-' + rand)

