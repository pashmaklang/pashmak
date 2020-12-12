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
        mem $file->close()
    endfunc
    func read ($file)
        mem $file->read()
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
		mem hashlib.blake2b($value->encode())->hexdigest()
	endfunc
	func blake2s ($value)
		mem hashlib.blake2s($value->encode())->hexdigest()
	endfunc
	func md5 ($value)
		mem hashlib.md5($value->encode())->hexdigest()
	endfunc
	func sha1 ($value)
		mem hashlib.sha1($value->encode())->hexdigest()
	endfunc
	func sha224 ($value)
		mem hashlib.sha224($value->encode())->hexdigest()
	endfunc
	func sha256 ($value)
		mem hashlib.sha256($value->encode())->hexdigest()
	endfunc
	func sha384 ($value)
		mem hashlib.sha384($value->encode())->hexdigest()
	endfunc
	func sha3_224 ($value)
		mem hashlib.sha3_224($value->encode())->hexdigest()
	endfunc
	func sha3_256 ($value)
		mem hashlib.sha3_256($value->encode())->hexdigest()
	endfunc
	func sha3_384 ($value)
		mem hashlib.sha3_384($value->encode())->hexdigest()
	endfunc
	func sha3_512 ($value)
		mem hashlib.sha3_512($value->encode())->hexdigest()
	endfunc
	func sha512 ($value)
		mem hashlib.sha512($value->encode())->hexdigest()
	endfunc
	func shake_128 ($value)
		mem hashlib.shake_128(str($value[0])->encode()).hexdigest($value[1])
	endfunc
	func shake_256 ($value)
		mem hashlib.shake_256(str($value[0])->encode()).hexdigest($value[1])
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
        mem random.randint($args[0], $args[1])
    endfunc
    func random
        mem random.random()
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
class Object
endclass
func print
    mem self.print(^)
endfunc
func import
    include ^
endfunc;
func exit ($code)
    # TODO : delete `return` operation and exit by python code
    if type($code) == int
        return $code
    else
        return 0
    endif
endfunc
func eval
    # TODO : delete `core_eval` function and use python function
    core_eval ^
endfunc
func endns
    endnamespace
endfunc
func raise ($exdata)
	mem "self.raise_error('" + $exdata[0] + "', '" + $exdata[1] + "', self.operations[self.current_step])"
    python ^
endfunc
func assert ($value)
    if not $value
        raise 'AssertError', 'asserting that false is true'
    endif
endfunc
func gset ($args)
	python 'self.variables["' + str($args[0]) + '"] = self.get_var("args")[1]'
endfunc
func println ($value)
    print str($value) + '\\n'
endfunc
func printl ($value)
    println $value
endfunc
func cwd
    mem os.getcwd()
endfunc
func chdir ($path)
    mem os.chdir($path)
endfunc
func typeof ($obj)
    mem type($obj)
endfunc
func system ($cmd)
    mem os.system($cmd)
endfunc
func python
    rmem exec(^)
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
            python 'os.environ["PASHMAKPATH"] += ":' + str($new_path) + ':"'
            mem self.bootstrap_modules()
        endfunc
        func list
            $paths_list = os.environ["PASHMAKPATH"]->strip()->split(':')
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
        mem time.time()
    endfunc
    func sleep ($time_to_sleep)
        mem time.sleep($time_to_sleep)
    endfunc
    func ctime
        mem time.ctime()
    endfunc
    func gmtime
        mem time.gmtime()
    endfunc
    func localtime
        mem time.localtime()
    endfunc
endnamespace
"""
