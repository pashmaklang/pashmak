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
endclass
func print
    mem self.print(^)
endfunc
func import
    mem self.import_script(^)
endfunc
func import_once
    mem self.import_script(^, True)
endfunc
func exit($args)
    $args = format_args($args)
    $code = $args[0]
    if typeof($code) != int
        $code = 0
    endif
    python("self.exit_program(self.get_var('code'))")
endfunc
func eval
    mem self.pashmak_eval(^)
endfunc
func endns
    endnamespace
endfunc
func raise($args)
    $args = format_args($args)
    $ex = $args[0]
	python("self.raise_error('" + str($ex->type) + "', '" + str($ex->message) + "')")
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
	python('self.frames[0]["vars"]["' + str($args[0]) + '"] = self.get_var("args")[1]')
endfunc
func println($value)
    print(str($value) + '\\n')
endfunc
func printl($value)
    println($value)
endfunc
func cwd
    python("self.mem = os.getcwd()")
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
func read
    python("self.io_read()")
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
endns
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
func __namespace__
    python("self.mem = self.current_namespace()")
endfunc
func var_dump($obj)
    python("class Tmp:\\n    def write(self, value):\\n        current_prog.current_prog.print(str(value))\\npprint.pprint(self.get_var('obj'), Tmp())")
endfunc
func format_args($args)
    if type($args) != tuple
        $args = $args,
    endif
    return $args
endfunc"""
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
namespace sys
    $pashmakinfo = {"version": version.version, "pythoninfo": sys.version.replace("\\n", "")}
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
\\
    try:\\n\\
        webServer.serve_forever()\\n\\
    except KeyboardInterrupt:\\n\\
        pass\\n\\
\\
    webServer.server_close()\\n\\
\\
serve(self.get_var("this").host, self.get_var("this").port, self.get_var("this").do_get, self.get_var("this").do_post)\\n\\
            '
            python($py_code)
        endfunc
    endclass
endns"""
