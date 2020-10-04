#
# modules.py
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


modules = {}

modules["random"] = """alias random.randint;
    set $tmp_random.randint;
    copy $tmp_random.randint;
    py 'self.mem = random.randint(' + str($tmp_random.randint[0]) + ',' + str($tmp_random.randint[1]) + ')';
endalias;

alias random.random;
    py 'self.mem = random.random()';
endalias;
"""
modules["time"] = """alias time.time;
    py 'self.mem = time.time()';
endalias;

alias time.sleep;
    set $tmp_time_sleep_for; copy $tmp_time_sleep_for;
    py 'self.mem = time.sleep(' + str($tmp_time_sleep_for) + ')';
endalias;
"""
modules["file"] = """
alias file.open;
    set $args; copy $args;
    mem open("' + $args[0] + '" , "' + $args[1] + '");
    free $args;
endalias;

alias file.close;
    set $file; copy $file;
    mem $file.close();
    free $file;
endalias;

alias file.read;
    set $file; copy $file;
    mem $file.read();
    free $file;
endalias;

alias file.write;
    set $args; copy $args;
    mem $args[0].write(self.get_var("args")[1]);
    free $args;
endalias;
"""
modules["hash"] = """
alias hash.sha256;
	set $tmp_hash_sha256_value; copy $tmp_hash_sha256_value;
	py 'self.mem = hashlib.sha256("' + $tmp_hash_sha256_value + '".encode()).hexdigest()';
	free $tmp_hash_sha256_value;
endalias;

alias hash.md5;
	set $tmp_hash_md5_value; copy $tmp_hash_md5_value;
	py 'self.mem = hashlib.md5("' + $tmp_hash_md5_value + '".encode()).hexdigest()';
	free $tmp_hash_md5_value;
endalias;
"""
modules["stdlib"] = """
alias print;
    out ^;
endalias;

alias import;
    include ^;
endalias;

alias exit;
    return ^;
endalias;

alias py;
    python ^;
endalias;

alias sys;
    system ^;
endalias;

alias std.chdir;
    chdir ^;
endalias;

alias std.eval;
    eval ^;
endalias;

alias raise;
	set $tmp_stdlib_raise_exdata; copy $tmp_stdlib_raise_exdata;
	mem "self.raise_error('" + $tmp_stdlib_raise_exdata[0] + "' , '" + $tmp_stdlib_raise_exdata[1] + "' , op)";
    python ^;
    free $tmp_stdlib_raise_exdata;
endalias;

alias assert;
    gotoif tmp_assert_after_section;
    raise ['AssertError' , 'asserting that false is true'];
    section tmp_assert_after_section;
endalias;

alias gset;
	set $args; copy $args;
	mem 'self.variables["' + $args[0] + '"] = self.get_var("args")[1]';
	python ^;
endalias;
"""