#
# parser.py
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

''' Pashmak syntax parser '''

import random

def handle_special_char(op_str: str, ch: str) -> list:
    ''' Handle \\<special-char> as clean text '''

    # replace \<char> with a random string to replace it after argument parsing
    str_to_replace_with_semicolon = '<semicolon' + str(random.random()) + '>'

    # make sure generated random string is not currently in this line
    while str_to_replace_with_semicolon in op_str:
        str_to_replace_with_semicolon = '<semicolon' + str(random.random()) + '>'

    op_str = op_str.replace('\\' + ch, str_to_replace_with_semicolon)

    return [op_str, str_to_replace_with_semicolon]

def ignore_comment(op_str: str) -> str:
    ''' Remove comments from code line '''
    parts = op_str.split('#', 1) # just part of before `#` is the code and after that is comment
    return parts[0]

def parse_op(op_str: str, file_path='<system>', line_number=0) -> dict:
    ''' Parse a operation from text to object '''
    op = {}
    op['str'] = op_str # operation plain string
    op_parts = op_str.split(' ')
    op['command'] = op_parts[0]
    op['command'] = op['command'].split('(')
    if len(op['command']) > 1:
        op_parts[0] = op['command'][0]
        op_parts.insert(1, '(' + op['command'][1])
    op['command'] = op['command'][0]
    op_parts.pop(0)
    op['args_str'] = ''
    op['args'] = []
    # set operation arguments
    for op_part in op_parts:
        if op_part != '' or op['command'] == 'mem':
            if op['command'] == 'import':
                if op_part:
                    if op_part[0] == '@':
                        op_part = '"' + op_part
                        if op_part[-1] == ',':
                            op_part = op_part[:len(op_part)-1] + '",'
                        else:
                            op_part = op_part + '"'
            op['args'].append(op_part)
            op['args_str'] += op_part
        op['args_str'] += ' '
    op['args_str'] = op['args_str'].strip()
    op['str'] = op['command'] + ' ' + op['args_str']
    op['file_path'] = file_path
    op['line_number'] = line_number
    return op

def parse(content: str, filepath='<system>') -> list:
    ''' Parse code from text and return list of operations '''
    # split the lines
    lines = content.split('\n')
    line_counter = 1
    operations = []
    for line in lines:
        # clean line, remove comments from that
        line = line.strip()
        tmp = handle_special_char(line, '#')
        line = tmp[0]
        line = ignore_comment(line)
        line = line.replace(tmp[1], '#')
        tmp = handle_special_char(line, ';')
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
                op['line_number'] = line_counter
                op['file_path'] = filepath
                if op['command'] == 'section':
                    operations.append(parse_op('pass'))
                operations.append(op)
        line_counter += 1

    # handle the if statement
    open_ifs = []
    open_ifs_counters = []
    i = 0
    while i < len(operations):
        try:
            if operations[i]['command'] == 'if':
                # init new if block
                open_ifs.append('tmpsectionif' + str(random.random()).replace('.', '') + '_')
                open_ifs_counters.append(2)

                operations.insert(i+1, parse_op('mem not (' + operations[i]['args_str'] + ')', file_path='<system>', line_number=i))
                operations.insert(i+2, parse_op('gotoif ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
            elif operations[i]['command'] == 'elif' or operations[i]['command'] == 'else':
                cond = operations[i]['args_str']
                if operations[i]['command'] == 'else':
                    cond = 'True'
                operations.insert(i+1, parse_op('goto ' + open_ifs[-1] + 'end', file_path='<system>', line_number=i))
                operations.insert(i+2, parse_op('section ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
                operations.insert(i+3, parse_op('mem not (' + cond + ')', file_path='<system>', line_number=i))
                operations.insert(i+4, parse_op('gotoif ' + open_ifs[-1] + str(open_ifs_counters[-1]+1), file_path='<system>', line_number=i))
                open_ifs_counters[-1] += 1
            elif operations[i]['command'] == 'endif':
                operations.insert(i+1, parse_op('section ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
                operations.insert(i+2, parse_op('section ' + open_ifs[-1] + 'end', file_path='<system>', line_number=i))
                open_ifs.pop()
                open_ifs_counters.pop()
        except:
            pass

        if i == len(operations)-1 and open_ifs and open_ifs_counters:
            operations.insert(i+1, parse_op('endif', file_path='<system>', line_number=i))
        i += 1

    return operations
