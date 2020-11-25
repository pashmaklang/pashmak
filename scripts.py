#!/usr/bin/python3

help_msg = '''
this is a script to manage pashmak project

Commands:
    make-test       create new test
    update-headers  update files copyright headers
    build-doc       build documentation in README.md from doc/ folder
    build-modules   build modules from modules/ folder in src/core/modules.py
    release         release new version number
'''

header_text = '''#
# The Pashmak Project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
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

test_content = '''\'\'\' The test \'\'\'

from TestCore import TestCore

class <tstname>(TestCore):
    \'\'\' The test \'\'\'
    def run(self):
        \'\'\' Run test \'\'\'
        self.assert_true(True)
'''

import sys
import os
from datetime import date
from tests import tcolor

if len(sys.argv) <= 1:
    print(help_msg)
    sys.exit()

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
            new_content = header_text + spliter + parts[1]
        else:
            print('error in ' + fname + ': duplicate spliter')
            return

        # add current filename to header
        only_file_name = fname.split('/')[-1]
        new_content = '#\n# ' + only_file_name + '\n' + new_content

        if fname == 'src' + '/' + 'pashmak.py' or fname == 'tests' + '/' + 'run.py':
            new_content = '#!/usr/bin/env python3\n' + new_content

        f = open(fname, 'w')
        f.write(new_content)
        f.close()


class TestMaker:
    @staticmethod
    def make(test_name):
        if os.path.isfile('tests' + '/' + 'items' + '/' + test_name + '.py'):
            print('test "' + test_name + '" already exists')
            return 1

        f = open('tests' + '/' + 'items' + '/' + test_name + '.py', 'w')

        global test_content

        content = test_content.replace('<tstname>', test_name)

        f.write(content)
        f.close()
        return 0

class DocBuilder:
    @staticmethod
    def build(path):
        # load .md files from doc/ folder
        doc_parts = os.listdir(path)
        doc_parts = [part for part in doc_parts if part[len(part)-3:] == '.md' and part != 'README.md']
        doc_parts.sort()

        total_content = ''

        # add README.md to the first of content
        readme_header_f = open(path + '/' + 'README.md', 'r')
        total_content += readme_header_f.read() + '\n\n\n'
        readme_header_f.close()

        # append content of doc parts to total_content one by one
        for doc_part in doc_parts:
            doc_part_f = open(path + '/' + doc_part, 'r')
            doc_part_content = doc_part_f.read()
            total_content += doc_part_content + '\n\n\n'
            doc_part_f.close()

        # add a note to end of content
        total_content += '\n##### NOTE: this file is auto generated from `doc` folder. do not change it directly\n'

        # write generated content to the README.md file
        target_file = 'README.md'
        if path != 'doc' + '/' + 'en':
            target_file = 'README-' + path.split('/')[1] + '.md'
        readme_f = open(target_file, 'w')
        readme_f.write(total_content)
        readme_f.close()

        print('\033[32mDocumentation built successfully and README.md generated.\033[0m')


class ModuleBuilder:
    @staticmethod
    def build():
        # get list of modules
        modules = {}
        module_files = os.listdir('modules')
        module_files.sort()
        for module in module_files:
            file_content = open('modules' + '/' + module, 'r').read()
            modules[module[:len(module)-6]] = file_content

        pycode = '''""" Internal modules """

modules = {}
'''
        # write modules as python dictonary in src/core/modules.py file
        for k in modules:
            pycode += '\nmodules["' + k + '"] = """' + modules[k].replace('\n\n', '\n') + '"""'

        pycode += '\n'

        f = open('src' + '/' + 'core' + '/' + 'modules.py', 'w')
        f.write(pycode)
        f.close()

        print("\033[32mall of modules mixed in 'src/core/modules.py' successfuly\033[0m")

class Releaser:
    @staticmethod
    def run(new_version: str):
        if new_version[0] == 'v':
            new_version = new_version[1:]
        # change version number
        f = open('src/core/version.py', 'r')
        content = f.read()
        content = content.split('version = ')[0]
        content += 'version = \'v'
        content += new_version
        content += '\'\n'
        f.close()
        f = open('src/core/version.py', 'w')
        f.write(content)
        f.close()

        f = open('CHANGELOG.md', 'r')
        content = f.read()
        date_str = date.today()
        date_str = str(date_str.year) + '-' + str(date_str.month) + '-' + str(date_str.day)
        content = content.replace('## next release', '## ' + new_version + ' (' + date_str + ')')
        f.close()
        f = open('CHANGELOG.md', 'w')
        f.write(content)
        f.close()

if sys.argv[1] == 'update-headers':
    # get files list in src/ folder and set header of them
    files_list = CopyrightHeaderUpdater('src' + '/').files_list
    for f in files_list:
        CopyrightHeaderUpdater.set_once_file_header(f)

    # get files list in src/ folder and set header of them
    files_list = CopyrightHeaderUpdater('tests' + '/').files_list
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
    sys.exit()

if sys.argv[1] == 'make-test':
    if len(sys.argv) <= 2:
        print('make-test: test name argument is required')
        sys.exit(1)

    sys.exit(TestMaker.make(sys.argv[2]))

if sys.argv[1] == 'build-doc':
    for item in os.listdir('doc'):
        sys.exit(DocBuilder.build('doc' + '/' + item))

if sys.argv[1] == 'build-modules':
    sys.exit(ModuleBuilder.build())

if sys.argv[1] == 'release':
    if len(sys.argv) <= 2:
        print('release: new version name is required')
        sys.exit(1)

    sys.exit(Releaser.run(sys.argv[2]))

print('Unknow command "' + sys.argv[1] + '"')
sys.exit(1)
