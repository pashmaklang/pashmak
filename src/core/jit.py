#
# jit.py
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

""" The pashmak Jit compiler

The pashmak jit compiler caches runed files and loads them from cache and
makes interpreter speed up
"""

import os
import hashlib
from . import parser

def calc_file_sha256(filepath: str) -> str:
    """
    gets filepath and calculates sha256 sum of that
    
    Args:
        filepath (str): filepath you want to calculate hash of that

    Returns:
        str: calculated hash
    """
    sha256_hash = hashlib.sha256()
    f = open(filepath, 'rb')
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load(path: str, code_location: str, self=None) -> list:
    """ Loads a script

    If file is already caches and file is not changed, returns the cache
    but if not, caches the file and then returns the commands
    """
    # check is jit disabled
    is_jit_disabled = False
    try:
        is_jit_disabled = bool(os.environ['PASHMAK_DISABLE_JIT'])
    except:
        pass
    if is_jit_disabled:
        f = open(path, 'r')
        content = f.read()
        f.close()
        if self != None:
            content = '$__ismain__ = False; $__file__ = "' + path.replace('\\', '\\\\') + '";\n$__dir__ = "' + os.path.dirname(path).replace('\\', '\\\\') + '"\n' + content
            content += '\n$__file__ = "' + self.get_var('__file__').replace('\\', '\\\\') + '"'
            content += '\n$__dir__ = "' + self.get_var('__dir__').replace('\\', '\\\\') + '"'
            content += '\n$__ismain__ = "' + str(bool(self.get_var('__ismain__'))) + '"'
        return parser.parse(content, filepath=code_location)

    file_hash = calc_file_sha256(path)
    path = path.replace('\\', '/')
    only_file_name = path.split('/')[-1]
    the_cache_dir = os.path.dirname(os.path.abspath(path)) + '/__pashmam__'
    the_cache_file = the_cache_dir + '/' + only_file_name + '.rikht'
    content = False
    is_new_cache = False
    try:
        # check cache exists
        if not os.path.isdir(the_cache_dir):
            os.mkdir(the_cache_dir)
        if os.path.isfile(the_cache_file):
            cache_f = open(the_cache_file, 'r')
            cache_f_content = cache_f.read()
            cache_f.close()
            the_hash = cache_f_content.split('\n', 1)[0]
            if the_hash == file_hash:
                content = cache_f_content.split('\n', 1)[-1]
    except:
        pass

    if content == False:
        is_new_cache = True
        f = open(path, 'r')
        content = f.read()
        f.close()
        if self != None:
            content = '$__ismain__ = False; $__file__ = "' + path.replace('\\', '\\\\') + '";\n$__dir__ = "' + os.path.dirname(path).replace('\\', '\\\\') + '"\n' + content
            content += '\n$__file__ = "' + self.get_var('__file__').replace('\\', '\\\\') + '"'
            content += '\n$__dir__ = "' + self.get_var('__dir__').replace('\\', '\\\\') + '"'
            content += '\n$__ismain__ = "' + str(bool(self.get_var('__ismain__'))) + '"'

    # write the content on cache
    if is_new_cache:
        code_commands = parser.parse(content, filepath=code_location, only_parse=True)
        new_content = file_hash + '\n'
        for op in code_commands:
            new_content += op['str'] + '\n'
        new_content = new_content.strip()
        cache_f = open(the_cache_file, 'w')
        cache_f.write(new_content)
        cache_f.close()
    code_commands = parser.parse(content, filepath=code_location)

    return code_commands
