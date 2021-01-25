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
    #op['eval'] = parse_eval(op['str'])
    #op['args_eval'] = parse_eval(op['args_str'])
    return op

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

def parse_eval(command, self=None, only_str_parse=False):
    """ This function parses the eval and converts it to the python eval """
    # TODO : drop dependency to `self`
    command_parts = parse_string(command)

    if only_str_parse:
        return command_parts, []

    global literals

    full_op = ''
    opened_inline_calls_count = 0
    vars_to_check = []
    for code in command_parts:
        if code[0] == False:
            code = code[1]
            # replace variable names with value of them
            literals = literals
            code_words = multi_char_split(code, literals)
            for word in code_words:
                if word:
                    if word[0] == '$':
                        vars_to_check.append(word[1:])
                        code = code.replace('$' + word[1:], 'self.get_var("' + word[1:] + '")', 1)
                    else:
                        func_real_name = self.get_func_real_name(word)
                        if func_real_name != False:
                            tmp_counter = 0
                            while tmp_counter < len(code):
                                tmp_index = code.find(word, tmp_counter)
                                if tmp_index < 0:
                                    tmp_counter = (+tmp_counter) + 1
                                else:
                                    tmp_counter = tmp_index + 1
                                if code[tmp_index-2:tmp_index] != '->':
                                    if code[tmp_index-1:tmp_index] in literals:
                                        if code[tmp_index+len(word):tmp_index+len(word)+1] in literals:
                                            code = code.replace(code[tmp_index-2:tmp_index] + word + code[tmp_index+len(word):tmp_index+len(word)+1], code[tmp_index-2:tmp_index] + 'self.functions["' + func_real_name + '"]' + code[tmp_index+len(word):tmp_index+len(word)+1], 1)
                                            break
                        else:
                            # This is a class
                            class_real_name = self.get_class_real_name(word)
                            if class_real_name != False:
                                tmp_counter = 0
                                while tmp_counter < len(code):
                                    tmp_index = code.find(word, tmp_counter)
                                    if tmp_index < 0:
                                        tmp_counter = (+tmp_counter) + 1
                                    else:
                                        tmp_counter = tmp_index + 1
                                    if code[tmp_index-2:tmp_index] != '->':
                                        if code[tmp_index-1:tmp_index] in literals:
                                            if code[tmp_index+len(word):tmp_index+len(word)+1] in literals:
                                                code = code.replace(code[tmp_index-2:tmp_index] + word + code[tmp_index+len(word):tmp_index+len(word)+1], code[tmp_index-2:tmp_index] + 'self.classes["' + class_real_name + '"]' + code[tmp_index+len(word):tmp_index+len(word)+1], 1)
                                                break
                            else:
                                try:
                                    self.defines[word]
                                    tmp_counter = 0
                                    while tmp_counter < len(code):
                                        tmp_index = code.find(word, tmp_counter)
                                        if tmp_index < 0:
                                            tmp_counter = (+tmp_counter) + 1
                                        else:
                                            tmp_counter = tmp_index + 1
                                        if code[tmp_index-2:tmp_index] != '->':
                                            if code[tmp_index-1:tmp_index] in literals:
                                                if code[tmp_index+len(word):tmp_index+len(word)+1] in literals:
                                                    code = code.replace(code[tmp_index-2:tmp_index] + word + code[tmp_index+len(word):tmp_index+len(word)+1], code[tmp_index-2:tmp_index] + 'self.defines["' + word + '"]' + code[tmp_index+len(word):tmp_index+len(word)+1], 1)
                                                    break
                                except:
                                    pass

            code = code.replace('->', '.')
            tmp = '<<<tempstrforxor' + str(time.time()) + str(random.random()) + '>>>'
            code = code.replace('^^', tmp)
            code = code.replace('^', 'self.get_mem()')
            code = code.replace(tmp, '^')
        else:
            code = code[1]
        full_op += code
    return full_op, vars_to_check

def multi_char_split(string, seprators, count=None):
    """ Splits string by multi seprators """
    result = ['']
    i = 0
    for char in string:
        if char in seprators:
            if count == None:
                result.append('')
            elif i < count:
                result.append('')
            i += 1
        else:
            result[-1] += char
    return result
