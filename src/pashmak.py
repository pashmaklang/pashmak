#!/usr/bin/env python3
# pashmak.py
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

#!/usr/bin/python3

import sys
import os
from syntax import parser
from core import program

# validate arguments
if len(sys.argv) <= 1:
    print('pashmak: script file name is required: pashmak [filename]')
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print('pashmak: file "' + filename + '" not found')
    sys.exit(1)


# read content of file and parse it with the parser
script_f = open(filename , 'r')
script_content = script_f.read()
script_operations = parser.parse(script_content)

# make pashmak program object
prog = program.Program()
prog.set_operations(script_operations)
prog.start()

