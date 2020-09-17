# test_read.py
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

script_content = '''
set $input;
read $input;
out $input;
'''

script_content_b = '''
set $input;
read $input;
out $input;

set $input_1;
read $input_1;
out $input_1;
'''

script_content_c = '''
set $a $b;
read $a $b;
'''

script_content_d = '''
read ^;
'''

script_content_e = '''
set $var;
read ^ $var;
'''

script_content_f = '''
read;
'''

script_content_g = '''
read $notfound;
'''

script_content_h = '''
read hgfjgky;
'''

class test_read(TestCore):
    def run(self):
        program_data = self.run_script(script_content , ['pashmak'])
        self.assert_equals(program_data['output'] , 'pashmak')
        self.assert_equals(program_data['vars'] , {'input': 'pashmak'})

        program_data = self.run_script(script_content_b , ['pashmak' , 'parsa'])
        self.assert_equals(program_data['output'] , 'pashmakparsa')
        self.assert_equals(program_data['vars'] , {'input': 'pashmak' , 'input_1': 'parsa'})

        program_data = self.run_script(script_content_c , ['pashmak' , 'parsa'])
        self.assert_equals(program_data['vars'] , {'a': 'pashmak' , 'b': 'parsa'})

        program_mem = self.run_script(script_content_d , ['pashmak'])['mem']
        self.assert_equals(program_mem , 'pashmak')

        program_data = self.run_script(script_content_e , ['themem' , 'pashmak'])
        self.assert_equals(program_data['mem'] , 'themem')
        self.assert_equals(program_data['vars']['var'] , 'pashmak')

        program_data = self.run_script(script_content_f , ['temp'])
        self.assert_equals(program_data['runtime_error'] , None)

        program_data = self.run_script(script_content_g , ['temp'])
        self.assert_not_equals(program_data['runtime_error'] , None)

        program_data = self.run_script(script_content_h , ['temp'])
        self.assert_not_equals(program_data['runtime_error'] , None)

