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

script_content = '''
mem 'start\\n'; out ^;
mem 'touch /tmp/pashmak-test-created-file-<rand>'; system ^;
'''

script_content_b = '''
set $cmd; mem "touch /tmp/pashmak-test-created-file-<rand>"; copy $cmd;
system $cmd;
'''

script_content_c = '''
system $notfound;
'''

script_content_d = '''
system fgfdtyjgh;
'''

class test_system(TestCore):
    def run(self):
        rand = time.time()
        program_data = self.run_script(script_content.replace('<rand>' , str(rand)))
        self.assert_equals(program_data['output'] , 'start\n')
        self.assert_equals(program_data['mem'] , 0)
        self.assert_true(os.path.isfile('/tmp/pashmak-test-created-file-' + str(rand)))
        os.remove('/tmp/pashmak-test-created-file-' + str(rand))

        rand = time.time()
        program_data = self.run_script(script_content_b.replace('<rand>' , str(rand)))
        self.assert_true(os.path.isfile('/tmp/pashmak-test-created-file-' + str(rand)))
        os.remove('/tmp/pashmak-test-created-file-' + str(rand))

        program_data = self.run_script(script_content_c)
        self.assert_not_equals(program_data['runtime_error'] , None)

        program_data = self.run_script(script_content_d)
        self.assert_not_equals(program_data['runtime_error'] , None)




