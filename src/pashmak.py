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

