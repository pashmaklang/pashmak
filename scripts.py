#!/usr/bin/python3

help_msg = '''
this is a script to manage pashmak project

Commands:
    make-test       create new test
    update-headers  update files copyright headers
    build-doc       build documentation in README.md from doc/ folder
    build-modules   build modules from modules/ folder in src/core/modules.py
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
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
'''

test_content = '''from TestCore import TestCore

class <tstname>(TestCore):
    def run(self):
        self.assert_true(True)
'''

import sys, os

from tests import tcolor

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
        new_content = '#\n# ' + only_file_name + '\n' + new_content

        if fname == 'src/pashmak.py' or fname == 'tests/run.py':
            new_content = '#!/usr/bin/env python3\n' + new_content

        f = open(fname , 'w')
        f.write(new_content)
        f.close()


class TestMaker:
    @staticmethod
    def make(test_name):
        if os.path.isfile('tests/items/' + test_name + '.py'):
            print('test "' + test_name + '" already exists')
            return 1
        
        f = open('tests/items/' + test_name + '.py' , 'w')

        global test_content

        content = test_content.replace('<tstname>' , test_name)

        f.write(content)
        f.close()
        return 0


class DocBuilder:
    @staticmethod
    def build():
        # load .md files from doc/ folder
        doc_parts = os.listdir('doc')
        doc_parts = [part for part in doc_parts if part[len(part)-3:] == '.md' and part != 'README.HEADER.md']
        doc_parts.sort()
        
        total_content = ''

        # add README.HEADER.md to the first of content
        readme_header_f = open('doc/README.HEADER.md' , 'r')
        total_content += readme_header_f.read() + '\n\n\n'
        readme_header_f.close()

        # append content of doc parts to total_content one by one
        for doc_part in doc_parts:
            doc_part_f = open('doc/' + doc_part , 'r')
            doc_part_content = doc_part_f.read()
            total_content += doc_part_content + '\n\n\n'
            doc_part_f.close()

        # write generated content to the README.md file
        readme_f = open('README.md' , 'w')
        readme_f.write(total_content)
        readme_f.close()

        print('\033[32mDocumentation built successfully and README.md generated.\033[0m')


class ModuleBuilder:
    @staticmethod
    def build():
        # get list of modules
        modules = {}
        module_files = os.listdir('modules')
        for module in module_files:
            file_content = open('modules/' + module , 'r').read()
            modules[module[:len(module)-6]] = file_content

        pycode = '''
modules = {}
'''
        # write modules as python dictonary in src/core/modules.py file
        for k in modules:
            pycode += '\nmodules["' + k + '"] = """' + modules[k].replace('\n\n' , '\n') + '"""'
        
        f = open('src/core/modules.py' , 'w')
        f.write(pycode)
        f.close()

if sys.argv[1] == 'update-headers':
    # get files list in src/ folder and set header of them
    files_list = GetFilesList('src/').files_list
    for f in files_list:
        GetFilesList.set_once_file_header(f)

    # get files list in src/ folder and set header of them
    files_list = GetFilesList('tests/').files_list
    for f in files_list:
        GetFilesList.set_once_file_header(f)

    print('\033[32mHeaders updated successfully\033[0m')
    sys.exit()


if sys.argv[1] == 'make-test':
    if len(sys.argv) <= 2:
        print('make-test: test name argument is required')
        sys.exit(1)

    sys.exit(TestMaker.make(sys.argv[2]))

if sys.argv[1] == 'build-doc':
    sys.exit(DocBuilder.build())

if sys.argv[1] == 'build-modules':
    sys.exit(ModuleBuilder.build())

print('Unknow command "' + sys.argv[1] + '"')
sys.exit(1)
