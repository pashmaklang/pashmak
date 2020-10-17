#
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

''' The test '''

import os
import tempfile
from TestCore import TestCore

class test_chdir(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        current_wd = os.getcwd()
        self.run_without_error(''' mem "''' + tempfile.gettempdir().replace('\\', '/') + '''"; chdir ^; ''')
        self.assert_equals(os.getcwd(), tempfile.gettempdir())
        os.chdir(current_wd)

        self.run_without_error('''
            set $path; mem "''' + tempfile.gettempdir().replace('\\', '/') + '''"; copy $path;
            chdir $path;
        ''')
        self.assert_equals(os.getcwd(), tempfile.gettempdir())
        os.chdir(current_wd)

        self.assert_has_error(self.run_script(''' mem '/gdghfjuyjfjhgjghjghj'; chdir ^; '''), 'RuntimeError')
        os.chdir(current_wd)

        self.assert_has_error(self.run_script(''' chdir $notfound; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' chdir gfhhhrtryru; '''), 'VariableError')
