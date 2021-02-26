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

""" Pashmak syntax lexer """

import time
import random

literals = '()+-/*%=}{<>[],:! '
""" The literal characters """

def parse_op(op_str: str, file_path='<system>', line_number=0) -> dict:
    """Parse a command from text to object

    Args:
        op_str(str): The command as string
        file_path(str): Which file this line is loaded from
        line_number(int): Which line number this code loaded from
    
    Return:
        returns a dict.
        Strructure:
        {
            "command": "<the command>",
            "args_str": "arguments of command as string",
            "str": "all of command as string",
            "args": ["arguments", "as", "list"], // seprated by ` ` space
            "file_path": "/path/to/file/that/this/line/loaded/from",
            "line_number": 12
        }
    """
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

    # handle backward compatiblity for `section` command
    if op['command'] == 'section':
        op['command'] = 'label'

    if op['command'] in ['import', 'import_once', 'import_run', 'import_run_once']:
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
        if op_parts:
            if op_parts[0].strip()[0] == '(':
                op_parts[0] = op_parts[0].strip()[1:]
                op_parts[-1] = op_parts[-1].strip()
                op_parts[-1] = op_parts[-1][:len(op_parts[-1])-1]
    # set command arguments
    for op_part in op_parts:
        if op_part != '' or op['command'] == 'mem':
            if op['command'] in ['import', 'import_once', 'import_run', 'import_run_once']:
                op_part = op_part.strip()
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
    op['strings'] = parse_string(op['str'].strip())
    op['eval'] = parse_eval(op['str'].strip())
    op['args_eval'] = parse_eval(op['args_str'].strip())
    return op

def parse_string(command: str):
    """ Splits strings and codes

    Args:
        command(str): That thing you want to parse

    Return:
        A list from other lists
        [
            [False, "println("],
            [True, "'hello world'"],
            [False, ")"],
        ]
        (the above output is for `println('hello world')`)
        The first boolean item, if is True, means that this part is a string,
        But if is False, means this is a native code.
        And the second item is the code as string

    This function is useful when you want to replace/etc something on a code,
    But only in native code and not on strings.
    """
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

def parse_eval(command: str):
    """ This function parses the eval and converts it to the python eval
    
    Args:
        command(str): The command

    Return:
        Returns a string from generated python code

    Example:
        `$name + '.'` -> `self.get_var('name') + '.'`
        or
        `some_func($i + 1)` -> `self.functions['some_func'](self.get_var('i') + 1)`
    """
    if type(command) == str:
        command_parts = parse_string(command)
    else:
        command_parts = command

    output = []
    for code in command_parts:
        if code[0] == False:
            code = code[1]
            # replace variable names with value of them
            code_words = multi_char_split(code, literals, keep_seprators=True)
            code_words = [w.strip() for w in code_words if w.strip() != '']
            counter = 0
            for word in code_words:
                if word in literals:
                    output.append(['l', word])
                elif word[0] == '$':
                    output.append(['v', word[1:], 'self.get_var("' + word[1:] + '")'])
                else:
                    try:
                        tmp = code_words[counter-2:counter]
                    except:
                        tmp = []
                    if tmp == ['-', '>']:
                        output.append(['n', word])
                    else:
                        output.append(['o', word])
                counter += 1
        else:
            output.append(['s', code[1]])

    i = 0
    while i < len(output):
        if output[i][-1] == '>':
            try:
                if output[i-1:i+1] == [['l', '-'], ['l', '>']]:
                    output[i-1:i+1] = [['l', '.']]
                    i -= 1
            except:
                pass
        elif output[i][0] != 's':
            output[i][-1] = output[i][-1].replace('^', 'self.get_mem()')
        i += 1
    # TODO : handle xor
    #tmp = '<<<tempstrforxor' + str(time.time()) + str(random.random()) + '>>>'
    #code = code.replace('^^', tmp)
    #code = code.replace(tmp, '^')

    return output

def multi_char_split(string, seprators, count=None, keep_seprators=False):
    """ Splits string by multi seprators """
    result = ['']
    i = 0
    for char in string:
        if char in seprators and (count is None or i < count):
            if keep_seprators:
                result.append(char)
            result.append('')
            i += 1
        else:
            result[-1] += char
    return result
