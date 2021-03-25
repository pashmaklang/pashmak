#
# jit.py
#
# The Pashmak Project
# Copyright 2020-2021 parsa shahmaleki <parsampsh@gmail.com>
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

What does Jit compiler?
Jit means `Just in time`.
This system is for speed up interpreting process

While you running a code at First time,
Jit loads source code and parses and lexes this,
Then caches the parsed code.

Then, at the second, third... time you run the same code,
Jit checks that is any cache available for that code.
If yes, do not parse the code again and load the cache
Also jit checks file change. Jit stores sha256 hash of the script in the cache
In the next times, checks that is file changed(using sha256), if yes, parses code again.

How to use it?
Instead of parsing code directly using parser, use the jit.

While you are using parser directly:
    f = open('script.pashm', 'r')
    content = f.read()
    f.close()

    parsed_code = parser.parse(content)

But if you want to use Jit:
    parsed_code = jit.load('/path/to/script.pashm', '/path/to/script.pashm', program_object)

The first and second argument are one thing, but why they are seprated?
The first argument is the real file path that you want to load.
But the second argument is a path to set on parsed core result(code_location).
The second will be used by error raiser system to show that this line of code is loaded from which file.
But usually, both of them are one thing.

Also there is other arguments you can see them:
    print(jit.load.__doc__) # Read docstring of jit.load function
"""

import os
import hashlib
import pickle
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
    with open(filepath, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load(path: str, code_location: str, self=None, is_jit_disabled=False, ismain_default=False) -> list:
    """ Loads a script

    If file is already caches and file is not changed, returns the cache
    but if not, caches the file and then returns the commands

    Args:
        path(str): the real file path
        code_location(str): that file path you want to set on parsed code commands(will be passed to parser)
        self(Program): the current program object
        is_jit_disabled(bool): If Jit should be disabled,
                               put True on this and then this function will parse code and do not uses the cache
        ismain_default(bool): default value of $__ismain__ variable
    """
    # check is jit disabled
    try:
        is_jit_disabled = bool(os.environ['PASHMAK_DISABLE_JIT'])
    except:
        try:
            if os.path.isdir(os.path.dirname(os.path.abspath(path)) + '/__pashmam__'):
                if not os.access(os.path.dirname(os.path.abspath(path)) + '/__pashmam__', os.W_OK):
                    is_jit_disabled = True
            else:
                if not os.access(os.path.dirname(os.path.abspath(path)), os.W_OK):
                    is_jit_disabled = True
        except:
            is_jit_disabled = True
    if is_jit_disabled:
        f = open(path, 'r')
        content = f.read()
        f.close()
        if self != None:
            content = '$__ismain__ = ' + str(ismain_default) + '; $__file__ = ' + repr(path.replace('\\', '\\\\')) + '\n$__dir__ = ' + repr(os.path.dirname(path).replace('\\', '\\\\')) + '\n' + content
            content += '\n$__file__ = ' + repr(self.get_var('__file__').replace('\\', '\\\\'))
            content += '\n$__dir__ = ' + repr(self.get_var('__dir__').replace('\\', '\\\\'))
            content += '\n$__ismain__ = ' + str(bool(self.get_var('__ismain__')))
        return parser.parse(content, filepath=code_location)

    try:
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
                cache_f = open(the_cache_file, 'rb')
                cache_f_content = pickle.load(cache_f)
                cache_f.close()
                the_hash = cache_f_content[0]
                if the_hash == file_hash:
                    content = cache_f_content[1]
                    if content:
                        if content[0]['str'].startswith('$__ismain__ = '):
                            content[0]['str'] = '$__ismain__ = ' + str(ismain_default)
                            content[0]['strings'] = parser.parse_string('$__ismain__ = ' + str(ismain_default))
                            content[0]['args_str'] = '= ' + str(ismain_default)
                            content[0]['args'] = ['=', str(ismain_default)]
                            if len(content) > 1 and self != None:
                                if content[-1]['str'].startswith('$__ismain__ = '):
                                    content[-1]['str'] = '$__ismain__ = ' + str(self.get_var('__ismain__'))
                                    content[-1]['args_str'] = '= ' + str(self.get_var('__ismain__'))
                                    content[-1]['args'] = ['=', str(self.get_var('__ismain__'))]
        except:
            pass

        if content == False:
            is_new_cache = True
            f = open(path, 'r')
            content = f.read()
            f.close()
            if self != None:
                content = '$__ismain__ = ' + str(ismain_default) + '; $__file__ = ' + repr(path.replace('\\', '\\\\')) + '\n$__dir__ = ' + repr(os.path.dirname(path).replace('\\', '\\\\')) + '\n' + content
                content += '\n$__file__ = ' + repr(self.get_var('__file__').replace('\\', '\\\\'))
                content += '\n$__dir__ = ' + repr(self.get_var('__dir__').replace('\\', '\\\\'))
                content += '\n$__ismain__ = ' + str(bool(self.get_var('__ismain__')))

        # write the content on cache
        if is_new_cache:
            content = parser.parse(content, filepath=code_location)
            cache_f = open(the_cache_file, 'wb')
            pickle.dump([file_hash, content], cache_f)
            cache_f.close()

        return content
    except:
        return load(path, code_location, self=self, is_jit_disabled=True)
