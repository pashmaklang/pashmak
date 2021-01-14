#
# modules.py
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

""" Internal modules """

modules = {}

modules["hash"] = """#
# hash.pashm
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
namespace hash
	func blake2b($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.blake2b(self.get_var('value').encode()).hexdigest()")
	endfunc
	func blake2s($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.blake2s(self.get_var('value').encode()).hexdigest()")
	endfunc
	func md5($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.md5(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha1($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha1(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha224($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha224(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha256($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha256(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha384($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha384(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha3_224($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha3_224(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha3_256($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha3_256(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha3_384($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha3_384(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha3_512($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha3_512(self.get_var('value').encode()).hexdigest()")
	endfunc
	func sha512($args)
		$args = format_args($args)
		$value = $args[0]
		python("self.mem = hashlib.sha512(self.get_var('value').encode()).hexdigest()")
	endfunc
	func shake_128($args)
		$args = format_args($args)
		python("self.mem = hashlib.shake_128(str(self.get_var('args')[0]).encode()).hexdigest(self.get_var('args')[1])")
	endfunc
	func shake_256($args)
		$args = format_args($args)
		python("self.mem = hashlib.shake_256(str(self.get_var('args')[0]).encode()).hexdigest(self.get_var('args')[1])")
	endfunc
endns"""
modules["helloworld"] = """#
# __init__.pashm
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
if $__ismain__
    println('Hello world!')
endif"""
modules["math"] = """#
# math.pashm
#
# The Pashmak Project
# This Pashmak module is created and developed by mehan alavi majd <mehan.alavi.majd88@gmail.com> 
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
ns math 
    func acos($num)
        $num = format_args($num)[0]
        python("self.mem = math.acos(self.get_var('num'))")
    endfunc
    func acosh($num)
        $num = format_args($num)[0]
        python("self.mem = math.acosh(self.get_var('num'))")
    endfunc
    func ceil($num)
        $num = format_args($num)[0]
        python("self.mem = math.ceil(self.get_var('num'))")
    endfunc
    func cos($num)
        $num = format_args($num)[0]
        python("self.mem = math.cos(self.get_var('num'))")
    endfunc
    func degrees($num)
        $num = format_args($num)[0]
        python("self.mem = math.degrees(self.get_var('num'))")
    endfunc
    func factorial($num)
        $num = format_args($num)[0]
        python("self.mem = math.factorial(self.get_var('num'))")
    endfunc
    func floor($num)
        $num = format_args($num)[0]
        python("self.mem = math.floor(self.get_var('num'))")
    endfunc
    $pi = python("self.mem = math.pi")
    func pow($args)
        $args = format_args($args)
        $num = $args[0]
        $nextnum = $args[1]
        python("self.mem = math.pow(self.get_var('num'), self.get_var('nextnum'))")
    endfunc
    func sin($num)
        $num = format_args($num)[0]
        python("self.mem = math.sin(self.get_var('num'))")
    endfunc
    func tan($num)
        $num = format_args($num)[0]
        python("self.mem = math.tan(self.get_var('num'))")
    endfunc    
endns"""
modules["os"] = """#
# os.pashm
#
# The Pashmak Project
# This Pashmak module is created by mehan alavi majd <mehan.alavi.majd88@gmail.com> 
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
namespace os
    $env = python("self.mem = os.environ")
    func chdir($args)
        $args = format_args($args)
        python("os.chdir(self.get_var('args')[0]")
    endfunc
    func cpu_count
        python("self.mem = os.cpu_count()")
    endfunc
    func mkdir($args)
        $args = format_args($args)
        python("os.mkdir(self.get_var('args')[0])")
    endfunc
    $curdir = python("self.mem = os.curdir")
    func kill($args)
        $args = format_args($args)
        $pid = $args[0]
        $signal = $args[1]
        python("os.kill(self.get_var('pid'), self.get_var('signal'))")
    endfunc
    func rmdir($args)
        $args = format_args($args)
        python("os.rmdir(self.get_var('args')[0])")
    endfunc
    $osname = python('self.mem = os.name')
    $pardir = python('self.mem = os.path.pardir')
    func isdir($args)
        $args = format_args($args)
        python("self.mem = os.path.isdir(self.get_var('args')[0])")
    endfunc
    func isfile($args)
        $args = format_args($args)
        python("self.mem = os.path.isfile(self.get_var('args')[0])")
    endfunc
    
    func exists($args)
        $args = format_args($args)
        python("self.mem = os.path.exists(self.get_var('args')[0])")
    endfunc
    func cwd
        python("self.mem = os.getcwd()")
    endfunc
endnamespace"""
modules["random"] = """#
# random.pashm
#
# The Pashmak Project
# This Pashmak module is developed by Amirmohammad Ghazi dizaji <amirghazi1387@gmail.com> 
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
    func randint($args)
        $args = format_args($args)
        python("self.mem = random.randint(self.get_var('args')[0], self.get_var('args')[1])")
    endfunc
    func seed($args)
        $args = format_args($args)
        python("random.seed(self.get_var('args')[0])")
    endfunc
    
    func getstate
        python("self.mem = random.getstate()")
    endfunc
    func setstate($args)
        $args = format_args($args)
        python("random.setstate(self.get_var('args')[0])")
    endfunc
    func getrandbits($args)
        $args = format_args($args)
        python("self.mem = random.getrandbits(self.get_var('args')[0])")
    endfunc
    func randrange($args)
        $args = format_args($args)
        python("self.mem = random.randrange(self.get_var('args')[0], self.get_var('args')[1])")
    endfunc
    func choice($args)
        $args = format_args($args)
        python("self.mem = random.choice(self.get_var('args')[0])")
    endfunc
    func choices($args)
        $args = format_args($args)
        python("self.mem = random.choices(self.get_var('args')[0] , self.get_var('args')[1] , self.get_var('args')[2] , self.get_var('args')[3])")
    endfunc
    
    func shuffle($args)
        $args = format_args($args)
        python("random.shuffle(self.get_var('args')[0], self.get_var('args')[1])")
    endfunc
    func sample($args)
        $args = format_args($args)
        python("self.mem = random.sample(self.get_var('args')[0], self.get_var('args')[1])")
    endfunc
    func uniform($args)
        $args = format_args($args)
        python("self.mem = random.uniform(self.get_var('args')[0], self.get_var('args')[1])")
    endfunc
    func triangular($args)
        $args = format_args($args)
        python("self.mem = random.triangular(self.get_var('args')[0], self.get_var('args')[1], self.get_var('args')[2])")
    endfunc
    func random
        python("self.mem = random.random()")
    endfunc
endns"""
modules["stdlib"] = """#
# stdlib.pashm
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
func import
    mem self.import_script(^)
endfunc
func import_once
    mem self.import_script(^, True)
endfunc
func import_run
    mem self.import_script(^, False, ismain_default=True)
endfunc
func import_run_once
    mem self.import_script(^, True, ismain_default=True)
endfunc
func endns
    endnamespace
endfunc
func eval
    mem self.pashmak_eval(^)
endfunc
func assert($args)
    $args = format_args($args)
    $value = $args[0]
    if not $value
        raise(Error('AssertError', 'asserting that false is true'))
    endif
endfunc
func gset($args)
    $args = format_args($args)
	python('self.frames[0]["vars"][' + repr($args[0]) + '] = self.get_var("args")[1]')
endfunc
func gget($args)
    $args = format_args($args)
	python('self.mem = self.frames[0]["vars"][' + repr($args[0]) + ']')
endfunc
func typeof($obj)
    python("self.mem = type(self.get_var('obj'))")
endfunc
func system($args)
    $args = format_args($args)
    $cmd = $args[0]
    python("self.mem = os.system(self.get_var('cmd'))")
endfunc
func python
    rmem exec(^)
endfunc
func required
endfunc
func py_load_file($args)
    $args = format_args($args)
    $path = $args[0]
	python("import importlib.util; spec = importlib.util.spec_from_file_location('pyloadedfile', self.get_var('path')); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); self.mem = m")
endfunc
func fopen($args)
    $args = format_args($args)
    $path = $args[0]
    if len($args) > 1
        $type = $args[1]
    else
        $type = 'r'
    endif
    python("self.mem = open(self.get_var('path'), self.get_var('type'))")
endfunc
func __namespace__
    python("self.mem = self.current_namespace()")
endfunc
namespace pashmak
    func zen
        println('Zen of Pashmak\\n\\
\\n\\
The Zen of Pashmak is a collection of "guiding principles" for writing computer programs that influence the design of the Pashmak programming language. (Like zen of python). This fucking list is written by Mohammad Esmaeili.\\n\\
\\n\\
    Fucking syntax is better than beautiful syntax\\n\\
    English is better than Finglish\\n\\
    Lossless slow is better than loosing fast\\n\\
    CatShit is better than DogShit\\n\\
    DogShit is better than BullShit\\n\\
    Chaos is better than peace\\n\\
    Enthropy is better than order\\n\\
    Crazy is better than logic\\n\\
    Fun is better than boring\\n\\
    Happy is better than sad\\n\\
    Pashm is better than Hash\\n\\
    While is better than Do-While\\n\\
    Space is better than Tab\\n\\
    Also tab is better than Space\\n\\
    -> is better than .\\n\\
    if-else is better than switch-case')
    endfunc
endns
import @stdlib.obj
import @stdlib.io
import @stdlib.func
import @stdlib.class
import @stdlib.exception"""
modules["stdlib.class"] = """#
# class.pashm
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
# The class super tools
namespace class
    func list
        # returns list of classes
        python("self.mem = list(self.classes.keys())")
    endfunc
    func exists($args)
        $args = format_args($args)
        $name = $args[0]
        # checks a class exists or not
        $name = str($name)
        return $name in class.list()
    endfunc
    func delete($args)
        $args = format_args($args)
        $name = $args[0]
        # deletes a class
        $name = str($name)
        if not class.exists($name)
            raise(Error('ClassNotFound', 'class "' + $name + '" not found'))
            return
        endif
        $undeletable_classes = ['Object', 'Error'] # list of undeletable classes
        if $name in $undeletable_classes
            raise(Error('ClassCannotBeDeleted', 'class "' + $name + '" is a builtin class and cannot be deleted'))
        endif
        # delete the class
        python("del self.classes[self.get_var('name')]")
    endfunc
endns"""
modules["stdlib.exception"] = """#
# exception.pashm
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
class Error
    $type
    $messae
    func __init__($args)
        $args = format_args($args)
        $this->type = $args[0]
        $this->message = $args[1]
    endfunc
    func __str__
        return $this->type + ': ' + $this->message
    endfunc
endclass
func raise($args)
    $args = format_args($args)
    $ex = $args[0]
	python("self.raise_error('" + str($ex->type) + "', '" + str($ex->message) + "')")
endfunc"""
modules["stdlib.func"] = """#
# func.pashm
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
# The function super tools
namespace func
    func list
        # returns list of functions
        python("self.mem = list(self.functions.keys())")
    endfunc
    func exists($args)
        $args = format_args($args)
        $name = $args[0]
        # checks a function exists or not
        $name = str($name)
        return $name in func.list()
    endfunc
    func delete($args)
        $args = format_args($args)
        $name = $args[0]
        # deletes a function
        $name = str($name)
        if not func.exists($name)
            raise(Error('FunctionNotFound', 'function "' + $name + '" not found'))
            return
        endif
        $undeletable_functions = ['func.list', 'func.delete', 'func.exists', 'gset', 'py_load_file', 'system', 'typeof', 'required', 'print', 'import', 'println', 'printl', 'import_once', 'mem', 'rmem', 'python', 'endns', 'exit', 'eval', 'raise', 'assert', 'read'] # list of undeletable functions
        if $name in $undeletable_functions
            raise(Error('FunctionCannotBeDeleted', 'function "' + $name + '" is a builtin function and cannot be deleted'))
        endif
        # delete the function
        python("del self.functions[self.get_var('name')]")
    endfunc
endns
func format_args($args)
    if type($args) != tuple
        $args = $args,
    endif
    return $args
endfunc"""
modules["stdlib.io"] = """#
# io.pashm
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
func print
    mem self.print(^)
endfunc
func println($value)
    print(str($value) + '\\n')
endfunc
func printl($value)
    println($value)
endfunc
func perror($value)
    mem self.print($value, file=sys.stderr)
endfunc
func printf($args)
    $args = format_args($args)
    $obj = $args[0]
    $file = python("self.mem = sys.stdout")
    if len($args) > 1
        $file = $args[1]
    endif
    $file->write(str($obj))
endfunc
func out_start
    python("self.out_started = True")
endfunc
func out_end
    python("self.out_started = False")
endfunc
func out_clean
    python("self.out_content = ''")
endfunc
func out_get
    python("self.mem = self.out_content")
endfunc
func out_get_clean
    $content = out_get()
    out_clean()
    return $content
endfunc
func exit($args)
    $args = format_args($args)
    $code = $args[0]
    if typeof($code) != int
        $code = 0
    endif
    python("self.exit_program(self.get_var('code'))")
endfunc
func read
    python("self.io_read()")
endfunc
func var_dump($obj)
    python("class Tmp:\\n    def write(self, value):\\n        current_prog.current_prog.print(str(value))\\npprint.pprint(self.get_var('obj'), Tmp())")
endfunc"""
modules["stdlib.obj"] = """#
# obj.pashm
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
class Object
    func __init__
    endfunc
    func __str__
        return '[PashmakObject name="' + $this->__name__ + '"]'
    endfunc
    func isinstanceof($args)
        $args = format_args($args)
        $class = $args[0]
        if typeof($class) != str
            $class = $class->__name__
        endif
        return $class in $this->__inheritance_tree__
    endfunc
endclass"""
modules["string"] = """#
# string.pashm
#
# The Pashmak Project
# This Pashmak module is created by Sam Ghasemi or sami2020pro <samprogram2007@gmail.com> 
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
ns string
	func concat($args)
		$args = format_args($args)
		return $args[0] + $args[1]
	endfunc 
	
	func remove_last($str)
		$str = format_args($str)[0]
		python("self.mem = self.get_var('str')[:-1] ")
	endfunc
	func remove_first($str)
		$str = format_args($str)[0]
		python("self.mem = self.get_var('str')[1:]")
	endfunc
	func add_last($args)
		$args = format_args($args)
		python("self.mem = self.get_var('args')[0] + self.get_var('args')[1]")
	endfunc
	func add_first($args)
		$args = format_args($args)
		python("self.mem = self.get_var('args')[1] + self.get_var('args')[0]")
	endfunc 
	func length($str)
		$str = format_args($str)[0]
		python("self.mem = len(self.get_var('str'))")
	endfunc
	func cut($args)
		$args = format_args($args)
		python("self.mem = self.get_var('args')[0][self.get_var('args')[1]:self.get_var('args')[2]]")
	endfunc 
	func upcase($str)
		$str = format_args($str)[0]
		python("self.mem = self.get_var('str').upper()")
	endfunc
	func lowcase($str)
		$str = format_args($str)[0]
		python("self.mem = self.get_var('str').lower()")
	endfunc
	func reverse($str)
		$str = format_args($str)[0]
		python("self.mem = self.get_var('str')[::-1]")
	endfunc
	func to_str($var)
		$var = format_args($var)[0]
		python("self.mem = repr(self.get_var('var'))")
	endfunc
endns"""
modules["sys"] = """#
# sys.pashm
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
import @sys.path
namespace sys
    $pashmakinfo = {"version": version.version, "pythoninfo": sys.version.replace("\\n", "")}
    $pashmakexe = sys.argv[0]
endns"""
modules["sys.path"] = """#
# path.pashm
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
namespace sys
    namespace path
        func add($args)
            $args = format_args($args)
            python('os.environ["PASHMAKPATH"] += ":' + str($args[0]) + ':"')
            python("self.bootstrap_modules()")
        endfunc
        func list
            $paths_list = python("self.mem = os.environ['PASHMAKPATH'].strip().split(':')")
            $paths_list = [item.strip() for item in $paths_list if item != '']
            return $paths_list
        endfunc
    endns
endns"""
modules["tengine"] = """#
# __init__.pashm
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
namespace tengine
	func include($args)
		$args = format_args($args)
		$path = $args[0]
		$htmldata = {}
		if len($args) > 1
			$htmldata = $args[1]
		endif
		tengine.run_file($path, True, $htmldata)
	endfunc
	func run_file($args)
		$args = format_args($args)
		$realtime_run = False
		$htmldata = {}
		$path = $args[0]
		if len($args) > 1
			$realtime_run = $args[1]
		endif
		if len($args) > 2
			$htmldata = $args[2]
		endif
		$f = fopen($path, 'r')
		$content = $f->read()
		$f->close()
		return tengine.run($content, $realtime_run, $path, $htmldata)
	endfunc
	func run($args)
		$args = format_args($args)
		$realtime_run = False
		$__htmldir__ = $__dir__
		$__htmlfile__ = $__htmldir__ + '/-'
		$content = $args[0]
		$content = $content->split('\\n', 1)
		if len($content) > 1
			if $content[0]->startswith('#!/')
				$content = $content[1]
			else
				$content = '\\n'->join($content)
			endif
		else
			$content = $content[0]
		endif
		if len($args) > 1
			$realtime_run = $args[1]
		endif
		if len($args) > 2
			$__htmlfile__ = os.path.abspath($args[2])
			$__htmldir__ = os.path.dirname($__htmlfile__)
		endif
		if len($args) > 3
			$htmldata = $args[3]
		endif
		$randstr_1 = '<<<therandomstringfortengine' + str(time.time()) + str(random.random()) + '>>>'
		$randstr_2 = '<<<therandomstringfortengine' + str(time.time()) + str(random.random()) + '>>>'
		$content = $content->replace('\{', $randstr_1)
		$content = $content->replace('\}', $randstr_2)
		$content = $content->replace('{{', '{=')
		$content = $content->replace('}}', '}')
		$parts = $content->split('{')
		$i = 0
		$new_parts = []
		section tengine_loop1
			$tmp = $parts[$i]->split('}', 1)
			if len($tmp) > 1
				$new_parts->append([True, $tmp[0]->replace($randstr_1, '{')->replace($randstr_2, '}')])
				$new_parts->append([False, $tmp[1]->replace($randstr_1, '{')->replace($randstr_2, '}')])
			else
				$new_parts->append([False, $tmp[0]->replace($randstr_1, '{')->replace($randstr_2, '}')])
			endif
			$i = $i + 1
		mem $i < len($parts); gotoif tengine_loop1
		
		$tengine_i = 0
		$tengine_parts = $new_parts
		$tengine_code = ''
		free $i $new_parts $parts $content $randstr_1 $randstr_2 $tmp
		section tengine_loop2
			if $tengine_parts[$tengine_i][0] == True
				if $tengine_parts[$tengine_i][1]
					if $tengine_parts[$tengine_i][1][0] == '='
						$tengine_code = $tengine_code + ('\\nprint(' + $tengine_parts[$tengine_i][1][1:] + ')')
					else
						$tengine_code = $tengine_code + ('\\n' + $tengine_parts[$tengine_i][1])
					endif
				endif
			else
				$tengine_code = $tengine_code + ('\\nprint(base64.b64decode("' + base64.b64encode($tengine_parts[$tengine_i][1]->encode())->decode() + '")->decode())')
			endif
			$tengine_i = $tengine_i + 1
		mem $tengine_i < len($tengine_parts); gotoif tengine_loop2
		free $tengine_i $tengine_parts
		if $realtime_run
			eval($tengine_code)
		else
			out_start()
			eval($tengine_code)
			out_end()
			return out_get_clean()
		endif
	endfunc
endns
if $__ismain__
	if len($argv) > 1
        tengine.run_file($argv[1], True)
	else
        println('tengine: File name is required')
        exit(1)
	endif
endif"""
modules["test"] = """#
# test.pashm
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
namespace test
    func doAssert($args)
        $args = format_args($args)
        $value = $args[0]
        assert($value)
    endfunc
    func assertTrue($args)
        $args = format_args($args)
        $value = $args[0]
        test.doAssert($value)
    endfunc
    func assertFalse($args)
        $args = format_args($args)
        $value = $args[0]
        test.doAssert(not $value)
    endfunc
    func assertEquals($args)
        $args = format_args($args)
        $a = $args[0]
        $b = $args[1]
        test.doAssert($a == $b)
    endfunc
    func assertNotEquals($args)
        $args = format_args($args)
        $a = $args[0]
        $b = $args[1]
        test.doAssert($a != $b)
    endfunc
    func assertEmpty($args)
        $args = format_args($args)
        $value = $args[0]
        test.doAssert($valie == None)
    endfunc
    func assertNotEmpty($args)
        $args = format_args($args)
        $value = $args[0]
        test.doAssert($valie != None)
    endfunc
endns"""
modules["time"] = """#
# time.pashm
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
namespace time
    func time
        python("self.mem = time.time()")
    endfunc
    func sleep($args)
        $args = format_args($args)
        python("time.sleep(self.get_var('args')[0])")
    endfunc
    func ctime
        python("self.mem = time.ctime()")
    endfunc
    func gmtime
        python("self.mem = time.gmtime()")
    endfunc
    func localtime
        python("self.mem = time.localtime()")
    endfunc
endnamespace"""
modules["webserver"] = """#
# webserver.pashm
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
namespace webserver
    class WebServer
        func __init__($args)
            if typeof($args) != tuple
                $args = $args,
            endif
            $this->host = $args[0]
            $this->port = $args[1]
            $this->do_get = None
            $this->do_post = None
        endfunc
        func set_get($func)
            $this->do_get = $func
            return $this
        endfunc
        func set_post($func)
            $this->do_post = $func
            return $this
        endfunc
        func serve
            $py_code = '\\
def serve(host, port, do_get=None, do_post=None):\\n\\
    class TheServer(http.server.BaseHTTPRequestHandler):\\n\\
        def do_GET(self):\\n\\
            if self.get_event != None:\\n\\
                self.get_event(self)\\n\\
\\
        def do_POST(self):\\n\\
            if self.post_event != None:\\n\\
                self.post_event(self)\\n\\
\\
    tmp_TheServer = copy.deepcopy(TheServer)\\n\\
    tmp_TheServer.get_event = do_get\\n\\
    tmp_TheServer.post_event = do_post\\n\\
    webServer = http.server.HTTPServer((host, port), tmp_TheServer)\\n\\
    return webServer\\n\\
self.mem = serve(self.get_var("this").host, self.get_var("this").port, self.get_var("this").do_get, self.get_var("this").do_post)\\n\\
            '
            $this->server = python($py_code)
            $this->server->serve_forever()
        endfunc
    endclass
endns
if $__ismain__
    if '--help' in $argv
        println('Serve a simple webserver for development environment')
        println('')
        println('Usage:   pashmak @webserver <port>')
        println('         pashmak @webserver <host> <port>')
        println('         pashmak @webserver <host> <port> <directory>')
        println('Example: pashmak @webserver 8080')
        println('         pashmak @webserver 0.0.0.0 8080')
        println('         pashmak @webserver 0.0.0.0 8080 path/to/public/html')
        exit()
    endif
    $port = 8000
    $host = 'localhost'
    $dir = os.getcwd()
    if len($argv) > 2
        $host = $argv[1]
        $port = int($argv[2])
        if len($argv) > 3
            $dir = $argv[3]
        endif
    elif len($argv) > 1
        $port = int($argv[1])
    endif
    os.chdir($dir)
    $server = webserver.WebServer($host, $port)
    # a handler for POST and GET methods
    func the_handler($handler)
        if os.path.isfile(os.getcwd() + '/' + $handler->path)
            $full_path = os.path.abspath(os.getcwd() + '/' + $handler->path)
            $mime = mimetypes.guess_type($full_path)[0]
            if $full_path->endswith('.pashm')
                import @sys
                $result = subprocess.run([$sys.pashmakexe, $full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # TODO : use stderr for headers
                $handler->send_response(200)
                $handler->send_header("Content-type", "text/html")
                $handler->end_headers()
                if $result->stderr == None
                    $result->stderr = ''
                endif
                $handler->wfile->write($result->stdout + $result->stderr)
                return
            endif
            try handle_file_error
                $f = open($full_path, 'r')
                $content = $f->read()
                $f->read()
            endtry
            goto after_handle_file_error; section handle_file_error
                $handler->send_response(403)
                $handler->send_header("Content-type", "text/html")
                $handler->end_headers()
                $handler->wfile->write(bytes('403 - Access Denied', "utf-8"))
                return
            section after_handle_file_error
            $handler->send_response(200)
            if $mime == None
                $mime = 'text/plain'
            endif
            $handler->send_header("Content-type", $mime)
            $handler->end_headers()
            $handler->wfile->write(bytes($content, "utf-8"))
            return
        else
            $handler->send_response(404)
            $handler->send_header("Content-type", "text/html")
            $handler->end_headers()
            $handler->wfile->write(bytes('404 - Not Found', "utf-8"))
            return
        endif
    endfunc
    # set request handlers
    $server->set_get(the_handler)
    $server->set_post(the_handler)
    # start the server
    println('Serving the development server on http://' + $host + ':' + str($port) + ' - Do not use this on production')
    $server->serve()
endif"""
