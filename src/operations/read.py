# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# read.py															#
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

''' Reads a input from stdin '''

def run(self, op: dict):
    ''' Reads a input from stdin '''

    for arg in op['args']:
        self.arg_should_be_variable_or_mem(arg, op)
        if arg[0] == '$':
            self.variable_required(arg[1:], op)

    if len(op['args']) <= 0:
        if not self.is_test:
            input()
        else:
            self.read_data.pop(0)
        return

    for arg in op['args']:
        if not self.is_test:
            readed_data = input()
        else:
            readed_data = self.read_data[0]
            self.read_data.pop(0)

        if arg == '^':
            self.mem = readed_data
        else:
            self.set_var(arg[1:], readed_data)
