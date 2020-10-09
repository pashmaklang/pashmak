#
# test_include.py
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

from TestCore import TestCore

import hashlib

class test_include(TestCore):
    def run(self):
        program = self.run_without_error('''
            mem 'before include\\n'; out ^;
            mem 'examples/will_be_include.pashm'; include ^;
            mem 'after include\\n'; out ^;
            testfunc;
        ''')
        self.assert_output(program, 'before include\ni am included\nafter include\ni am included func\n')
        self.assert_vars(program, {'included_var': 'included value'})

        self.assert_output(self.run_without_error('''
            set $path;
            mem 'examples/will_be_include.pashm'; copy $path;
            include $path;
        '''), 'i am included\n')

        self.assert_has_error(self.run_script(''' include $not_found; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' include hhghgjghj; '''))

        self.assert_output(self.run_without_error('''
            mem '@hash'; include ^;
            hash.sha256 'hello'; out ^;
        '''), hashlib.sha256('hello'.encode()).hexdigest())

        self.assert_has_error(self.run_script(''' mem '@notfound233445'; include ^; '''), 'ModuleError')
