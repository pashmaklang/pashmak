# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# parser.py															#
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

''' Pashmak syntax parser '''

import random

def handle_backslash_semicolon(op_str: str) -> list:
    ''' Handle \\; as clean text semicolon '''

    # replace \; with a random string to replace it after argument parsing
    str_to_replace_with_semicolon = '<semicolon' + str(random.random()) + '>'

    # make sure generated random string is not currently in this line
    while str_to_replace_with_semicolon in op_str:
        str_to_replace_with_semicolon = '<semicolon' + str(random.random()) + '>'

    op_str = op_str.replace('\\;', str_to_replace_with_semicolon)

    return [op_str, str_to_replace_with_semicolon]

def ignore_comment(op_str: str) -> str:
    ''' Remove comments from code line '''
    parts = op_str.split('#', 1) # just part of before `#` is the code and after that is comment
    return parts[0]

def parse_op(op_str: str) -> dict:
    ''' Parse a operation from text to object '''
    op = {}
    op['str'] = op_str # operation plain string
    op_parts = op_str.split(' ')
    op['command'] = op_parts[0]
    op_parts.pop(0)
    op['args_str'] = ''
    op['args'] = []
    # set operation arguments
    for op_part in op_parts:
        if op_part != '' or op['command'] == 'mem':
            op['args'].append(op_part)
            for ch in op_part:
                op['args_str'] += ch
            op['args_str'] += ' '
    op['args_str'] = op['args_str'].strip()
    return op

def parse(content: str) -> list:
    ''' Parse code from text and return list of operations '''
    # split the lines
    lines = content.split('\n')
    operations = []
    for line in lines:
        # clean line, remove comments from that
        line = line.strip()
        line = ignore_comment(line)
        tmp = handle_backslash_semicolon(line)
        line = tmp[0]
        clean_semicolon = tmp[1]

        # get operations by spliting line by ;
        ops = line.split(';')
        for op in ops:
            op = op.strip()
            op = op.replace(clean_semicolon, ';')
            if op != '':
                # parse once operation and append it to the list
                op = parse_op(op)
                operations.append(op)
    return operations
