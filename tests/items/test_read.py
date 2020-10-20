#
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

''' The test '''

from TestCore import TestCore

class test_read(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        program = self.run_without_error(''' set $input; read $input; out $input; ''', ['pashmak'])
        self.assert_output(program, 'pashmak')
        self.assert_vars(program, {'input': 'pashmak'})

        program = self.run_without_error('''
            set $input;
            read $input;
            out $input;

            set $input_1;
            read $input_1;
            out $input_1;
        ''', ['pashmak', 'parsa'])
        self.assert_output(program, 'pashmakparsa')
        self.assert_vars(program, {'input': 'pashmak', 'input_1': 'parsa'})

        self.assert_vars(
            self.run_without_error(
                ''' set $a $b; read $a $b; ''', ['pashmak', 'parsa']
            ),
            {'a': 'pashmak', 'b': 'parsa'}
        )

        self.assert_mem(self.run_without_error(''' read ^; ''', ['pashmak']), 'pashmak')

        program = self.run_without_error(''' set $var; read ^ $var; ''', ['themem', 'pashmak'])
        self.assert_mem(program, 'themem')
        self.assert_equals(program['vars']['var'], 'pashmak')

        self.assert_has_not_error(self.run_script(''' read; ''', ['temp']))

        self.assert_has_error(self.run_script(''' read $notfound; ''', ['temp']), 'VariableError')

        self.assert_has_error(self.run_script(''' read hgfjgky; ''', ['temp']), 'SyntaxError')
