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

modules["random"] = """
namespace random;
    func randint;
        set $args; copy $args;
        py 'self.mem = random.randint(' + str($args[0]) + ',' + str($args[1]) + ')';
    endfunc;
    func random;
        py 'self.mem = random.random()';
    endfunc;
endnamespace;
"""
modules["time"] = """
namespace time;
    func time;
        py 'self.mem = time.time()';
    endfunc;
    func sleep;
        set $tmp_time_sleep_for; copy $tmp_time_sleep_for;
        py 'self.mem = time.sleep(' + str($tmp_time_sleep_for) + ')';
    endfunc;
endnamespace;
"""
modules["file"] = """
namespace file;
    func open;
        set $args; copy $args;
        mem open($args[0] , $args[1]);
        free $args;
    endfunc;
    func close;
        set $file; copy $file;
        mem $file.close();
        free $file;
    endfunc;
    func read;
        set $file; copy $file;
        mem $file.read();
        free $file;
    endfunc;
    func write;
        set $args; copy $args;
        mem $args[0].write($args[1]);
        free $args;
    endfunc;
endnamespace;
"""
modules["hash"] = """
namespace hash;
	func sha256;
		set $value; copy $value;
		py 'self.mem = hashlib.sha256("' + $value + '".encode()).hexdigest()';
		free $value;
	endfunc;
	func md5;
		set $value; copy $value;
		py 'self.mem = hashlib.md5("' + $value + '".encode()).hexdigest()';
		free $value;
	endfunc;
endnamespace;
"""
modules["stdlib"] = """
func print;
    out ^;
endfunc;
func import;
    include ^;
endfunc;
func exit;
    return ^;
endfunc;
func py;
    python ^;
endfunc;
func sys;
    system ^;
endfunc;
func std.chdir;
    chdir ^;
endfunc;
func std.eval;
    eval ^;
endfunc;
func endns;
    endnamespace;
endfunc;
func raise;
	set $exdata; copy $exdata;
	mem "self.raise_error('" + $exdata[0] + "' , '" + $exdata[1] + "' , op)";
    python ^;
    free $exdata;
endfunc;
func assert;
    gotoif tmp_assert_after_section;
    raise ['AssertError' , 'asserting that false is true'];
    section tmp_assert_after_section;
endfunc;
func gset;
	set $args; copy $args;
	mem 'self.variables["' + $args[0] + '"] = self.get_var("args")[1]';
	python ^;
endfunc;
"""