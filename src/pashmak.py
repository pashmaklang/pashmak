#!/usr/bin/env python3
#
# pashmak.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of Pashmak.
#
# Pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pashmak.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################

''' Pashmak cli entry point '''

import sys
import os
import signal
from core import parser
from core import program, version, jit

def signal_handler(signal_code, frame):
    """ handle signal """
    sys.exit(1)

if __name__ == '__main__':
    # set signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # validate arguments
    if len(sys.argv) <= 1:
        print(sys.argv[0] + ': script file name is required: pashmak [filename]')
        sys.exit(1)

    if sys.argv[1] == '--info':
        print('Pashmak Version: ' + version.version)
        print('Python Version: ', end='')
        print(sys.version.replace('\n', ''))
        sys.exit(0)

    if sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print(version.version)
        sys.exit(0)

    if sys.argv[1] in ['-m', '--modules']:
        sys.argv[1] = '-r'
        if len(sys.argv) <= 2:
            sys.argv.append('')
        sys.argv[2] = '''
        # print list of modules
        println 'List of pashmak available modules';
        println '---------------------------------';
        $modules = list(modules.modules.keys())
        $i = 0;
        section loop;
            println $modules[$i];
            $i = $i + 1;
        mem $i < len($modules); gotoif loop;
        '''

    if sys.argv[1] == '-r':
        if len(sys.argv) <= 2:
            print(sys.argv[0] + ': `-r` option requires code as argument: -r [code...]')
            sys.exit(1)
        script_commands = parser.parse(sys.argv[2], filepath=filename)
        filename = '-r'
    else:
        filename = sys.argv[1]

        if sys.argv[1] == '-':
            script_content = ''
            for line in sys.stdin.readlines():
                script_content += line
            script_commands = parser.parse(script_content, filepath=filename)
        elif not os.path.isfile(filename):
            print(sys.argv[0] + ': file "' + filename + '" not found')
            sys.exit(1)
        else:
            # read content of file and parse it with the parser
            script_commands = jit.load(filename, code_location=filename)

    # make pashmak program object
    prog = program.Program(args=sys.argv[1:])
    prog.main_filename = filename
    prog.set_commands(script_commands)
    prog.start()
