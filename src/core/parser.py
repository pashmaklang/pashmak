#
# parser.py
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

''' Pashmak syntax parser '''

import random
import time
from .lexer import parse_op, parse_string

def parse(content: str, filepath='<system>', only_parse=False) -> list:
    """ Parse code from text and return list of commands

    The main parser function.

    Args:
        content(str): The code you want to parse
        filepath(str): The file path you loaded file from
        only_parse(bool): if is True, do not parses `if` statement(default is False)

    Return:
        Returns a list:
        [
            {<output of lexer.parse_op>},
            {<output of lexer.parse_op>},
            {<output of lexer.parse_op>},
            ...
        ]
    
    Handles multiline and if statements.
    """
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
            if (p_counter + b_counter + a_counter) > 0:
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

def split_by_equals(string: str) -> list:
    """ Parses `<something> = <something>`

    Args:
        string(str): The command

    Return:
        list
        Example for `$name = 'pashmak'`: ['$name', "'pashmak'"]
        Example for `println($name)`: ['println($name)']

        If output is a list with 1 item, means this is a not `<a> = <b>`.
        But if yes, first item is `<a>`(before `=`) and second it after `=`.
    """
    commands_parts = parse_string(string)
    parts = ['']
    i = 0
    block_depth = 0
    while i < len(commands_parts):
        if commands_parts[i][0] == True:
            parts[-1] += commands_parts[i][1]
        else:
            j = 0
            while j < len(commands_parts[i][1]):
                if j < len(commands_parts[i][1]) and j > 0:
                    previous_char = ''
                    next_char = ''
                    try:
                        previous_char = commands_parts[i][1][j-1]
                    except IndexError:
                        pass
                    try:
                        next_char = commands_parts[i][1][j+1]
                    except IndexError:
                        pass
                    if commands_parts[i][1][j] == '=' and previous_char != '=' and next_char != '=' and len(parts) == 1 and block_depth <= 0:
                        parts.append('')
                    else:
                        if commands_parts[i][1][j] == '(':
                            block_depth += 1
                        elif commands_parts[i][1][j] == ')':
                            block_depth -= 1
                        parts[-1] += commands_parts[i][1][j]
                else:
                    parts[-1] += commands_parts[i][1][j]
                j += 1
        i += 1
    return parts
