# test_chdir.py
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

import os

from TestCore import TestCore

script_content = '''
mem '/tmp'; chdir ^;
'''

script_content_b = '''
set $path; mem '/tmp'; copy $path;
chdir $path;
'''

script_content_c = '''
mem '/gdghfjuyjfjhgjghjghj'; chdir ^;
'''

class test_chdir(TestCore):
    def run(self):
        current_wd = os.getcwd()

        self.run_script(script_content)
        self.assert_equals(os.getcwd() , '/tmp')
        os.chdir(current_wd)

        self.run_script(script_content_b)
        self.assert_equals(os.getcwd() , '/tmp')
        os.chdir(current_wd)

        program_data = self.run_script(script_content_c)
        self.assert_not_equals(program_data['runtime_error'] , None)
        os.chdir(current_wd)

