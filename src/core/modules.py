#
# modules.py
#
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

""" Internal modules """

modules = {}

modules["file"] = """#
# file.pashm
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
namespace file
    func open ($args)
        mem open($args[0], $args[1])
    endfunc
    func close ($file)
        mem "self.get_var('file').close()"; python ^
    endfunc
    func read ($file)
        mem "self.mem = self.get_var('file').read()"; python ^
    endfunc
    func write ($args)
        mem $args[0].write($args[1])
    endfunc
endns
"""
modules["hash"] = """#
# hash.pashm
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
namespace hash
	func blake2b ($value)
		py 'self.mem = hashlib.blake2b("' + $value + '".encode()).hexdigest()'
	endfunc
	func blake2s ($value)
		py 'self.mem = hashlib.blake2s("' + $value + '".encode()).hexdigest()'
	endfunc
	func md5 ($value)
		py 'self.mem = hashlib.md5("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha1 ($value)
		py 'self.mem = hashlib.sha1("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha224 ($value)
		py 'self.mem = hashlib.sha224("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha256 ($value)
		py 'self.mem = hashlib.sha256("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha384 ($value)
		py 'self.mem = hashlib.sha384("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha3_224 ($value)
		py 'self.mem = hashlib.sha3_224("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha3_256 ($value)
		py 'self.mem = hashlib.sha3_256("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha3_384 ($value)
		py 'self.mem = hashlib.sha3_384("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha3_512 ($value)
		py 'self.mem = hashlib.sha3_512("' + $value + '".encode()).hexdigest()'
	endfunc
	func sha512 ($value)
		py 'self.mem = hashlib.sha512("' + $value + '".encode()).hexdigest()'
	endfunc
	func shake_128 ($value)
		py 'self.mem = hashlib.shake_128("' + str($value[0]) + '".encode()).hexdigest(' + str($value[1]) + ')'
	endfunc
	func shake_256 ($value)
		py 'self.mem = hashlib.shake_256("' + str($value[0]) + '".encode()).hexdigest(' + str($value[1]) + ')'
	endfunc
endns
"""
modules["random"] = """#
# random.pashm
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
namespace random
    func randint ($args)
        py 'self.mem = random.randint(' + str($args[0]) + ',' + str($args[1]) + ')'
    endfunc
    func random
        py 'self.mem = random.random()'
    endfunc
endns
"""
modules["stdlib"] = """#
# stdlib.pashm
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
func print
    out ^
endfunc
func import
    include ^
endfunc;
func exit ($code)
    mem type($code) != int; gotoif stdlib_exit_default_exit_with_zero_code
    return $code
    section stdlib_exit_default_exit_with_zero_code
    return 0
endfunc
func py
    python ^
endfunc
func sys
    system ^
endfunc
func std_chdir
    chdir ^
endfunc
func std_eval
    eval ^
endfunc
func endns
    endnamespace
endfunc
func raise ($exdata)
	mem "self.raise_error('" + $exdata[0] + "', '" + $exdata[1] + "', op)"
    python ^
endfunc
func assert
    gotoif tmp_assert_after_section
    raise 'AssertError', 'asserting that false is true'
    section tmp_assert_after_section
endfunc
func gset ($args)
	mem 'self.variables["' + $args[0] + '"] = self.get_var("args")[1]'
	python ^
endfunc
func println ($value)
    print str($value) + '\\n'
endfunc
func printl ($value)
    println $value
endfunc
"""
modules["sys"] = """#
# sys.pashm
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
namespace sys
    $pashmakinfo = {"version": version.version, "pythoninfo": sys.version.replace("\\n", "")}
    namespace path
        func add $new_path
            mem 'os.environ["PASHMAKPATH"] += ":' + str($new_path) + ':"'; python ^
            mem 'self.bootstrap_modules()'; python ^
        endfunc
        func list
            $paths_list = os.environ["PASHMAKPATH"]
            $paths_list = $paths_list.strip().split(':')
            $paths_list = [item.strip() for item in $paths_list if item != '']
            mem $paths_list
        endfunc
    endns
endns
"""
modules["test"] = """#
# test.pashm
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
namespace test
    func doAssert $value
        assert $value
    endfunc
    func assertTrue $value
        test.doAssert $value
    endfunc
    func assertFalse $value
        test.doAssert not $value
    endfunc
    func assertEquals $args
        $a = $args[0]
        $b = $args[1]
        test.doAssert $a == $b
    endfunc
    func assertNotEquals $args
        $a = $args[0]
        $b = $args[1]
        test.doAssert $a != $b
    endfunc
    func assertEmpty $value
        test.doAssert $valie == None
    endfunc
    func assertNotEmpty $value
        test.doAssert $valie != None
    endfunc
endns
"""
modules["time"] = """#
# time.pashm
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
namespace time
    func time
        py 'self.mem = time.time()'
    endfunc
    func sleep ($time_to_sleep)
        py 'self.mem = time.sleep(' + str($time_to_sleep) + ')'
    endfunc
    func ctime
        py 'self.mem = time.ctime()'
    endfunc
    func gmtime
        py 'self.mem = time.gmtime()'
    endfunc
    func localtime
        py 'self.mem = time.localtime()'
    endfunc
endnamespace
"""
