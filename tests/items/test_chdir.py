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

import os

from TestCore import TestCore

class test_chdir(TestCore):
    def run(self):
        current_wd = os.getcwd()

        self.run_without_error(''' mem '/tmp'; chdir ^; ''')
        self.assert_equals(os.getcwd() , '/tmp')
        os.chdir(current_wd)

        self.run_without_error('''
            set $path; mem '/tmp'; copy $path;
            chdir $path;
        ''')
        self.assert_equals(os.getcwd() , '/tmp')
        os.chdir(current_wd)

        self.assert_has_error(self.run_script(''' mem '/gdghfjuyjfjhgjghjghj'; chdir ^; '''))
        os.chdir(current_wd)

        self.assert_has_error(self.run_script(''' chdir $notfound; '''))

        self.assert_has_error(self.run_script(''' chdir gfhhhrtryru; '''))
