# parser.py
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

import time

# handle \; as a clean text semicolon
def handle_backslash_semicolon(op_str):
    str_to_replace_with_semicolon = '<semicolon' + str(time.time()) + '>'

    while str_to_replace_with_semicolon in op_str:
        str_to_replace_with_semicolon = '<semicolon' + str(time.time()) + '>'

    op_str = op_str.replace('\;' , str_to_replace_with_semicolon)

    return [op_str , str_to_replace_with_semicolon]

# remove comments from code line
def ignore_comment(op_str):
    parts = op_str.split('#')
    return parts[0]

def parse_op(op_str):
    op = {}
    op['str'] = op_str
    op_parts = op_str.split(' ')
    op['command'] = op_parts[0]
    op_parts.pop(0)
    op['args_str'] = ''
    for op_part in op_parts:
        for ch in op_part:
            op['args_str'] += ch
        op['args_str'] += ' '
    return op

# parse content of the file to the operations list
def parse(content):
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
            op = op.replace(clean_semicolon , ';')
            if op != '':
                op = parse_op(op)
                operations.append(op)
    return operations
