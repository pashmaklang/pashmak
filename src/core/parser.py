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
import time

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
    ''' Parse a command from text to object '''
    op = {}
    op['str'] = op_str # command plain string
    op_parts = op_str.split(' ')
    op['command'] = op_parts[0]
    op['command'] = op['command'].split('(', 1)
    if len(op['command']) > 1:
        op_parts[0] = op['command'][0]
        op_parts.insert(1, '(' + op['command'][1])
    op['command'] = op['command'][0]
    op_parts.pop(0)
    op['args_str'] = ''
    op['args'] = []
    if op['command'] == 'import':
        new_op_parts = []
        i = 0
        while i < len(op_parts):
            if '@' in op_parts[i] and ',' in op_parts[i]:
                op_parts[i] = op_parts[i].replace(',', ', ')
                tmp = op_parts[i].split(' ')
                if len(tmp) > 1:
                    op_parts[i] = tmp[0]
                    tmp[1:]
                    z = 0
                    while z < len(tmp):
                        new_op_parts.append(tmp[z])
                        z += 1
            else:
                new_op_parts.append(op_parts[i])
            i += 1
        op_parts = new_op_parts
    # set command arguments
    for op_part in op_parts:
        if op_part != '' or op['command'] == 'mem':
            if op['command'] == 'import':
                op_part = op_part.strip().strip(')').strip('(')
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

def parse(content: str, filepath='<system>', only_parse=False) -> list:
    ''' Parse code from text and return list of commands '''
    # split the lines
    lines = content.split('\n')
    line_counter = 1
    commands = []
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

        # get commands by spliting line by ;
        ops = line.split(';')
        for op in ops:
            op = op.strip()
            op = op.replace(clean_semicolon, ';')
            if op != '':
                # parse once command and append it to the list
                op = parse_op(op)
                op['line_number'] = line_counter
                op['file_path'] = filepath
                if op['command'] == 'section' and only_parse == False:
                    commands.append(parse_op('pass'))
                commands.append(op)
        line_counter += 1

    if only_parse:
        return commands

    # handle the if statement
    open_ifs = []
    open_ifs_counters = []
    i = 0
    while i < len(commands):
        try:
            if commands[i]['command'] == 'if':
                # init new if block
                open_ifs.append('tmpsectionif' + str(random.random()).replace('.', '') + str(time.time()).replace('.', '') + '_')
                open_ifs_counters.append(2)

                commands.insert(i+1, parse_op('mem not (' + commands[i]['args_str'] + ')', file_path='<system>', line_number=i))
                commands.insert(i+2, parse_op('gotoif ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
            elif commands[i]['command'] == 'elif' or commands[i]['command'] == 'else':
                cond = commands[i]['args_str']
                if commands[i]['command'] == 'else':
                    cond = 'True'
                commands.insert(i+1, parse_op('goto ' + open_ifs[-1] + 'end', file_path='<system>', line_number=i))
                commands.insert(i+2, parse_op('section ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
                commands.insert(i+3, parse_op('mem not (' + cond + ')', file_path='<system>', line_number=i))
                commands.insert(i+4, parse_op('gotoif ' + open_ifs[-1] + str(open_ifs_counters[-1]+1), file_path='<system>', line_number=i))
                open_ifs_counters[-1] += 1
            elif commands[i]['command'] == 'endif':
                commands.insert(i+1, parse_op('section ' + open_ifs[-1] + str(open_ifs_counters[-1]), file_path='<system>', line_number=i))
                commands.insert(i+2, parse_op('section ' + open_ifs[-1] + 'end', file_path='<system>', line_number=i))
                open_ifs.pop()
                open_ifs_counters.pop()
        except:
            pass

        if i == len(commands)-1 and open_ifs and open_ifs_counters:
            commands.insert(i+1, parse_op('endif', file_path='<system>', line_number=i))
        i += 1

    return commands
