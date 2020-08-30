#!/usr/bin/python3

help_msg = '''
this is a script to manage pashmak project

Commands:
    test            run tests
    make-test       create new test
    update-headers  update files copyright headers
'''

header_text = '''#
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
'''

import sys, os

if len(sys.argv) <= 1:
    print(help_msg)
    sys.exit()




class GetFilesList:
    # get list of all of .py files in src/ folder
    def __init__(self , path='src/'):
        self.files_list = []
        self.get(path)
    
    def get(self , path='src/'):
        # load and return list
        for f in os.listdir(path):
            if os.path.isdir(path + '/' + f):
                self.get(path + '/' + f + '/')
            elif os.path.isfile(path + '/' + f):
                self.add_once(path + '/' + f)

    def add_once(self , f):
        # add on file to the list
        # check if file is .py
        if f[len(f)-3:] == '.py':
            # replace // with /
            f = f.replace('//' , '/')
            self.files_list.append(f)
    
    @staticmethod
    def set_once_file_header(fname):
        global header_text
        spliter = ('#' * 50) + '\n\n'
    
        # open file and add header
        content = open(fname , 'r').read()
        new_content = ''

        parts = content.split(spliter)
        if len(parts) == 1:
            new_content = header_text + spliter + parts[0]
        elif len(parts) == 2:
            new_content = header_text + spliter + parts[1]
        else:
            print('error in ' + fname + ': duplicate spliter')
            return

        # add current filename to header
        only_file_name = fname.split('/')[-1]
        new_content = '# ' + only_file_name + '\n' + new_content

        if fname == 'src/pashmak.py':
            new_content = '#!/usr/bin/env python3\n' + new_content

        f = open(fname , 'w')
        f.write(new_content)
        f.close()



    


if sys.argv[1] == 'update-headers':
    # get files list in src/ folder and set header of them
    files_list = GetFilesList('src/').files_list
    for f in files_list:
        GetFilesList.set_once_file_header(f)

    print('Headers updated successfully')
    sys.exit()


print('Unknow command "' + sys.argv[1] + '"')