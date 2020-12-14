#!/usr/bin/python3

header_text = '''#
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
'''

import sys
import os

class CopyrightHeaderUpdater:
    # get list of all of .py files in src/ folder
    def __init__(self, path='src' + '/', file_extension='.py'):
        self.files_list = []
        self.get(path, file_extension)
    
    def get(self, path='src' + '/', file_extension='.py'):
        # load and return list
        for f in os.listdir(path):
            if os.path.isdir(path + '/' + f):
                self.get(path + '/' + f + '/', file_extension)
            elif os.path.isfile(path + '/' + f):
                self.add_once(path + '/' + f, file_extension)

    def add_once(self, f, file_extension):
        # add on file to the list
        # check if file is .py
        if f[len(f)-len(file_extension):] == file_extension:
            # replace // with /
            f = f.replace('/'*2, '/')
            self.files_list.append(f)
    
    @staticmethod
    def set_once_file_header(fname):
        global header_text
        spliter = ('#' * 73) + '\n\n'
    
        # open file and add header
        content = open(fname, 'r').read()
        new_content = ''

        parts = content.split(spliter)
        if len(parts) == 1:
            new_content = header_text + spliter + parts[0]
        elif len(parts) == 2:
            old_header = parts[0]
            old_header_parts = old_header.split('# This file is part of Pashmak.')
            old_copyrights = old_header_parts[0].split('# The Pashmak Project')[-1]
            new_header = header_text

            tmp = new_header.split('# This file is part of Pashmak.')
            new_header = '# The Pashmak Project' + old_copyrights + '# This file is part of Pashmak.' + tmp[-1]

            new_content = new_header + spliter + parts[1]
        else:
            print('error in ' + fname + ': duplicate spliter')
            return

        # add current filename to header
        only_file_name = fname.split('/')[-1]
        new_content = '#\n# ' + only_file_name + '\n#\n' + new_content

        if fname == 'src' + '/' + 'pashmak.py' or fname == 'tests' + '/' + 'run.py':
            new_content = '#!/usr/bin/env python3\n' + new_content

        f = open(fname, 'w')
        f.write(new_content)
        f.close()

if __name__ == '__main__':
    # get files list in src/ folder and set header of them
    files_list = CopyrightHeaderUpdater('src' + '/').files_list
    for f in files_list:
        CopyrightHeaderUpdater.set_once_file_header(f)

    # get files list in src/ folder and set header of them
    files_list = CopyrightHeaderUpdater('tests' + '/', '.pashmt').files_list
    for f in files_list:
        CopyrightHeaderUpdater.set_once_file_header(f)

    # get files list in modules/ folder and set header of them
    files_list = CopyrightHeaderUpdater('modules' + '/', '.pashm').files_list
    for f in files_list:
        CopyrightHeaderUpdater.set_once_file_header(f)

    # get files list in examples/ folder and set header of them
    files_list = CopyrightHeaderUpdater('examples' + '/', '.pashm').files_list
    for f in files_list:
        CopyrightHeaderUpdater.set_once_file_header(f)

    print('\033[32mHeaders updated successfully\033[0m')
