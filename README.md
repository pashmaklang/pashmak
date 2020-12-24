
##### NOTE: this file is auto generated from `doc` folder. do not change it directly. If you want to edit documentation, edit `doc/` folder files. your changes will built from that folder into this file.

# Pashmak Programming Language
Hi there. this is Pashmak programming language. Pashmak is an interpreter written in Python.
Pashmak scripts have cool and pashmaki syntax.

### hello world!
this is a simple hello world script in pashmak:

```bash
println('hello world')
```

## Online interpreter
if you want to test pashmak without installing and need to run it online, go to [Pashmak online interpreter](https://pashmio-parsampsh.fandogh.cloud/)

## Authors
pashmak is written by [parsampsh](https://github.com/parsampsh) and [contributors](https://github.com/pashmaklang/pashmak/graphs/contributors)

## Contributing
if you want to contribute to this project, read [Contributing Guide](CONTRIBUTING.md)

## Changelog
to see pashmak versions changelog, read [Changelog](CHANGELOG.md)

## Security Policy
if you detected an bug or vulnearability, read [Pashmak Security Policy](/SECURITY.md).

# Documentation
read the following Documentation to learn pashmak.

### Table of contents
- [Installation](#installation)
- [Basics](#basics)
- [Variables](#variables)
- [Constants](#Constants)
- [Read Input From User](#read-input-from-user)
- [Sections](#sections)
- [If statements](#if-elif-else-statement)
- [Functions](#functions)
- [Arrays](#arrays)
- [Try-Endtry statement](#try-and-endtry-statement)
- [OS Commands](#os-commands)
- [Importing scripts](#importing-scripts)
- [Namespaces](#namespaces)
- [Working with files](#working-with-files)
- [Classes](#Classes)
- [Eval](#eval)
- [Modules](#internal-modules)
- [Jit compiler](#the-pashmak-jit-compiler)
- [Developer Guide](#developer-guide)



## Installation

### GNU/Linux/Unix
This installation guide is for GNU/Linux/UNIX systems. Also compile process needs `pyinstaller` pip library.
If you don't have Pyinstaller, run `pip3 install pyinstaller` command in terminal.

Compile & Install:

```bash
# checkout to latest release
git branch installation $(git describe --abbrev=0)
git checkout installation

# compile and install
make all
make
sudo make install

# back to master branch and delete installation branch
git checkout master
git branch -D installation
```

Run above commands in terminal to install Pashmak interpreter on your GNU/Linux/UNIX system.

Also if you want install latest version(development state), do not run above git commands and just run it:

```bash
make all
make
sudo make install
```

Above commands install latest (development) state of the program.

Now you can run Interpreter in terminal:

```bash
pashmak --info # shows info about pashmak
pashmak -v # --version, shows version of pashmak
pashmak app.pashm
pashmak /path/to/script.pashm # runs file
pashmak - # gets code from stdin and run that
pashmak -r "<you code...>" # run code from cli arguments with `-r` option
pashmak -m # or --modules. shows list of available pashmak modules on the system
```

IF YOU DON'T WANT TO INSTALL IT, you can run this with python3 in terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

#### uninstallation
To uninstall Pashmak, run this make command in terminal:

```bash
sudo make uninstall
```

Or manually remove `/usr/bin/pashmak`.

Pashmak will be remove from your system.

### Windows
In Windows, you can run program with python interpreter without compiling:

```bash
cd \path\to\project
python src\pashmak.py
```

But also you can compile it with `pyinstaller`. If you don't have Pyinstaller, run `pip install pyinstaller` in command line.

Compile:

```bash
# install pyinstaller with pip
pip install pyinstaller

# configure & compile
.\win-configure.bat
python -m PyInstaller src\pashmak.py --onefile
```

now executable file is created in `dist\pashmak.exe`:

```bash
dist\pashmak.exe -v
```



## Basics

A simple printing in Pashmak:

```bash
mem 'something to print\n'; print(^)
```

or

```bash
print('something to print\n')
```

#### how it works?

First, we go through pashmak syntax structure.
The base structure of pashmak syntax is this:

```bash
<command> [arguments]
<command> [arguments]
<command> [arguments]; <command> [arguments]
```

In this example, we have two commands:

```bash
mem 'something to print\n' # first command
print(^) # second command
```

##### NOTE: the `;` in the end of lines is not required. you can write your code without `;` IF you don't want to write two or more command in one line

Here, `mem` is an command and `'something to print\n'` is the argument of that, and
`print` is an command and `^` is the argument of that.

But what is the function of this code?

when you run the script in terminal:

```bash
pashmak myscript.pashm # or any filename you saved code in that
```

##### NOTE: the `.pashm` extension for pashmak scripts is not required. you can run any file with any name as pashmak script

you will get this output:

```
something to print
```

This code, prints `'some thing to print'` on the stdout.
but how?

First, `mem` command brings the string `'some thing to print'` in memory, and next `print` command prints the memory value on screen.

### what is `mem`?
mem is a temp place to make and calculate values.

```bash
mem 'hello world'
print(^) # the ^ is pointer of mem
```

The `^` is pointer of the mem.

You can also write the code like this to have shorter code (we have to use `;` to seprate them):

```bash
mem 'hello world\n'; print(^)
```

###### NOTE: remember to put \n when you want to go to the next line

#### mem is temp

Look at this example:

```bash
mem 'some thing\n'

print(^) # output: some thing

print(^) # output: None
```

Why in the first time when mem value was read, the value correctly was printed on screen, but in the second time, the `None` was printed?

Because memory is a temp place. When you read the memory, that will be empty after read automaticly.

Look at this example:

```bash
mem 'first value\n'
print(^)

mem 'second value\n'
print(^)
```

output of this code:

```
first value
second value
```

###### NOTE: the # character is comment symbol. you can put comment in your code after # character. comments have not any effect in program

### more about mem
You can calculate every thing in the `mem`.

For undrestanding this, look at the following examples:

```bash
mem 'hi there'; print(^) # output: hi there

# you can paste strings
mem 'first string ' + 'last string'; print(^) # output: first string last string

# run math calculations
mem 2*7; print(^) # output: 14

mem 3*(2+1); print(^) # output: 9

mem str(7*7) + ' is sum'; print(^) # output: 49 is sum
# the `str` function gets a value and convert it to string.
# in here you can not paste number to string. first need to convert num to str with str()
```

**The mem structure, is handled by Python(eval function) and you can use all of python features in the mem calculation**

#### Print `;` and `#`
For printing `;` and `#` special characters, put a `\` before them:

```bash
mem 'this is \; semicolon\n'; print(^)
mem 'this is \# sharp\n'; print(^)
```

output:

```
this is ; semicolon
this is # sharp
```

### Printing without using mem
this is a easier syntax for printing:

```bash
mem 'hello world\n'; print(^)

# this is easier
print('hello world\n')

print(str(2*2))

print('hello ' + 'parsa\n')

print('num is ' + str(100+7))
```

you can use all of features of `mem` in the argument of commands like above example.

after this, we never use `mem <something>; print(^)` pattern for printing, and we just use `print` command.

### println

If you want to print something and go next line, you have to put `\n` in the end of string.

But with `println` function, you don't need to use `\n` and that will put automaticaly:

```bash
println('hello world')
```

output:

```
hello world<nextline>
```

Also there is a alias for `println`, this is `printl`:

```bash
#println("hello world")
printl("hello world")
```



## Variables

Variables are like a pot which you can save data in them.

Look at this example:

```bash
$myvar = 'this is data'

println($myvar) # output: this is data
```

##### NOTE: always put $ before name of variable everywhere

Declaring variables is so easy, only you have to write `$<name_of_variable>`.

Also you can set variables without value like this example:

```bash
$var1
$var2; $var3 # default value is null
```

##### NOTE: variable name should not contains `()+-/*%=}{<>[], ` chars(literal chars)

### Using variables in mem calculation

look at this example:

```bash
$name = 'parsa' # set name variable

println('hello ' + $name) # output: hello parsa

$num = 12
println($num * 5) # output: 60

$num2 = 4

println($num * $num2 + 1) # output: 49
```

#### copy variables in other variables

look at this example:

```bash
$var1 = 'hi'
$var2 = 'bye'

println($var1) # output: hi
println($var2) # output: bye

$var2 = $var1

println($var1) # output: hi
println($var2) # output: hi

$name = 'parsa'
$message = 'hello' + $parsa # you can use all of mem calculation features in here
println($message) # output: hello parsa
```

#### NOTE: allowed characters for variable name are `A-Za-z`(or any alpha-bet characters in other languages), `&._` characters.

### Put `mem` value to variable

We can set value of mem to variables with this code:

```bash
mem 'something'
$myvar = ^
```

If you put `^` (mem symbol) as value, memory value will put in the variable.

Also you can use that mem alongside another values.

for example:

```bash
mem 'parsa'
$message = 'my name is ' + ^
println($message) # output: my name is parsa

mem 10
println((^ + 5) * 2) # output: 30
```

### free(delete) variables
When you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
$somevar = 'some value'
println($somevar) # output: some value

free $somevar

println($somevar) # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
```

Also you can make free more than one variables with `free` command:

```bash
free $var1 $var2 $var3 # ...
```

### Checking a variable isset
You can check a variable existens with `isset` command.

look at this example:

```bash
$somevar; $v # set `somevar` and `v` variables

isset $somevar; println(^) # output: True
isset $this_var_not_found; println(^) # output: False
isset $somevar $sassadffgdty; println(^) # output: False
isset $somevar $v; println(^) # output: True
```

(The `True` and `False` are Python booleans).

#### how it works?

The isset command gets one or more variable names and if all of that vars exist, it will put `True` in  memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

You can get the data type of a variable with `typeof` function.

look at this example:

```bash
$mystr = 'hi'
$myint = 20
$myfloat = 15.32
$mybool = False

typeof($mystr); println(^) # output: <class 'str'>
typeof($myint); println(^) # output: <class 'int'>
typeof($myfloat); println(^) # output: <class 'float'>
typeof($mybool); println(^) # output: <class 'bool'>
# also you can use this syntax and use function directly
println(typeof($myint))
```

This command puts the typeof variable in mem.

(All of pashmak datatypes are handled by python and you can use all of python variables features).

### required command

The required command requiring an variable existens.

look at this example:

```bash
$name

required $name
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#$name
required $name
```

now `$name` variable is not exists, and you will get this error:

```
VariableError: undefined variable $name
```

The `required` command checks a variable is exists, if no, raises VariableError.

also you can check more than one variables:

```bash
required $a, $b
# you have to seprate them with `,`
```

### python datatype methods
datatype of the pashmak variables, is handled by python. this means you can use all python methods on them.

for example:

```bash
$mystring = '  hello world          '
println($mystring->strip()) # output: `hello world`
```

#### NOTE: in python, for calling function or access to property of a object, we use `.` character, but in pashmak we use `->` symbol(like php)

## Constants
Constants (consts) are even like variables, but one thing is different in constants, **Constant value cannot be changed**.

for example:

```bash
# declare the const
$&name = 'the value'

println($&name)
```

output:

```
the value
```

To declare consts, you only need to put a `&` in the name of variable(location of that is not important).

```bash
$&const1 = 123
$&const2 = 'fsgdf'
# ...
```

When we try to change value of the const, we will get error:

```bash
$&name = 'the name'

$&name = 'new value'
```

output:

```
ConstError: "$&name" is const and cannot be changed...
```

also you can **declare** a constant, but set value of that later.

for example:

```bash
$&name # only declare constant, default value is `None`

# set value
$&name = 'parsa'

println($&name)
```

output:

```
parsa
```

But in the second time, error will be raised.



## Read Input From User

You can read input from user in stdin.

look at this example:

```bash
print('what is your name? ')
$name = read() # read a input and put that in $name variable
println('hello ' + $name) # say hello to $name :)
```

When we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for input, and when you type something and press enter, program prints `hello <your-input>`.

for example here I entered `parsa` as input and program printed `hello parsa`.

We can get input from user like above example.

also look at this example:

```bash
$num1; $num2

print('enter first number: ')
$num1 = int(read())

print('enter second number: ')
$num2 = int(read())

# now we want to plus them
$sum = $num1 + $num2

println(str($sum))
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them.

### Reading command line arguments
To access command line arguments, you can use `$argv` variable.
this variable is a public variable and is list contains command line arguments.

look at this example:

```bash
println($argv[1])
```

we run above code:

```bash
pashmak mycode.pashm hello
```

output:

```
hello
```

Type of `$argv` is the python `list`.



# Sections
Section is a system to make pointer to a part of code. this is useful to create loop, if and... and is used to handle program flow.

Actually, programs flow maybe changed by conditions and loop...
the section system is used to control program flow.

look at this example:
```bash
section my_loop
    println('hello world')
goto my_loop
```

this code prints `hello world` non-stop.

Actually when my code starts, prints hello world and then `goto` commands directs program step to the `my_loop` section and it will repeat again and again.

###### NOTE: that TAB before `println('hello world')...` line is not required. this is writen only to have beautiful code

look at this example:

```bash
$i = 1

section loop
    println($i) # print($i)
    $i = $i + 1 # add 1 to $i
mem $i < 10; gotoif loop # check the condition in `mem` and use gotoif command
```

the output of this code is:

```
1
2
3
4
5
6
7
8
9
```

we have 3 functions about section system:
- section
- goto
- gotoif

### section
This command gets name of section as parameter like above examples. This is for declaring the sections.

### goto
goto command gets a name as section name and brings program current step to that section.

### gotoif
gotoif checks `mem` and if mem is True, will go to wanted section. if not, does nothing and continue.

look at this example:

```bash
# read age from user
print('enter your age: ')
$age = read()
$age = int($age)
# OR
$age = int(read())

mem $age > 18; gotoif age_is_more_than_18 # if age is more than 18, goto age_is_more_than_18 section

# if not, this line will run and program goes to age_is_less_than_18
goto age_is_less_than_18

section age_is_more_than_18

    println('you are more than 18')
    goto after_if

section age_is_less_than_18

    println('you are less than 18')

section after_if

println('program ends')
```

we run the program:

```bash
enter your age: <input>22
you are more than 18
program ends
```

run again:
```bash
enter your age: <input>14
you are less than 18
program ends
```

The above example is used to create conditions.
That code gets age of user as a integer, and checks conditions on that and does something by that conditions.



# If elif else statement
in the previous part, you learned how to use **sections** for creating **Conditions** and **Loops**.
but there is a easy way to create **Conditions**, that is **If..elif..else** statement. this system is very easy for creating conditions and handling program flow.

example:

```bash
if 2 == 2
    println('yes, 2 is 2')
endif
```

or:

```bash
if 3 == 7
    println('3 is 7')
else
    println('3 is NOT 7')
endif
```

in this part, we learn how to use this system.

The if syntax is this:

```bash
if <condition>
    # code
endif
```

for example:

```bash
$age = 30

if $age > 18
    println('Welcome!')
endif
```

output:

```
Welcome!
```

```bash
$age = 12

if $age > 18
    println('Welcome!')
endif

# above code haven't output
```

also you can use `else`:

```bash
$age = 12

if $age > 18
    println('Welcome!')
else
    println('you cannot access')
endif
```

if condition of `if` is not true, `else` block will be runed.

also there is other keyword `elif`:

```bash
$num = 17

if $num == 5
    println('num is 5')
elif $num == 6
    println('num is 6')
elif $num == 17
    println('num is 17')
else
    println('nothing')
endif
```

output:

```
num is 17
```

actually, `elif` block will be checked one by one. `elif` means `else if`.

### If in If
you can write ifs in ifs.

look at this example:

```bash
$num = 15
$test = True

if $num == 18
    pass
elif $num == 15
    println('num is 15')

    # another if in the parent if
    if $test
        println('this is a test')
    else
        println('this is not test')
    endif
endif
```

output:

```
num is 15
this is a test
```



# Functions
Function is a system to make alias for some codes (function).

look at this example:
```bash
func say_hello
    println('hello world')
endfunc

say_hello()
```

output:

```
hello world
```

```bash
func say_hello
    println('hello world')
endfunc

# we run this two times
say_hello()
say_hello()
```

output:

```
hello world
hello world
```


You can declare a function and call it from everywhere. when you call a function, all of codes inside that function will be runed.

for declare a function you have to write `func <name-of-function>` and write codes. then for close function write `endfunc` after codes.

look at this smarter function:
```bash
mem 'program started\n'; print(^)

func say_hello
    $name = ^ # copy mem to $name
    println('hello ' + $name)
endfunc

mem 'parsa'; say_hello()
```

program output:

```
program started
hello parsa
```

##### NOTE: function name should not contains `()+-/*%=}{<>[],. ` chars(literal chars)

### passing argument to Functions
for pass argument to the Functions, you can put value after name of function:

```bash
func myfunc
    print(^)
endfunc

myfunc("hello")
```

output:

```
hello
```

This is exactly like

```
mem 'something'; some_func()
```

but with better syntax, you only need to run `some_func('something')`.

##### how it works?
you can put a value after name of function. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
func say_hello
    $name = ^ # copy mem(the passed argument to function) to $name
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

output:

```
hello parsa
```

also you can pass more than 1 argument to functions:

```bash
func say_hello
    $args = ^ # copy mem to $args
    $first_name = $args[0]
    $last_name = $args[1]
    println('hello ' + $first_name + ' ' + $last_name)
endfunc

say_hello('parsa', 'shahmaleki')
```

arguments should be split with `,` and this will make a array in mem and function can access that array and use arguments.

we to copy function argument (in mem) to a variable, using this syntax:

```bash
func say_hello
    $name = ^
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

but also we can use this syntax to copy function argument to variable with better syntax:

```bash
func say_hello ($name)
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

#### NOTE: that space between `hello` and `($name)` is not required.

we can put `($varname)` after name of function (with a space between them) and mem will copy automatic in that variable.
also you can don't use `()` and you can write above code like this:

```bash
func say_hello $name # without ()
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

also you can use empty `()` to have better syntax:

```bash
func say_hello()
    println('hello ' + ^)
endfunc

say_hello('parsa')
```

also we can use mem symbol in argument of function.

for example:

```bash
func say_hello $name # without ()
    println('hello ' + $name)
endfunc

mem 'parsa'

say_hello(^)
```

or:

```bash
func say_hello $name # without ()
    println('hello ' + $name)
endfunc

mem 'parsa'

say_hello(^ + ' shahmaleki')
```

#### how two handle multiple arguments?
in the above examples, all of created functions only have ONE argument. some times our functions recives more than one arguments. how we can handle this?

to handle this, you can use something like this:

```bash
func say_hi($args)
    $first_name = $args[0]
    $last_name = $args[1]
    println('hello ' + $first_name + ' ' + $last_name)
endfunc

say_hi('parsa', 'shahmaleki')
```

in above example, all of our arguments are in `$args`. that variable is a python tuple/list. we can handle multiple arguments like this example.

### local variables & global variables

look at this example:

```bash
func myfunc
    $name = 'new name'
    println($name)
endfunc

$name = 'parsa'
println($name)

myfunc()

println($name)
```

output:

```
parsa
new name
parsa
```

there is a note. why when we changed `$name` variable in `myfunc` function, this was the old value after function?

the `$name` where was set in `myfunc`, is local. means that do not points to global `$name` in out program.

the seted variables in Functions, are local. also Functions cannot change global variables

the variable environment in Functions are isolated.

so, how to change a global variable from a function?

the answer is in `gset`:

```bash
func myfunc
    $name = 'new name'
    gset('name', $name)
    println($name)
endfunc

$name = 'parsa'
println($name)

myfunc()

println($name)
```

output:

```
parsa
new name
new name
```

here, `gset` function gets two parameters: first, global variable name and second, new value for that

this command sets value of that variable globaly.

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)

### handle functions output

when you calling a function, that function may return a output. this value as output should be save in mem

look at this example:

```bash
func add_two_nums($nums)
    $sum = $nums[0] + $nums[1] # add two numbers
    mem $sum # put result to mem
endfunc

# now we call this function
add_two_nums(10, 5)
$result = ^ # function output is in mem and we copy mem to variable $result
println($result)
```

output:

```
15
```

also you can use `return` command instead of above method.

for example:

```bash
func get_data
    println('start')
    return 'the data'
    println('end') # this will not be runed
endfunc

println(get_data())
```

output:

```
start
the data
```

actually, in `return` command, value will be put in the mem as output and function will be finished(commands after return will not be runed).

### inline calling functions
you can call a function as argument of another function.

look at this example:

```bash
# the say_hi function returns string `hello <$name>`
func say_hi($name)
    return 'hello ' + $name
endfunc

# we want to call this function and print the output of that
println(say_hi("parsa"))
```

output:

```
hello parsa
```

in the above example, we directly called a function and passed the output of that as argument of `println` function.

another example:

```bash
func say_hi($name)
    return 'hello ' + $name
endfunc

func get_name
    return 'pashmak'
endfunc

println(say_hi(get_name()))
```

output:

```
hello pashmak
```

another example:

```bash
func add_two_nums($nums)
    return $nums[0] + $nums[1]
endfunc

$result = add_two_nums(10, 5)
println('sum is ' + str($result))
```

This is very useful.

### Puting functions into variables
Functions are like variables, you can put them into variables and use them.

look at this example:

```bash
func hello($name)
    println('hello ' + $name)
endfunc

hello('parsa')

# puting the function into the variable
$myfunc = hello

# calling the variable
$myfunc('pashmak')
```

output:

```
hello parsa
hello pashmak
```

another example:

```bash
func somefunc()
    println('hello. I was runed')
endfunc

$myfunc = somefunc
$myfunc()
```


also look at this example:

```bash
func run_the_func($func)
    println('start')
    $func()
    println('finish')
endfunc

func hi
    println('hello world')
endfunc

run_the_func(hi)
```



# Arrays
arrays are a list from variables.

look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack']

println($names) # output: ['parsa', 'pashmak', 'jack']
println($names[0]) # output: parsa
println($names[1]) # output: pashmak
println($names[2]) # output: jack
```

this is a example about array and loop:

```bash
$names = ['parsa', 'pashmak', 'jack']

$i = 0

section loop
    println($names[$i])
    $i = $i + 1
mem $i < len($names); gotoif loop
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### adding new item to array
you can add new item to an array by using python `append` and `insert` methods:

```bash
$myarray = ['first', 'second']
println($myarray)

$myarray->append('new item')
println($myarray)
```

output:

```
['first', 'second']
['first', 'second', 'new item']
```

also with `insert` method you can set the location of new item:

```bash
$myarray = ['one', 'two', 'four']
println($myarray)

$myarray->insert(3, 'three')
println($myarray)
```

output:

```
['one', 'two', 'four']
['one', 'two', 'three', 'four']
```

### removing an item from array
you can delete an item from array by using python `pop` method:

```bash
$myarray = ['first', 'second']
println($myarray)

$myarray->pop(1)
println($myarray)
```

output:

```
['first', 'second']
['first']
```

also `pop` method without argument removes last item by default.

### setting value of an item in array
look at this example:

```bash
$abc = ['a', 'b', 'c']
println($abc) # output: ['a', 'b', 'c']

$abc[0] = '000'
println($abc) # output: ['000', 'b', 'c']
```

like above example, we can set a specify item of array with a syntax like this: `$my_list[<index>] = <value>`.

also you can do this on a subitem. look at this example:

```bash
$my_list = []
$my_list->append(['a'])

println($my_list[0]) # output: ['a']

$my_list[0][0] = 'AAA'

println($my_list[0]) # output: ['AAA']
```

### Dictonaries
dictonaries are like lists, but in dicts you can set a string as key instead of index number.

look at this example:

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict) # output: {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict['hello']) # output: Hello world
```

like above example, we can use string as key instead of index number. in the above example, `hello` is the key.

also you can set the keys like lists(arrays):

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}
println($my_dict['hello']) # output: Hello world

$my_dict['hello'] = 'new hello'

println($my_dict['hello']) # output: new hello
```

The **list(Array)** and **dict** are python datatypes(means you can use all of python list and dict methods on them).



# Try and Endtry statement

we may recive some errors in our program. for example:

```bash
println($this_var_not_found)
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined function
printlgdfgfd(^)
```

output:

```
SyntaxError:
        undefined function "printlgdfgfd"
```

they are errors.

##### but how to handle errors?

we can handle errors with `try-endtry` statement.

look at this example:

```bash
try handle_error
    println($somevar)
endtry

goto after_error

section handle_error

println('some errors raised')

section after_error
```

when you write code between `try <section-name> ... endtry`, errors will not raised in them and if an error is raised, that section where passed to try command will run.
actually, we say to the Pashmak to don't show error to user and do that thing I'm saying you instead of default error showing.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error
    println($somevar)
endtry

goto after_error

section handle_error

$ex = ^ # copy mem (^) to $ex variable (this includes information about raised error)
println($ex) # output: {"type": "VariableError", "message": "undefined variable $somevar"}...

section after_error
```

#### raising errors
Your self can raise errors in the program.

for example:

```bash
println('program started')

raise('MyError', 'this is my error')

println('this will not print')
```

output:

```
progrma started
MyError: this is my error
```

The `raise` function can raise errors in program.

first argument `'TheError'` is error type and second error `'this is my error'` is error message.



# OS Commands

here is some commands about OS.

### chdir
change directory. with this command you can change program working directory:

```bash
chdir('/tmp')
```

### cwd
get current working directory.

```bash
cwd()
println(^)
```

output:

```
/tmp
```

or:

```bash
$cwd = cwd()
println('The current working directory is ' + $cwd)
```

or:

```bash
println(cwd())
```

this command puts current working directory path into the mem.

### system
you can run shell commands by this command:

```bash
system('ls /tmp')
```

also after run `system` function, exit code will put in `mem`:

```bash
system('ls /')
println(^) # output: 0
```

or:

```bash
println(system('ls /'))
```

### exit
this command exits program

look at this example:

```bash
println('first print')

exit()

println('last print') # this will not print
```

output:

```
first print
```

###### exit with exit code:

```bash
println('hello world')
exit(1)
```

exit code of program will be `1`

### `$__file__` and `$__dir__` variables
`$__file__` and `$__dir__` variables are two variables contains self script filepath and dirpath.

for example, if you run an script in `/home/parsa/myscript.pashm` with this content:

```bash
println($__file__)
println($__dir__)
```

output is:

```
/home/parsa/myscript.pashm
/home/parsa
```

The `$__file__` variable contains filepath of current running script.

The `$__dir__` variable contains dirpath of current running script.



# Importing scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a function to show fibonaccy algo.

###### fib.pashm:
```bash
# this function prints fibonacci pattern
func fib
    $a = 1
    $b = 1

    section loop;
        println($a)

        $tmp_a = $a
        $tmp_b = $b

        $a = $tmp_b

        $b = $tmp_a + $tmp_b
    mem $a < 10000; gotoif loop
endfunc
```

###### app.pashm:
```bash
import 'fib.pashm'

fib()
```

when we run `import` function and pass a file path to that, content of that file will be included in our code and will be runed. for example, here we used a function from the `fib.pashm` file.

also you can import more than 1 scripts in one command:

```bash
# seprate them with `,` (actially a tuple or list)
import('a.pashm', '/path/to/b.pashm', 'dir/c.pashm')
```

### import_once function
there is a command named `import_once`. this is excatly like `import` function, but this function do not repeats for import one script.

for example, we have a file named `foo.pashm`:

##### foo.pashm:

```bash
func hello
    println('hello')
endfunc
```

now, we import this file Two times:

```bash
import('foo.pashm')
import('foo.pashm')
```

we will get this error:

```
FunctionError: function "hello" already declared...
```

because i imported this script two times and my code tryied to declare function `hello` two times, so, we get the error.

but if i use the `import_once` function:

```bash
import_once('foo.pashm')
import_once('foo.pashm')
```

the above code will be runed successfully.

because, `import_once` function checks the file, and if files already imported, don't imports again.

### `$__ismain__` variable
the `$__ismain__` variable, is a general Boolean variable. this variable is used to check the current file, is the **Main runed file** or not.

for example, we have two files, `my_program.pashm` and `lib.pashm`. we want to know that in our scripts **Is the current script main directly runed file?**.

when you run in terminal:

```bash
pashmak my_program.pashm
```

the `my_program.pashm` file is runed directly.

##### my_program.pashm:

```bash
println($__ismain__)

import('lib.pashm')
```

the above code, prints value of this variable and also imports `lib.pashm` file.

##### lib.pashm:

```bash
println($__ismain__)
```

when i run `my_program.pashm`, output is this:

```
True
False
```

actually, value of this variable in `my_program.pashm` is `True`, but in `lib.pashm` is `False`.

now, when i run `pashmak lib.pashm`, output is `True`.

**The `$__ismain__` variable says that the current file is main runed file or not and you can check this**.

for example, if we want to run a code only if our script is directly runed and is not imported from other script:

```bash
if $__ismain__
    # do something
endif
```



# Namespaces

name space is a very useful system to split sections of program.

look at this example:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endnamespace

App.say_hello
```

output:

```
hello world
hello world
```

actualy, everything which is declared between `namespace <something>` and `endnamespace` will be under this.

in above example, we declared a namespace named `App`. and we declared `say_hello` function in that.

next, we called `say_hello` inside the namespace, and one time we called `say_hello` outside the namespace.

when we are calling a member of namespace from outside of that namespace, we have to put name of namespace with a `.` before name of that function

for example here, our namespace name is `App` and out function name is `say_hello`. we can write only `say_hello` inside the namespace but for call it from outside of namespace, we have to write `App.say_hello`.

also look at this example:

```bash
namespace First
    func dosomething
        println('i am from First')
    endfunc
endnamespace

namespace Last
    func dosomething
        println('i am from Last')
    endfunc
endnamespace

First.dosomething()
Last.dosomething()
```

output:

```
i am from First
i am from Last
```

also you can use `endns` keyword insted of `endnamespace`:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endns

App.say_hello()
```

also namespace system is sync with variables:

```bash
namespace App
    $name = 'parsa'
    println($name) # output: parsa
    println($App.name) # output: parsa
endns

println($App.name) # output: parsa

# but this has error:
println($name) # VariableError: undefined variable $name, because it is in App namespace and is accessible with `$App.name`
```

##### NOTE: variable name should not contains `()+-/*%=}{<>[],. ` chars(literal chars)

this system is very useful.

### use command
the `use` command is a command to use content of a namespace.

look at this example:

```bash
namespace App
    func dosomething
        println('hello world')
    endfunc

    $name = 'parsa'
endns

App.dosomething()
println($App.name)
```

output:

```
hello world
parsa
```

we have to put `App.` before `dosomething` to run this function.
but i want to don't use namespace prefix and just type name of function to call this. what i have to do?

look at this example:

```bash
namespace App
    func dosomething
        println('hello world')
    endfunc

    $name = 'parsa\n'
endns

use App

App.dosomething()
dosomething()

println($App.name)
println($name)
```

output:

```
hello world
hello world
parsa
parsa
```

when i use `use` command and give a namespace as argument to that, i can call all of that namespace members without namespace prefix.

for example if there is a namespace named `App` and have a function named `dosomething`, for call that function i have to write `App.dosomething`. but if i run `use App`, after that i can call this function just by typing `dosomething;`

### namespace in namespace (subnamespace)
you can declare a namespace in a namespace

look at this example:

```bash
namespace App
    func hello
        println('hello world')
    endfunc

    # declare namespace `Core` under `App`
    namespace Core
        func run
            println('the core')
        endfunc
    endns
endns

# now we use it
App.hello()

App.Core.run()
```

output:

```
hello world
the core
```

### importing inside namespaces
you can import an script inside an namespace.

for example, we have `foo.pashm` and `bar.pashm` scripts.

##### `foo.pashm`:

```bash
namespace foo
    func hello
        println('hello world')
    endfunc
endns

func bye
    println('good bye')
endfunc
```

##### `bar.pashm`:

```bash
import('foo.pashm')

namespace App
    import('foo.pashm')
endns

foo.hello() # output: hello world
bye() # output: good bye

App.foo.hello() # output: hello world
App.bye() # output: good bye
```

in above example, we imported `foo.pashm` inside an namespace and content of `foo.pashm` is loaded under that namespace. for example, `foo.hello` function is loaded under `App` namespace, so finally will be set as `App.foo.hello`.



# Working with files
working with files in pashmak is so easy.

we have 4 main operations on files: Open, Read, Write, Close

look at this example for reading content of a file:

```bash
$my_file = open('/path/to/some/file.txt', 'r')
println($my_file->read())
$my_file->close()
```

In above example, we opened our file, read content and then we closed that.

the `$file->read()`, the `read` method reads content of file and returns that.

you can put that in a variable:

```bash
$content = $file->read()
```

to write content of a file, we can use `write` method:

```bash
$my_file = open('/path/to/some/file.txt', 'w')
$my_file->write('new content')
$my_file->close()
```

The second argument for opening file is type of opening. `r` means Read and `w` means write.

Also you can use `fopen` function instead of `open`. this is not different, just is an alias.

The file objects in pashmak are handled by python you can use all of python file features in pashmak like python.



# Classes
class is a system to declare a structure of data. actually, class is a model with some fields.

for example, we want to declare a model from **Car**. we can declare a class:

```bash
class Car
    $name
    $color
endclass
```

in above example, we declared a class named `Car` with `name` and `color` properties.

let's use this:

```bash
class Car
    $name
    $color
endclass

$my_car = %{new Car()}%

println($my_car)
```

output:

```
[PashmakClass name="Car"]
```

now, we want to set the properties:

```bash
class Car
    $name
    $color
endclass

$my_car = %{new Car}%
$my_car->name = 'BMW'
$my_car->color = 'white'

println($my_car->name + ' ' + $my_car->color)
```

output:

```
BMW white
```

so, let's review the classes. for declaring the classes, we have to use `class` and `endclass` commands:

```bash
class TheClassName
    # declare the properties
endclass
```

between them, you have to declare properties like normal variables:

```bash
class TheClassName
    # declare the properties
    $prop1
    $prop2
    $prop3; $prop4
endclass
```

default value for that properties is `None`.

also you can set the default value:

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass
```

now, we declared our class, how to create a instance from that? actually, we can create infinitivly object from that. for example we have a thing named `Car`, this is a class and we have much many objects with `Car` class.

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass

$my_object = %{new TheClassName}%
```

the `new` command gets name of class and creates an instance from that and puts that in the mem temp value.
means, if i want to put created object in a variables, i need to write `$var = %{new ClassName}%`.

now, we can create object from a class. how to access to the properties? look at this example:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = %{new Car}%

println($my_car->name) # output: default name
```

we can access to the object properties by writing `$varname->property_name`

the `->` symbol is important.

also you can set the value with this syntax:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = %{new Car}%

println($my_car->name) # output: default name

# setting the new value
$my_car->name = 'new name'
println($my_car->name) # output: new name
```

##### NOTE: class name should not contains `()+-/*%=}{<>[],. ` chars(literal chars)

### classes in namespaces
you can declare classes inside the namespaces like variables and functions.

for example:

```bash
namespace Models
    class Car
        $name
        $color
    endclass
endns

$my_car = %{new Models.Car}%
```

all of laws for **classes in namespaces** is like `functions` and `variables`.

### Advance property usage
you can use more features of the properties. actually, you can create any structure in your properties.

look at this example:

```bash
class Brand
    $title = 'the brand name'
endclass

class Car
    $name
    $color

    # the brand property is a object from Brand class
    $brand = %{new Brand}%
endclass

$my_car = %{new Car}%
$my_car->name = 'my car'
$my_car->brand->title = 'BMW'

println($my_car->name)
println($my_car->brand->title)
```

output:

```
my car
BMW
```

actually, your property value can be a object from other property and this process can be continued recursivly.

you can access to properties by `->` symbol:

```bash
# access to `prop3` of `prop2` of `prop1` of $obj
$obj->prop1->prop2->prop3
```

also you can set new properties on a object:


```bash
class Car
    $name
    $color
endclass

$my_car = %{new Car}%
$my_car->name = 'my car'
$my_car->color = 'red'

$my_car->the_new_prop = 'the value'

println($my_car->the_new_prop)
```

output:

```
the value
```

in the above example, property `the_new_prop` is not declared in class by default, but you can add props without any problem in objects.

also you can use **Consts** in classes.

for example:

```bash
class Person
    $name = 'parsa'
    $_age = 100 # age is const
endclass

$p = %{new Person}%

$p->_age = 50
```

output:

```
ClassConstError:...
```

if you want to set a peoperty as constant, you have to put a `_` in the start of that name.

### inheritance
the inheritance in classes means classes can be child of another classes. this means the child class has all of he's/she's parent properties.

look at this example:

```bash
class Thing
    $name
endclass

class Animal < Thing
    $title
    $size
    $color
    $gender
endclass

class Cat<Animal
    $mioo
endclass

class Human<Animal
    $height
endclass
```

in the above example, we used `<` symbol to make a class child of another class:

```bash
class Parent

endclass

# the `Child < Parent` sets this class as child of the `Parent`
class Child < Parent

endclass
```

the child class, has all of properties of the parent.

for example:

```bash
class Father
    $name = 'hello world'
endclass

class Child < Father
    $age = 100
endclass

$child = %{new Child}%

println($child->name) # output: hello world
println($child->age) # output: 100
```

actually, the parent class has not properties of he's childs, but childs has all of parent's props.

#### All of classes extends `Object` class
all of classes by default extedns from a class named `Object`. this class is a internal pashmak class.
all of classes are child of this class.

### Classes general attributes
classes has some general properties:

- `__name__`: name of the class
- `__parent__`: name of parent of class

for example:

```bash
class Person

endclass

$person = %{new Person}%

println($person->__name__) # output: Person
```

### Class methods
you can declare function inside classes. the class's function is named **Method**.

look at this example:

```bash
class Cat
    $name

    func mio
        println('miooo...')
    endfunc
endclass

# create a object from Cat
$my_cat = %{new Cat}%

$my_cat->mio()
```

output:

```
miooo...
```

actually, you can call functions of a class.

another example:

```bash
class Cat
    $name

    func mio
        println('miooo... my name is ' + $this->name)
    endfunc
endclass

# create a object from Cat
$my_cat = %{new Cat}%
$my_cat->name = 'gerdoo'
$my_cat->mio()
```

output:

```
miooo... my name is gerdoo
```

in above example, we used a variable named `$this`. this variable is a pointer to self of object.

another example:

```bash
class Person
    $name

    func set_name($name)
        $this->name = $name
    endfunc

    func say_hi
        println('hello. my name is ' + $this->name)
    endfunc
endclass

$p = %{new Person}%

$p->set_name('parsa')

$p->say_hi()
```

output:

```
hello. my name is parsa
```

**You can set object self properties by using $this variable like above examples**

total syntax:

```bash
$object->method_name('arguments...', 'arg2...')
```

also all of classes extends parent methods.

for example:

```bash
class Father
    func hi
        # returnns this string
        return 'hello world'
    endfunc
endclass

class Child < Father; endclass

$obj = %{new Child}%

println($obj->hi())
```

output:

```
hello world
```

### Class magic methods
now, you know what is the class methods. some methods in classes are special.

#### `__init__`
the `__init__` method, will be runed when an object is created from a class.

look at this example:

```bash
class Person
    func __init__
        println('a new Person is created')
    endfunc
endclass

$p = %{new Person}%
```

output:

```
a new Person is created
```

also you can pass argument to `__init__` method. look at this example:

```bash
class Person
    func __init__($name)
        $this->name = $name
        println('hello ' + $this->name)
    endfunc
endclass

$p = %{new Person('parsa')}%
println($p->name)
```

output:

```
hello parsa
parsa
```

#### `__str__`
the `__str__` method, is a method to customize object string value.

look at this example:

```bash
class Person
    $name
endclass

$p = %{new Person}%
$p->name = 'parsa'
println($p)
# OR
println(%{new Person}%)
```

output:

```
[PashmakClass name="Person"]
```

in the above example, when we print a object, default string value is the above output.

but we can customize this string with `__str__` method.

look at this example:

```bash
class Person
    $name

    func __str__
        return 'hello. my name is ' + $this->name
    endfunc
endclass

$p = %{new Person}%
$p->name = 'parsa'
println($p)
```

output:

```
hello. my name is parsa
```

in the above example, we declared `__str__` method for the class. then, when class is printed, output of `__str__` method will be used instead of that default string (output of method should be put in `mem`).



# Eval

you can run pashmak code from string.

look at this example:

```bash
eval('println("hello world from string")')
```

output:

```
hello world from string
```

this code is runed from a string.

look at this example:

```bash
print('enter some code: ')
$code = read()

eval($code)
```

output:

```
enter some code: <input>mem 'hi\n'; print(^);
hi
```

the above code gets a string from user and runs that as pashmak code.

## run python code
you can run python code like `eval` with `python` command:

```bash
$code = 'print("hello world from python")'
python($code)
```

output:

```
hello world from python
```

### `py_load_file`
The `py_load_file` is a function to load python scripts as object in pashmak.

for example, we have `myscript.py`:

```python
def somefunc():
	print("hello world")

the_var = 'the value'

```

and our pashmak script:

```bash
$pyobj = py_load_file('/path/to/myscript.py')

println($pyobj->the_var)
$pyobj->somefunc()
```

output:

```
the value
hello world
```

also if your python script imports another python module, you should add path of that module to `PYTHONPATH` env var. for example:

```bash
PYTHONPATH=/path/to/pypath pashmak myapp.pashm
```




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
println(hash.sha256("hello"))
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

println(time.time()) # output is some thing like this: `1600416438.687201`
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
println(random.randint(1, 10))
```

##### random.random
```bash
import @random

# generates a random float less that 1
$rand = random.random()
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
- `sys`
- `time`
- `hashlib`
- `random`
- `datetime`
- `json`

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

$module_paths = sys.path.list()

println($module_paths)
```

output:

```
['/path1', '/path2', '...']
```

### Another useful libraries written by others

- The [polor-pashm](https://github.com/sami2020pro/polor-pashm) library by [sami2020pro](https://github.com/sami2020pro)



# The Pashmak Jit Compiler
The **Jit** or **Just in time** compiler, is a system to cache the code and compress that to speed up the interpreter.

this system, compresses the content of scripts and saves them to `__pashmam__` directory. then, when file is runed again, jit system loads compressed content from that cache.

you can see `__pashmam__` directory alongside your scripts. this directory contains cached codes.

Also, make sure to add `__pashmam__` file to your **gitignore**.



# Developer Guide
In This guide, we'll browse about source code of pashmak interpreter. if you want to know logic of this code or contribute to the pashmak project, this is helpful.

## Interpreter Flow
The `src/pashmak.py` file is the main cli entry point of pashmak, program starts from here. this script gets the file path and runs that. this script gives filepath to `src/core/jit.py`. The **Jit** compiler loads content of the file and returns that. the content, is parsed by `src/core/parser.py`'s **parser.parse(code, filename)** function.

The returned data by Parser, is a list from dictonaries (`list[dict]`). the output is list of commands which parsed one by one, comments are deleted.

The output of parser is like this:

```json
{
    "command": "<name-of-command>",
    "str": "<full-command-as-string>",
    "args": ["list", "of", "command", "arguments"],
    "args_str": "<arguments-as-string>",
    "file_path": "/path/to/script/file/this/code/is/in/that",
    "line_number": 12344
}
```

for example, look at this code:

```
println('hello world')
```

output of parser is this:

```json
{
    "command": "println",
    "str": "println('hello world')",
    "args": ["('hello", "world')"],
    "args_str": "('hello world')",
    "file_path": "/path/to/script/file/this/code/is/in/that",
    "line_number": 1
}
```

After parsing process, parsed commands will be runed by `src/core/program.py`(`class Program`) object.

for example:

```python
from core import parser, program
commands = parser.parse('<the-code>') # parse the code
prog = program.Program() # create the program object
prog.set_commands(commands) # set the parsed commands on program object
prog.start() # run the program. this method starts running commands one by one
```

### Builtin functions
Normally, lot of pashmak Functions like `print`, `import`, etc. are declared as **Pashmak function**. but some commands are **internal and builtin**. They are declared in `src/core/builtin_functions.py`. for example, `class` command which is used to declare classes, is the `run_class` method. this methods get the parsed command as dictonary and program object.

For example, `goto` command code is this:

```python
self.require_one_argument(op, 'goto function requires section name argument') # require one argument should be passed to command
arg = op['args'][0] # get the first argument as name of section
try:
    # check section exists
    section_index = self.sections[arg]
except KeyError:
    # section is not exists, raise the error
    return self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)
# section exists, change the program current step to the section
self.threads[-1]['current_step'] = section_index-1
```

The above code is a example.

### Internal modules
Pashmak has some internal modules, like `@hash`, `@time`, etc.

They are declared in `src/modules`.

for example, `src/modules/hash.pashm` is accessible with `@hash`.




##### NOTE: this file is auto generated from `doc` folder. do not change it directly. If you want to edit documentation, edit `doc/` folder files. your changes will built from that folder into this file.
