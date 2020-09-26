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
    set $random.randint.temp;
    copy $random.randint.temp;
    mem 'self.mem = random.randint(' + str($random.randint.temp[0]) + ',' + str($random.randint.temp[1]) + ')';
    python ^;
endalias;

alias random.random;
    mem 'self.mem = random.random()';
    python ^;
endalias;
"""
modules["time"] = """alias time.time;
    mem 'self.mem = time.time()'; python ^;
endalias;

alias time.sleep;
    set $tmp_time_sleep_for; copy $tmp_time_sleep_for;
    mem 'self.mem = time.sleep(' + str($tmp_time_sleep_for) + ')'; python ^;
endalias;
"""
modules["hash"] = """
alias hash.sha256;
	set $tmp_hash_sha256_value; copy $tmp_hash_sha256_value;
	mem 'self.mem = hashlib.sha256("' + $tmp_hash_sha256_value + '".encode()).hexdigest()'; python ^;
	free $tmp_hash_sha256_value;
endalias;

alias hash.md5;
	set $tmp_hash_md5_value; copy $tmp_hash_md5_value;
	mem 'self.mem = hashlib.md5("' + $tmp_hash_md5_value + '".encode()).hexdigest()'; python ^;
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
"""