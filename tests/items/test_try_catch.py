# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# test_try_catch.py															#
#																		#
# the pashmak project                                                   #
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>                       #
#                                                                       #
# This file is part of pashmak.                                         #
#                                                                       #
# pashmak is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# pashmak is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##################################################

''' The test '''

from TestCore import TestCore

script_content = '''
set $name; mem 'pashmak'; copy $name;

try 10;
# a code without error
mem 'hello ' + $name; out ^;
endtry;

goto 20;

section 10;

mem 'the Error!'; out ^;

section 20;
'''

script_content_b = '''
try 10;
# a code with error
out $notfound;
endtry;

goto 20;

section 10;

mem 'the Error'; out ^;
goto 30;

section 20;

mem 'without error'; out ^;

section 30;
'''

script_content_c = '''
try 10;
# a code with error
mmdgfgdhgfhjh;
endtry;

goto 20;

section 10;

set $ex; copy $ex;
mem $ex['type'] + ':' + $ex['message']; out ^;
goto 30;

section 20;

mem 'without error'; out ^;

section 30;
'''

class test_try_catch(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(self.run_script(script_content, stop_after_error=False), 'hello pashmak')

        self.assert_output(self.run_script(script_content_b, stop_after_error=False), 'the Error')

        self.assert_output(
            self.run_script(script_content_c, stop_after_error=False),
            'SyntaxError:undefined operation "mmdgfgdhgfhjh"'
        )

        self.assert_has_error(
            self.run_script(''' try; gfdhghgfhf; endtry; ''', stop_after_error=False),
            'SyntaxError'
        )

        self.assert_has_error(
            self.run_script(''' try somesection; gfdhghgfhf; endtry; ''', stop_after_error=False),
            'RuntimeError'
        )
