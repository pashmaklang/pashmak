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

''' The test '''

import random
import os
import tempfile
from TestCore import TestCore

class test_modules(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(self.run_without_error('''
            import '@hash';

            use hash;

            blake2b 'hello'; out ^; print '\\n';

            blake2s 'hello'; out ^; print '\\n';

            md5 'hello'; out ^; print '\\n';

            sha1 'hello'; out ^; print '\\n';

            sha224 'hello'; out ^; print '\\n';

            sha256 'hello'; out ^; print '\\n';

            sha384 'hello'; out ^; print '\\n';

            sha3_224 'hello'; out ^; print '\\n';

            sha3_256 'hello'; out ^; print '\\n';

            sha3_384 'hello'; out ^; print '\\n';

            sha3_512 'hello'; out ^; print '\\n';

            sha512 'hello'; out ^; print '\\n';

            hash.shake_128 'hello', 30; out ^; print '\\n';

            hash.shake_256 'hello', 30; out ^; print '\\n';
            '''),
            '''e4cfa39a3d37be31c59609e807970799caa68a19bfaa15135f165085e01d41a65ba1e1b146aeb6bd0092b49eac214c103ccfa3a365954bbbe52f74a2b3620c94
19213bacc58dee6dbde3ceb9a47cbb330b3d86f8cca8997eb00be456f140ca25
5d41402abc4b2a76b9719d911017c592
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f
b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81
3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392
720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887
75d527c368f2efe848ecf6b073a36767800805e9eef2b1857d5f984f036eb6df891d75f72d9b154518c1cd58835286d1da9a38deba3de98b5a53e5ed78a84976
9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
8eb4b6a932f280335ee1a279f8c208a349e7bc65daf831d3021c21382529
1234075ae4a1e77316cf2d8000974581a343b9ebbca7e3d1db83394c30f2
'''
        )

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

        tmp_file = tempfile.gettempdir().replace('\\', '/') + '/' + 'pashmak-test-file-' + str(random.random())
        self.assert_output(self.run_without_error('''
        import '@file';

        file.open ["''' + tmp_file + '''", 'w'];
        set $file; copy $file;
        file.write [$file, "content of file"];
        file.close $file;

        file.open ["''' + tmp_file + '''", 'r'];
        copy $file;
        file.read $file; out ^;
        '''), 'content of file')

        try:
            os.remove(tmp_file)
        except:
            pass
