#
# test_fread.py
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

'''

class test_fread(TestCore):
    def run(self):
        rand = str(time.time())
        f = open('/tmp/pashmak-test-file-' + rand , 'w')
        f.write('hello world')
        f.close()
        
        self.assert_output(self.run_script_without_error(''' mem '/tmp/pashmak-test-file-<rand>'; fread ^; out ^; '''.replace('<rand>' , rand)) , 'hello world')

        os.remove('/tmp/pashmak-test-file-' + rand)
