#
# modules.py
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

modules["hash"] = """namespace hash
func blake2b($value)
python("self.mem = hashlib.blake2b(self.get_var('value').encode()).hexdigest()")
endfunc
func blake2s($value)
python("self.mem = hashlib.blake2s(self.get_var('value').encode()).hexdigest()")
endfunc
func md5($value)
python("self.mem = hashlib.md5(self.get_var('value').encode()).hexdigest()")
endfunc
func sha1($value)
python("self.mem = hashlib.sha1(self.get_var('value').encode()).hexdigest()")
endfunc
func sha224($value)
python("self.mem = hashlib.sha224(self.get_var('value').encode()).hexdigest()")
endfunc
func sha256($value)
python("self.mem = hashlib.sha256(self.get_var('value').encode()).hexdigest()")
endfunc
func sha384($value)
python("self.mem = hashlib.sha384(self.get_var('value').encode()).hexdigest()")
endfunc
func sha3_224($value)
python("self.mem = hashlib.sha3_224(self.get_var('value').encode()).hexdigest()")
endfunc
func sha3_256($value)
python("self.mem = hashlib.sha3_256(self.get_var('value').encode()).hexdigest()")
endfunc
func sha3_384($value)
python("self.mem = hashlib.sha3_384(self.get_var('value').encode()).hexdigest()")
endfunc
func sha3_512($value)
python("self.mem = hashlib.sha3_512(self.get_var('value').encode()).hexdigest()")
endfunc
func sha512($value)
python("self.mem = hashlib.sha512(self.get_var('value').encode()).hexdigest()")
endfunc
func shake_128($value)
python("self.mem = hashlib.shake_128(str(self.get_var('value')[0]).encode()).hexdigest(self.get_var('value')[1])")
endfunc
func shake_256($value)
python("self.mem = hashlib.shake_256(str(self.get_var('value')[0]).encode()).hexdigest(self.get_var('value')[1])")
endfunc
endns"""
modules["random"] = """namespace random
func randint($args)
python("self.mem = random.randint(self.get_var('args')[0], self.get_var('args')[1])")
endfunc
func random
python("self.mem = random.random()")
endfunc
endns"""
modules["stdlib"] = """class Object
func __init__
endfunc
func __str__
return '[PashmakClass name="' + $this->__name__ + '"]'
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
func exit($code)
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
func raise($exdata)
python("self.raise_error('" + str($exdata->type) + "', '" + str($exdata->message) + "')")
endfunc
func assert($value)
if not $value
raise(Error('AssertError', 'asserting that false is true'))
endif
endfunc
func gset($args)
python('self.threads[0]["vars"]["' + str($args[0]) + '"] = self.get_var("args")[1]')
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
func chdir($path)
python("self.mem = os.chdir(self.get_var('path'))")
endfunc
func typeof($obj)
python("self.mem = type(self.get_var('obj'))")
endfunc
func system($cmd)
python("self.mem = os.system(self.get_var('cmd'))")
endfunc
func python
rmem exec(^)
endfunc
func required
endfunc
func read
read
endfunc
func py_load_file($path)
python("import importlib.util\; spec = importlib.util.spec_from_file_location('pyloadedfile', self.get_var('path'))\; m = importlib.util.module_from_spec(spec)\; spec.loader.exec_module(m)\; self.mem = m")
endfunc
func fopen($args)
if typeof($args) != list and typeof($args) != tuple
$args = [$args]
endif
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
$this->type = $args[0]
$this->message = $args[1]
endfunc
func __str__
return $this->type + ': ' + $this->message
endfunc
endclass
namespace func
func list
python("self.mem = list(self.functions.keys())")
endfunc
func exists($name)
$name = str($name)
return $name in func.list()
endfunc
func delete($name)
$name = str($name)
if not func.exists($name)
raise(Error('FunctionNotFound', 'function "' + $name + '" not found'))
return
endif
$undeletable_functions = ['func.list', 'func.delete', 'func.exists', 'gset', 'py_load_file', 'system', 'typeof', 'required', 'print', 'import', 'println', 'printl', 'import_once', 'mem', 'rmem', 'python', 'endns', 'exit', 'eval', 'raise', 'assert', 'read']
if $name in $undeletable_functions
raise(Error('FunctionCannotBeDeleted', 'function "' + $name + '" is a builtin function and cannot be deleted'))
endif
python("del self.functions[self.get_var('name')]")
endfunc
endns
namespace class
func list
python("self.mem = list(self.classes.keys())")
endfunc
func exists($name)
$name = str($name)
return $name in class.list()
endfunc
func delete($name)
$name = str($name)
if not class.exists($name)
raise(Error('ClassNotFound', 'class "' + $name + '" not found'))
return
endif
$undeletable_classes = ['Object', 'Error']
if $name in $undeletable_classes
raise(Error('ClassCannotBeDeleted', 'class "' + $name + '" is a builtin class and cannot be deleted'))
endif
python("del self.classes[self.get_var('name')]")
endfunc
endns"""
modules["sys"] = """namespace sys
$pashmakinfo = {"version": version.version, "pythoninfo": sys.version.replace("\\n", "")}
namespace path
func add($new_path)
python('os.environ["PASHMAKPATH"] += ":' + str($new_path) + ':"')
python("self.bootstrap_modules()")
endfunc
func list
$paths_list = python("self.mem = os.environ['PASHMAKPATH'].strip().split(':')")
$paths_list = [item.strip() for item in $paths_list if item != '']
return $paths_list
endfunc
endns
endns"""
modules["test"] = """namespace test
func doAssert($value)
assert($value)
endfunc
func assertTrue($value)
test.doAssert($value)
endfunc
func assertFalse($value)
test.doAssert(not $value)
endfunc
func assertEquals($args)
$a = $args[0]
$b = $args[1]
test.doAssert($a == $b)
endfunc
func assertNotEquals($args)
$a = $args[0]
$b = $args[1]
test.doAssert($a != $b)
endfunc
func assertEmpty($value)
test.doAssert($valie == None)
endfunc
func assertNotEmpty($value)
test.doAssert($valie != None)
endfunc
endns"""
modules["time"] = """namespace time
func time
python("self.mem = time.time()")
endfunc
func sleep($time_to_sleep)
python("time.sleep(self.get_var('time_to_sleep'))")
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
