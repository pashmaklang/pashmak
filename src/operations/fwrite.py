#
# fwrite.py
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

''' Writes on a file '''

def run(self, op: dict):
    ''' Writes on a file '''
    args = op['args']

    if len(args) <= 0:
        self.raise_error('ArgumentError', 'fwrite operation gets two arguments', op)

    mem = self.mem

    filepath = args[0]

    if len(args) == 1:
        content = self.get_mem()
    else:
        content = args[1]

    self.arg_should_be_variable_or_mem(filepath, op)
    self.arg_should_be_variable_or_mem(content, op)

    try:
        if filepath == '^':
            filepath_value = self.get_mem()
        else:
            filepath_value = self.get_var(filepath[1:])
    except:
        self.raise_variable_error(filepath, op)

    try:
        if content == '^':
            content_value = mem
        else:
            content_value = self.get_var(content[1:])
    except:
        self.raise_variable_error(content, op)

    try:
        f = open(filepath_value, 'w')
        f.write(content_value)
        f.close()
    except Exception as ex:
        self.raise_error('FileError', str(ex), op)
