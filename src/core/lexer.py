#
# lexer.py
#
# The Pashmak Project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
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

''' Pashmak syntax lexer '''

import random
import time

literals = '()+-/*%=}{<>[], '
""" The literal characters """

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
    if op['command'] == 'import' or op['command'] == 'import_once':
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
            if op['command'] in ['import', 'import_once', 'import_run', 'import_run_once']:
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
    # handle multiline
    new_lines = ['']
    for line in lines:
        if line:
            if line[-1] == '\\':
                new_lines[-1] += line[:-1]
            else:
                new_lines[-1] += line
                new_lines.append('')
        else:
            new_lines.append(line)
    lines = new_lines

    # handle `([{` and `}])` chars
    p_counter = 0
    b_counter = 0
    a_counter = 0
    i = 0
    while i < len(lines):
        if lines[i]:
            line_parts = parse_string(lines[i])
            for part in line_parts:
                if part[0] == False:
                    j = 0
                    while j < len(part[1]):
                        if part[1][j] == '(':
                            p_counter += 1
                        elif part[1][j] == '[':
                            b_counter += 1
                        elif part[1][j] == '{':
                            a_counter += 1
                        elif part[1][j] == '}':
                            a_counter -= 1
                        elif part[1][j] == ']':
                            b_counter -= 1
                        elif part[1][j] == ')':
                            p_counter -= 1
                        if p_counter < 0:
                            p_counter = 0
                        if b_counter < 0:
                            b_counter = 0
                        if a_counter < 0:
                            a_counter = 0
                        j += 1
            if p_counter > 0 or b_counter > 0 or a_counter > 0:
                if lines[i][-1] != '\\':
                    lines[i] += '\\'
        i += 1

    # check \ in end of line again
    new_lines = ['']
    for line in lines:
        if line:
            if line[-1] == '\\':
                new_lines[-1] += line[:-1]
            else:
                new_lines[-1] += line
                new_lines.append('')
        else:
            new_lines.append(line)
    lines = new_lines

    line_counter = 1
    commands = []
    for line in lines:
        # clean line, remove comments from that
        line = line.strip()
        if line:
            if line[0] == '#':
                continue
        line_str_parts = parse_string(line)
        new_line = ''
        for line_part in line_str_parts:
            if line_part[0] == True:
                new_line += line_part[1]
            else:
                new_line += line_part[1].split('#', 1)[0]
                if '#' in line_part[1]:
                    break
        line = new_line

        # get commands by spliting line by ;
        line_str_parts = parse_string(line)
        new_lines = ['']
        for line_part in line_str_parts:
            if line_part[0] == True:
                new_lines[-1] += line_part[1]
            else:
                tmp = line_part[1].split(';')
                new_lines[-1] += tmp[0]
                if len(tmp) > 1:
                    tmp = tmp[1:]
                    new_lines = [*new_lines, *tmp]
        ops = new_lines
        for op in ops:
            op = op.strip()
            #op = op.replace(clean_semicolon, ';')
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

def parse_string(command: str):
    """ Splits strings and codes """
    i = 0
    command = command.strip()
    is_in_string = False
    command_parts = [[False, '']]
    while i < len(command):
        is_string_start = False
        if command[i] == '"' or command[i] == "'":
            before_backslashes_count = 0
            try:
                x = i-1
                while x >= 0:
                    if command[x] == '\\':
                        before_backslashes_count += 1
                    else:
                        x = -1
                    x -= 1
            except:
                pass
            if is_in_string:
                if before_backslashes_count % 2 != 0 and before_backslashes_count != 0:
                    pass
                elif is_in_string == command[i]:
                    is_in_string = False
                    command_parts[-1][1] += command[i]
                    is_string_start = True
                    command_parts.append([False, ''])
            else:
                is_in_string = command[i]
                command_parts.append([True, ''])
                command_parts[-1][1] += command[i]
                is_string_start = True
        if not is_string_start:
            command_parts[-1][1] += command[i]
        i += 1
    return command_parts
