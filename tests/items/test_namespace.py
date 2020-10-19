# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# test_namespace.py															#
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

class test_namespace(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(self.run_without_error('''
        namespace MySpace;
            func dosomething;
                print 'hello world\\n';
            endfunc;

            MySpace.dosomething;
            dosomething;
        endnamespace;

        MySpace.dosomething;
        '''), 'hello world\nhello world\nhello world\n')

        self.assert_output(self.run_without_error('''
        namespace MySpace;
            func dosomething;
                print 'hello world\\n';
            endfunc;

            MySpace.dosomething;
            dosomething;
        endns;

        MySpace.dosomething;
        '''), 'hello world\nhello world\nhello world\n')

        self.assert_output(self.run_without_error('''
            namespace App;
                func dosomething;
                    print 'hello world\\n';
                endfunc;
                set $name; mem 'the app'; copy $name;
            endns;

            namespace Second;
                func hello;
                    print 'hello\\n';
                endfunc;

                set $test; mem 'the second'; copy $test;
            endns;

            App.dosomething;
            Second.hello;

            out $App.name;
            out $Second.test;

            use App;
            use Second;

            App.dosomething;
            dosomething;
            Second.hello;
            hello;

            out $App.name;
            out $Second.test;

            out $name;
            out $test;

            '''),
            'hello world\nhello\nthe appthe secondhello world\nhello world\nhello\nhello\nthe appthe secondthe appthe second'
        )

        self.assert_output(self.run_without_error('''
        namespace App;
            set $name; mem 'parsa'; copy $name;
            out $name;
        endns;

        out $App.name
        '''), 'parsaparsa')

        self.assert_output(self.run_without_error('''
        namespace App;
            set $name; mem 'parsa'; copy $name;
            out $name;
            out $App.name;
        endns;

        out $App.name;
        '''), 'parsaparsaparsa')

        self.assert_has_error(self.run_script('''
        namespace App;
            set $name; mem 'parsa'; copy $name;
        endns;

        out $name;
        '''), 'VariableError')

        self.assert_output(self.run_without_error('''
        namespace App;
            $name = 'parsa';
            out $name;
            out $App.name;

            func dosomething;
                print 'doing';
            endfunc;

            dosomething;

            namespace Core;
                func run;
                    print 'thecore';
                endfunc;

                run;

                $corevar = 'corevar';
                out $corevar;
            endns;

            Core.run;
        endns;

        out $App.name;

        App.Core.run;

        out $App.Core.corevar;
        '''), 'parsaparsadoingthecorecorevarthecoreparsathecorecorevar')

        self.assert_output(self.run_without_error('''
        namespace App;
            $name = 'parsa';
            func dosomething;
                print 'doing';
            endfunc;

            namespace Core;
                func run;
                    print 'thecore';
                endfunc;
                $corevar = 'corevar';
            endns;
        endns;

        App.Core.run;
        print $App.Core.corevar;

        use App;

        Core.run;
        print $Core.corevar;

        use App.Core;

        Core.run;
        print $Core.corevar;

        run;
        print $corevar;
        '''), 'thecorecorevarthecorecorevarthecorecorevarthecorecorevar')
