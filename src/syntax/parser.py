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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################


# remove comments from code line
def ignore_comment(op_str):
    parts = op_str.split('#')
    return parts[0]

# parse content of the file to the operations list
def parse(content):
    # split the lines
    lines = content.split('\n')
    operations = []
    for line in lines:
        # clean line, remove comments from that
        line = line.strip()
        line = ignore_comment(line)

        # get operations by spliting line by ;
        ops = line.split(';')
        for op in ops:
            op = op.strip()
            if op != '':
                operations.append(op)
    return operations
