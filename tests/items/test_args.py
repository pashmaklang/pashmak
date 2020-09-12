# test_args.py
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


from TestCore import TestCore

script_content = '''
mem $argv[0]; out ^;
mem $argv[1]; out ^;
out $argc;
'''

class test_args(TestCore):
    def run(self):
        program_data = self.run_script(script_content , [] , ['hi' , 'bye'] , True)
        self.assert_equals(program_data['vars']['argv'][0] , 'hi')
        self.assert_equals(program_data['vars']['argv'][1] , 'bye')
        self.assert_equals(program_data['output'] , 'hibye2')

