# test_alias.py
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

mem 'starting\\n'; out ^;

alias myalias;
    mem 'alias runed\\n'; out ^;
    set $somevar; mem 20; copy $somevar;
    mem 'alias finished\\n'; out ^;
endalias;

call myalias;

mem 'finished\\n'; out ^;

call myalias;

'''

class test_alias(TestCore):
    def run(self):
        program_data = self.run_script(script_content)

        self.assert_equals(program_data['vars'] , {'somevar': 20})

        self.assert_equals(program_data['output'] , 'starting\nalias runed\nalias finished\nfinished\nalias runed\nalias finished\n')

