# Stdlib
`stdlib` is a very important and useful module.
this module make the pashmak syntax easy.

this module not need to be import because it will import automaticaly.

look at this example:

```bash
# print
print "hello world\n"; # INSTEAD OF `mem 'hello world\n'; out ^;`

# println
println "hello world"; # without using `\n` in the end of string

# import
import 'somefile.pashm';
import '@hash'; # INSTEAD OF `mem '@hash'; include ^`

# exit
exit; # exits program
exit 2; # exits with exit code
# INSTEAD OF `return;` and `return 2;`

# py
py "print('hello world from python')"; # INSTEAD OF `mem "print('hello world from python')"; python ^`

# sys
sys 'ls /tmp'; # INSTEAD OF `mem 'ls /tmp'; system ^;`

# std.chdir
std.chdir "/tmp"; # INSTEAD OF `mem '/tmp'; chdir ^;`

# std.eval
std.eval 'mem "hi"\; out ^\;'; # INSTEAD OF `mem 'mem "hi"\; out ^\;'; eval ^`

# gset
gset 'somevar', 'new global value'; # you learned this command in functions section
```

##### raising errors
```bash
print 'program started\n';

raise 'MyError', 'this is my error';

print 'this will not print\n';
```

output:

```
progrma started
MyError:
	this is my error
```

the `raise` function can raise errors in program

first argument `'TheError'` is error type and second error `'this is my error'` is error message.

##### asserting
the stdlib has a function named `assert`. this function is for testing and asserting

look at this example:

```bash
assert 2 == 3;
```

output:

```
AssertError:
	asserting that false is true
```

you can pass a condition or boolean value to assert function. if that is True, this function do nothing:

```bash
assert 2 == 2;
assert True;

$age = 18;
assert $age > 10;
```

the above code do nothing, because all of values passed to assert are True.

but if that value is false, program raises `AssertError`. this is helpful for testing.

##### finish

this module includes some functions to make the pashmak syntax better.

also look at this example about print:

```bash
print 'enter your name: ';
$name; read $name;

print 'hello ' + $name + '\n';

```
