# Internal Modules
pashmak has some internal libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `import` function.

look at this example:

```bash
import '@hash'
import "@module_name"
import "@module1", '@module2'

# also you can import modules without quotes
import @sys
import @hash, @mymodule

# also you can import modules like scripts under the namespaces
namespace Foo
    import '@hash'
endns

# ...
```

you have to give name of module with a `@` before that to the include command.

### hash module
with hash module, you can calculate hash sum of values:

```bash
import @hash

hash.sha256("hello") # also you can use hash.md5 and...
println(^) # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# OR
println(%{hash.sha256 "hello"}%)
```

##### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this function calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

#### another hash algos
- hash.blake2b(string)
- hash.blake2s(string)
- hash.md5(string)
- hash.sha1(string)
- hash.sha224(string)
- hash.sha256(string)
- hash.sha384(string)
- hash.sha3_224(string)
- hash.sha3_256(string)
- hash.sha3_384(string)
- hash.sha3_512(string)
- hash.sha512(string)
- hash.shake_128(string, length)
- hash.shake_256(string, length)

### time module
with this module, you can work with time.

##### time.time
this function gives you current UNIX timestamp:

```bash
import @time

println(%{time.time()}%) # output is some thing like this: `1600416438.687201`
```

when you call this function, this function puts the unix timestamp into mem and you can access and use that.

##### time.sleep
this function sleeps for secounds:

```bash
import @time

time.sleep(2) # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this function, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` function, then program will sleep for value of `mem` as secounds

#### Another time functions
- time.ctime
- time.gmtime
- time.localtime

### random module
this module makes random numbers

##### random.randint
```bash
import @random

# generates a random int between 1 and 10
println(%{random.randint(1, 10)}%)
```

##### random.random
```bash
import @random

# generates a random float less that 1
$rand = %{random.random}%
println($rand)
```

### test module
the `test` module has some assertion functions to testing.

##### default `assert` function
this function is a function in the pashmak. this function gets a value and asserts that is true:

```bash
# NOTE: you don't need to import anything for use this function
assert(2 == 2) # ok
assert(4 > 1) # ok
assert(True) # ok
assert('foo' == 'bar') # error: AssertError
```

##### test.assertTrue
asserts true:

```bash
import @test

test.assertTrue(True)
test.assertTrue(5 == 5)
test.assertTrue(10 > 5)
```

above code will be run without error.

this code will get `AssertError`:

```bash
test.assertTrue(False)
test.assertTrue(3 == 2)
```

##### test.assertFalse
this function is reverse of `test.assertTrue`.

```bash
test.assertFalse(False) # run be run without error
test.assertFalse(3 == 2) # run be run without error
test.assertFalse(2 == 2) # AssertionError
```

##### test.assertEquals
this function asserts two values equals.

```bash
# two arguments should be passed:
test.assertEquals('hello', 'hello') # successful
test.assertEquals(2, 2) # successful
test.assertEquals('foo', 'bar') # AssertionError
```

##### test.assertNotEquals
this function is reverse of `test.assertEquals`.

```bash
test.assertNotEquals('foo', 'bar') # successful
test.assertNotEquals(2, 7) # successful
test.assertNotEquals(2, 2) # AssertionError
```

##### test.assertEmpty
asserts the value is empty.

```bash
test.assertEmpty(None)
test.assertEmpty('hello') # error
```

##### test.assertNotEmpty
asserts value is not empty

```bash
test.assertNotEmpty('hello')
test.assertNotEmpty(None) # error
```

### sys module
this module has some functions to manage pashmak internal envrinonment.

#### sys.path module
this module is for manage module paths. you can add new module paths and load modules from everywhere at runtime with this module.

to know about this module, go to next section [Module path system](#module-path-system).

#### `$sys.pashmakinfo`, access to pashmakinfo

if you want to access to pashmak interpreter info, `sys` module has a variable named `pashmakinfo`:

```bash
import @sys

println($sys.pashmakinfo)
```

output is something like this:

```
{'version': 'vx.y.z', 'pythoninfo': 'x.y.z (default, Jul x y, a:b:c) [GCC x.y.x]'}
```

this variable is a dictonary.
for example, to access pashmak version:

```bash
import @sys

println($sys.pashmakinfo['version'])
```

output:

```
v1.x.y
```

and `$sys.pashmakinfo['pythoninfo']` shows info of python.

## Python standard modules
you can use this python standard modules in pashmak directly in your code:

- `os`
- `time`
- `hashlib`
- `random`
- `datetime`

for example:

```bash
println(os.getuid())
println(random.random())
println('hash is ' + hashlib.sha256('hello'.encode()).hexdigest())
$cwd = os.getcwd()
$time = time.time() - 100
# ...
```

this is very useful!

## Module path system
module path is a system to add pashmak scripts as modules to pashmak. for example, you have an directory named `/var/lib/pashmak_modules` and there is an file named `/var/lib/pashmak_modules/mymodule.pashm`. this file is a pashmak script. now, how to add that pashmak script to pashmak as module?

for example, we want to import that module:

```bash
import '@mymodule'
```

to do this, you have to add directory `/var/lib/pashmak_modules` to pashmak path:

```bash
PASHMAKPATH=/var/lib/pashmak_modules pashmak my_program.pashm
```

to add an directory to pashmak path, you have to set that directory to environment variable `PASHMAKPATH`:

```
PASHMAKPATH=/path/to/first/dir:/path/to/another/dir:/another/dir2...
```

you can seprate paths with `:`.

next, pashmak interpreter loads modules from that directories. how? pashmak loads pashmak files with `.pashm` extension as module. for example, if name of file is `my_module.pashm`, you can import that with `import "@my_module"`.

also you can import an directory as module. for example, `/usr/lib/pashmak_modules` is in the module path. and there is a directory in `/usr/lib/pashmak_modules/mymodule/`. if you import `import "@mymodule"`, pashmak uses `/usr/lib/pashmak_modules/mymodule/__init__.pashm` file in that directory as module main file. you can load another scripts of your module in this file.

for example:

##### __init__.pashm:

```bash
import $__dir__ + '/core.pashm'
import $__dir__ + '/another-file.pashm'
# ...
# or whatever you want to do
```

### Default paths
the default module paths in pashmak are:

- `<home-directory>/.local/lib/pashmak_modules`
- `/usr/lib/pashmak_modules` (only in UNIX systems)

### Show list of available modules
to see list of available modules, run this command:

```bash
pashmak -m
# or
pashmak --modules
```

### Adding module paths at runtime (sys.path module)
there is an namespace named `sys.path` in the `sys` module, this module is for adding new module paths at the runtime.
with this feature, you can add another directories to your path and load modules from them in your program.

for example:

```bash
import @sys

sys.path.add('/home/parsa/my-directory');
```

in above code, directory `/home/parsa/my-directory` will be added to the module path. after this action, you can import modules of that directory.

for example, we have `/home/parsa/my-directory/mylib.pashm` module and we can import that:

```bash
import '@sys'

sys.path.add('/home/parsa/my-directory');

import '@mylib'

# do whatever you want
```

this system is very helpful, specialy when you want to add your local modules from an directory in your project.

for example, i have an project and there is an directory named `pashmak_modules` contains local library. i can add this directory to module path in my code start point:

```bash
import $__dir__ + '/pashmak_modules/'

# now i can import libraries from pashmak_modules directory
```

also you can get list of module paths:

```bash
import '@sys'

$module_paths = %{sys.path.list}%

println($module_paths)
```

output:

```
['/path1', '/path2', '...']
```

### Another useful libraries written by others

- The [polor-pashm](https://github.com/sami2020pro/polor-pashm) library by [sami2020pro](https://github.com/sami2020pro)
