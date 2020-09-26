# Pashmak programming language
hi there. this is pashmak programming language. pashmak is an interpreter wrote in python.
the pashmak scripts has cool and fucking syntax.

### hello world!
this is a simple hello world script in pashmak:

```bash
mem 'hello world\n'; out ^;
```

## Installation
this installation guide is for GNU/Linux/UNIX systems. if you are windows user, you can run program with python. also compile process needs `pyinstaller`.

compile & install:

```bash
make all
make
sudo make install
```

run above commands in terminal to install pashmak interpreter on your GNU/Linux/UNIX system.

now you can run interpreter in terminal:

```bash
pashmak --info # shows info about pashmak
pashmak -v # --version , shows version of pashmak
pashmak app.pashm
pashmak /path/to/script.pashm # runs file
pashmak - # gets code from stdin and run that
```

IF YOU DON'T WANT TO INSTALL IT, you can run this with python3 in terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

windows users can use this way.

## Authors
pashmak is writed by [parsampsh](https://gitlab.com/parsampsh) and [contributors](https://gitlab.com/parsampsh/pashmak/-/graphs/master)

## Contributing
if you want to contribute to this project, read [Contributing Guide](CONTRIBUTING.md)

# Documentation
read the following Documentation to learn pashmak.

#### NOTE: the pashmak syntax is hard, surely read [STDLIB](#stdlib) document to learn very better and easier syntax



## Basics

a simple printing in pashmak on screen:

```bash
mem 'some thing to print\n'; out ^;
```

#### how it works?

first, we browse about pashmak syntax structure.
the base structure of pashmak syntax is this:

```bash
<operation> [arguments];
<operation> [arguments];
<operation> [arguments]; <operation> [arguments];
```

in this example, we have two operations:

```bash
mem 'some thing to print\n'; # first operation
out ^; # second operation
```

here, mem is a operation and `'something to print\n'` is argument of that, and
out is a operation and `^` is argument of that.

but what is the function of this code?

when you run the script in terminal:

```bash
pashmak myscript.pashm # or any filename you saved code in that
```

you will get this output:

```
something to print
```

this code, prints `'some thing to print'` on the stdout.
but how?

first, `mem` command brings the string `'some thing to print'` in memory, and next `out` command prints the memory value on screen.

### what is `mem`?
you cannot print any thing like this:

```bash
out 'hello world\n';
```

because commands in pashmak never gets a value directly.
if you want to pass a value to the commands, you need to use `mem` command to load that value.
in this example, first, `mem` command loads the `'some thing to print'`, and next, we pass value of mem to the `out` command:

```bash
mem 'hello world';
out ^; # the ^ is pointer of mem
```

the ^ is pointer of mem

you can also write the code like this to have shorter code:

```bash
mem 'hello world\n'; out ^;
```

###### NOTE: remember to put \n when you want to go to the next line

#### mem is temp

look at this example:

```bash
mem 'some thing\n';

out ^; # output: some thing

out ^; # output: None
```

why in the first time when mem value was read, the value correctly was printed on screen, but in the second time, the `None` was printed?

because memory is temporary. when you read the memory, that will be empty after read automaticly.

look at this example:

```bash
mem 'first value\n';
out ^;

mem 'second value\n';
out ^;
```

output of this code:

```
first value
second value
```

###### NOTE: the # character is comment operation. you can put comment in your code after # character


### more about mem
you can calculate every thing in mem

for undrestanding, look at the following examples:

```bash
mem 'hi there'; out ^; # output: hi there

# you can paste strings
mem 'first string ' + 'last string'; # output: first string last string

# run math operations
mem 2*7; out ^; # output: 14

mem 3*(2+1); out ^; # output: 9

mem str(7*7) + ' is sum'; out ^; # output: 49 is sum
# the `str` function gets a value and convert it to string.
# in here you can not paste number to string. first need to convert num to str with str()
```

the `mem` command is absolutely important and you need to use it everywhere

#### print `;`
for printing `;` character, put a `\` before semicolon:

```bash
mem 'this is \; semicolon\n'; out ^;
```

output:

```
this is ; semicolon
```



## Variables

variables are like a pot where you can save data in it

we work with three commands: `set`, `copy`, `free`, to set and handle variables in pashmak

```bash
set $myvar; # set a variables named $myvar
mem 'this is data'; # bring string 'this is data' to mem
copy ^ $myvar; # copy mem (^) to $myvar

out $myvar; # output: this is data
```

###### NOTE: always put $ before name of variable everywhere

also you can set more than one variable with `set` command:

```bash
set $var1 $var2 $var3;
```

### use variables in mem

look at this example:

```bash
set $name; # set name variable
mem 'parsa'; copy ^ $name; # copy 'parsa' string to name variable

mem 'hello ' + $name + '\n'; out ^; # output: hello parsa

set $num; mem 12; copy ^ $num;
mem $num*5; out ^; # output: 60

set $num2; mem 4; copy ^ $num2;

mem $num * $num2 + 1; out ^; # output: 49
```

#### how it works?
we declare $name variable and put `'parsa'` string in that

next, in mem we maked a string and paste $name variable value to `'hello '` with a \n at the end of it, and we print that mem

you can use variables in mem like example above


### free variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
set $somevar;
mem 'some value'; copy $somevar;

out $somevar; # output: some value

free $somevar;

out $somevar; # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
```

also you can make free more than one variable with `free` command:

```bash
free $var1 $var2 $var3; # ...
```

###### NOTE: in above example, we used `copy` command like this:

```bash
mem 'some value';
copy $somevar;
# that is alias of
copy ^ $somevar;
```

if you give just one variable to copy command, the mem will be copy in that variable

look at this example:

```bash
set $var1 $var2;

mem 'hi'; copy $var1;
mem 'bye'; copy $var2; # this is alias of `copy ^ $var2`

out $var1; # output: hi
out $var2; # output: bye

copy $var1 $var2; # copy a variable in variable

out $var1; # output: hi
out $var2; # output: hi

```

### checking a variable isset
you can check a variable existens with `isset` command

look at this example:

```bash
set $somevar $v;

isset $somevar; out ^; # output: True
isset $this_var_not_found; out ^; # output: False
isset $somevar $sassadffgdty; out ^; # output: False
isset $somevar $v; out ^; # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exist, it will put `True` in  memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` command

look at this example:

```bash
set $mystr $myint $myfloat $mybool;

mem 'hi'; copy $mystr;
mem 20; copy $myint;
mem 15.32; copy $myfloat;
mem False; copy $mybool;

typeof $mystr; out ^;   # output: str
typeof $myint; out ^;   # output: int
typeof $myfloat; out ^; # output: float
typeof $mybool; out ^;  # output: bool
```

this command puts the typeof variable in mem


### required command

the required command requiring an variable existens.

look at this example:

```bash
set $name;

required $name;
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#set $name;
required $name;
```

now $name variable is not set, and you will get this error:

```
VariableError:
    undefined variable $name
```

the `required` command checks a variable is exists, if no, raising RequireError

you will know why this command is usable in the aliases section



## Read Input From User

you can read input from user in stdin

look at this example:

```bash
set $name; # set the name variable
mem 'what is your name? '; out ^; # print
read $name; # read a input and copy that in $name variable
mem 'hello ' + $name + '\n'; out ^; # say hello to $name :)
```

when we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for input, and when you type something and press enter, program prints `hello <your-input>`

for example here I entered `parsa` as input and program printed `hello parsa`

we can get input from user like above example


also look at this example:

```bash
set $num1 $num2;

mem 'enter first number: '; out ^;
read $num1;

mem 'enter second number: '; out ^;
read $num2;

# now, $num1 and $num2 are string. we convert string to int:
mem int($num1); copy $num1;
mem int($num2); copy $num2;

# now we want to plus them
set $sum;
mem $num1 + $num2; copy $sum;

mem str($sum) + '\n'; out ^;
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them



# Sections
section is a system to make pointer to a part of code. this is useful to create loop, if and...

look at this example:
```bash
section my_loop;
    mem 'hello world\n'; out ^;
goto my_loop;
```

this code prints `hello world` non-stop

actually when my code starts, prints hello world and then `goto` commands directs program step to the `my_loop` section and it will repeat again and again.

###### NOTE: that TAB before `mem 'hello world'...` line is not required. this is writen only to have beautiful code

look at this example:

```bash
set $i; mem 1; copy $i;

section loop;
    mem str($i) + '\n'; out ^; # print $i
    mem $i + 1; copy $i; # add 1 to $i
mem $i < 10; gotoif loop; # check the condition in `mem` and use gotoif command
```

the output of this code is
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

we have 3 operations about section system:
- section
- goto
- gotoif

### section
this command gets name of section as parameter like above examples. this is for declare the section

### goto
goto gets a name as section name and goto to that section.

### gotoif
gotoif checks `mem` and if mem is True, will go to wanted section. if not, do nothing and continue


look at this example:

```bash
# read age from user
mem 'enter your age: '; out ^;
set $age;
read $age;
mem int($age); copy $age;

mem $age > 18; gotoif age_is_more_than_18; # if age is more than 18, goto age_is_more_than_18 section

# if not, this line will run and program goes to age_is_less_than_18
goto age_is_less_than_18;

section age_is_more_than_18;
    mem 'you are more than 18\n'; out ^;
    goto after_if;

section age_is_less_than_18;
    mem 'you are less than 18\n'; out ^;

section after_if;

mem 'program ends\n'; out ^;
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



# Aliases
alias is a system to make alias for some codes (function).

look at this example:
```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

call say_hello;
```

output:

```
hello world
```

```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

call say_hello;
call say_hello;
```

output:

```
hello world
hello world
```


you can declare a alias and call it from everywhere. when you call a alias, all of codes inside that alias will run

for declare a alias you have to write `alias <name-of-alias>`. and write codes. then for close alias write `endalias` after codes

look at this smarter alias:
```bash
mem 'program started\n'; out ^;

alias say_hello;
    set $say_hello_name; copy $say_hello_name
    mem 'hello ' + $say_hello_name + '\n'; out ^;
    free $say_hello_name;
endalias;

mem 'parsa'; call say_hello;
```

program output:

```
program started
hello parsa
```

also you can call alias without writing `call` operation:

```bash
#call somealias;
somealias; # this is shorter code for `call somealias;`
```

### passing argument to aliases
for pass argument to the aliases, you can put value after name of alias:

```bash
alias myalias;
    out ^;
endalias;

myalias "hello";
```

output:

```
hello
```

##### how it works?
you can put a value after name of alias. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
alias say_hello;
    set $say_hello_name_tmp; copy ^ $say_hello_name_tmp;
    mem 'hello ' + $say_hello_name_tmp + '\n'; out ^;
endalias;

say_hello 'parsa';
```

output:

```
hello parsa
```



# Work with files
there is two operations for working with files in pashmak: `fread`, `fwrite`

### read a file
```bash
mem '/path/to/file.txt'; fread ^;
set $content; copy $content;
mem 'content of file is: ' + $content; out ^;
```

the content of `/path/to/file.txt'` is:
```
hello world. this is my content
bye
```

output of the program:

```
content of file is: hello world. this is my content
bye
```

you can put a variable instead `^` in `fread ^` as path of file to read

after fread command, content of readed file will put in the mem and you can access that

### write on file
```bash
set $filepath; mem '/path/to/file.txt'; copy $filepath;

mem 'content of file';
fwrite $filepath ^; # write mem (^) on the $filepath (/path/to/file.txt)
```

the `fwrite` operation gets two argument: file path and new content of file



# Arrays
arrays are a list from variables

look at this example:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

out $names; # output: ['parsa' , 'pashmak' , 'jack']
mem $names[0]; out ^; # output: parsa
mem $names[1]; out ^; # output: pashmak
mem $names[2]; out ^; # output: jack
```

this is a example about array and loop:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

set $i; mem 0; copy $i;

section loop;
    mem $names[$i] + '\n'; out ^;
    mem $i + 1; copy $i;
mem $i < len($names); gotoif loop;
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### arraypush
you can add new item to a array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
out $myarray; # output: ['red' , 'green' , 'blue']

mem 'yellow'; arraypush $myarray ^; # add mem (^) to the $myarray
out $myarray; # output: ['red' , 'green' , 'blue' , 'yellow']
```

`arraypush` operation gets two argument: array and new item you want to add to the array

### arraypop
you can delete a item from array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
out $myarray; # output: ['red' , 'green' , 'blue']

mem 1; arraypop $myarray ^; # remove index mem (^) from $myarray
out $myarray; # output: ['red' , 'blue']
```

`arraypop` operation gets two argument: array and index of that item you want to be remove from array



# Try and Endtry statement

we may recive some errors in our program. for example:

```bash
out $this_var_not_found;
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined operation
outttt ^;
```

output:

```
SyntaxError:
        undefined operation "outttt"
```

they are errors

##### but how to handle errors?

we can handle errors with `try-endtry` statement.

look at this example:

```bash
try handle_error;
    out $somevar;
endtry;

goto after_error;

section handle_error;

mem 'some errors raised\n'; out ^;

section after_error;
```

when you write code between `try <section-name> ... endtry`, errors will not raised in them and if an error is raised, that section where passed to try operation will run.

this is helpful.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error;
    out $somevar;
endtry;

goto after_error;

section handle_error;

set $ex; copy $ex; # copy mem (^) to $ex variable (this includes information about raised error)
out $ex; # output: {"type": "VariableError" , "message": "undefined variable $somevar"}...

section after_error;
```



# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
mem '/tmp'; chdir ^;

# or

set $path; mem '/tmp'; copy $path;
chdir $path; # use variable
```

### cwd
get current working directory.

```bash
cwd;
out ^;
```

output:

```
/tmp
```

this command puts current working directory path in mem

### system
you can run shell commands by this command:

```bash
mem 'ls /tmp'; system ^;

# or

set $cmd; mem 'ls /tmp'; copy $cmd;
system $cmd; # use variable
```

### return
this command exits program

look at this example:

```bash
mem 'first print\n'; out ^;

return;

mem 'last print\n'; out ^; # this will not print
```

output:

```
first print
```

###### return with exit code:

```bash
mem 'hello world\n'; out ^;
return 1;
```

exit code of program will be `1`



# Include scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm` , `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a alias to show fibonaccy algo.

###### fib.pashm:
```bash
alias fib;
    set $a $b;
    mem 1; copy $a;
    mem 1; copy $b;

    section 10;
        mem str($b) + '\n'; out ^;

        set $tmp_a $tmp_b;
        copy $a $tmp_a;
        copy $b $tmp_b;

        copy $tmp_b $a;

        mem $tmp_a + $tmp_b; copy $b;
    mem $b < 10000; gotoif 10;
endalias;
```

###### app.pashm:
```bash
mem 'fib.pashm'; include ^;

call fib;
```

when we run `include` command and pass a file path from mem (^) or variable to that, content of thet file will include in our code and will run. for example, here we used a alias from the `fib.pashm` file.

this is very useful.



# Eval

you can run pashmak code from string.

look at this example:

```bash
mem 'mem "hello world from string\n"; out ^;'; eval ^;
```

output:

```
hello world from string
```

this code is runed from a string

look at this example:

```bash
set $code;
mem 'enter some code: '; out ^;
read $code;

eval $code;
```

output:

```
enter some code: <input>mem 'hi\n'; out ^;
hi
```

the above code gets a string from user and runs that as pashmak code.

## run python code
you can run python code like `eval` with `python` command:

```bash
set $code; mem 'print("hello world from python")'; copy $code;
python $code;
```

output:

```
hello world from python
```



# General Modules
pashmak has some general libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `include` operation.

look at this example:

```bash
mem '@hash'; include ^;
mem '@time'; include ^;
mem '@module_name'; include ^;

# or using stdlib
mem '@stdlib'; include ^;
import '@hash';

# ...
```

you have to give name of module with a `@` before that to the include operation.

### hash module
with hash module, you can calculate hash sum of values:

```bash
mem '@hash'; include ^;

hash.sha256 "hello"; # also you can use hash.md5 and...
out ^; # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

###### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this alias calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

also you can use `hash.md5` aliases and...

### time module
with this module, you can work with time.

###### time.time
this alias gives you current UNIX timestamp:

```bash
mem '@time'; include ^;

time.time; # this is shorter of `call time.time`
out ^; # output is some thing like this: `1600416438.687201`
```

when you call this alias, this alias puts the unix timestamp into mem and you can access and use that.

###### time.sleep
this alias sleeps for secounds:

```bash
mem '@time'; include ^;

time.sleep 2; # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this alias, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` alias, then program will sleep for value of `mem` as secounds

## random module
this module makes random numbers

###### random.randint
```bash
mem '@random'; include ^;

random.randint [1, 10]; # generates a random int between 1 and 10

out ^; # and puts generated random number in mem and you can access that
```

###### random.random
```bash
mem '@random'; include ^;

random.random; # generates a random float less that 1

out ^; # and puts generated random number in mem and you can access that
```

###### more modules comming soon...



# Stdlib
`stdlib` is a very important and useful module.
this module make the pashmak syntax easy.

look at this example:

```bash
mem '@stdlib'; include ^;

# print
print "hello world"; # INSTEAD OF `mem 'hello world'; out ^;`

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
```

this module includes some aliases to make the pashmak syntax better.



