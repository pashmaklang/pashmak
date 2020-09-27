#
# test_modules.py
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
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

import time, os

from TestCore import TestCore

class test_modules(TestCore):
    def run(self):
        self.assert_output(self.run_without_error('''
        import "@hash";

        hash.sha256 'hello'; out ^;
        print '\\n';

        hash.md5 'hello'; out ^;
        ''') , '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824\n5d41402abc4b2a76b9719d911017c592')

        mem = self.run_without_error('''
        import "@random";

        random.randint [5,10];
        ''')['mem']
        self.assert_true(int(mem) >= 5 and int(mem) <= 10)

        mem = self.run_without_error('''
        import "@random";
        random.random;
        ''')['mem']
        self.assert_true(float(mem) < 1)

        tmp_file = '/tmp/pashmak-test-file-' + str(time.time())
        self.assert_output(self.run_without_error('''
        import '@file';

        file.open ["''' + tmp_file + '''" , 'w'];
        set $file; copy $file;
        file.write [$file , "content of file"];
        file.close $file;

        file.open ["''' + tmp_file + '''" , 'r'];
        copy $file;
        file.read $file; out ^;
        ''') , 'content of file')
        os.remove(tmp_file)
