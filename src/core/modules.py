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