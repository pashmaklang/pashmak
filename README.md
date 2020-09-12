# Pashmak programming language
hi there. this is pashmak programming language. pashmak is a interpreter wrote in python.
the pashmak scripts has a cool syntax.

### hello world!
this is a simple hello world script in pashmak:

```bash
mem 'hello world\n'; out ^;
```

read the following Documentation to learn pashmak

# Documentation



## Basics

a simple printing in screen in pashmak:

```bash
mem 'some thing to print\n'; out ^;
```

#### how it works?

before every thing, we'll browse about pashmak syntax structure.
the base structure of pashmak syntax, is this:

```bash
<operation> [arguments];
<operation> [arguments];
<operation> [arguments]; <operation> [arguments];
```

some thing like this. in this example, we have two operations:

```bash
mem 'some thing to print\n'; # first operation
out ^; # second operation
```

in here, mem is a operation and `'something to print\n'` is argument of that, and
out is a operation and `^` is argument of that.

but this code doing what?

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

first, `mem` command brings the string `'some thing to print'` on the memory, and next `out` command prints the memory value on screen.

### what is `mem`?
you cannot print any thing like this:

```bash
out 'hello world\n';
```

because commands in pashmak never gets a value directly.
if you wanna pass a value to the commands, need to use `mem` command to load that value.
in this example, we first loading the `'some thing to print'` with mem command, and next pass value of mem to the out command:

```bash
mem 'hello world';
out ^; # the ^ is pointer to value of mem
```

the ^ is pointer to value of mem

you can also write the code like this to have shorter code:

```bash
mem 'hello world\n'; out ^;
```

###### NOTE: remember to put \n when you want to go next line

#### mem is temp

look at this example:

```bash
mem 'some thing\n';

out ^; # output: some thing

out ^; # output: None
```

why in the first time while reading mem value, the value correctly printed on screen, but in the second time the None value printed?

because memory is temporary. when you read the memory, that will be empty automatic after read.

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

###### NOTE: the # is comment operation. you can put comment in your code after # character


### more about mem
you can calculate every thing in mem

for know this, look at the following examples:

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

the `mem` command is very very important and you need to use it every where



## Variables

variables are like a put where you can save a data on them

to set and handle variables in pashmak, we work with three commands: `set`, `copy`, `free`

```bash
set %myvar; # set a variables named %myvar
mem 'this is data'; # bring string 'this is data' to mem
copy ^ %myvar; # copy mem (^) to %myvar

out %myvar; # output: this is data
```

###### NOTE: always put % before name of variable every where

also you can set more than one variables with `set` command:

```bash
set %var1 %var2 %var3;
```

### use variables in mem

look at this example:

```bash
set %name; # set name variable
mem 'parsa'; copy ^ %name; # copy 'parsa' string to name variable

mem 'hello ' + %name + '\n'; out ^; # output: hello parsa

set %num; mem 12; copy ^ %num;
mem %num*5; out ^; # output: 60

set %num2; mem 4; copy ^ %num2;

mem %num * %num2 + 1; out ^; # output: 49
```

#### how it works?
we declared a %name variable and put `'parsa'` string in that

next, in mem we maked a string and paste %name variable value to `'hello '` with a \n in end of that, and we printed that mem

you can use variables in mem like that example


### free variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
set %somevar;
mem 'some value'; copy %somevar;

out %somevar; # output: some value

free %somevar;

out %somevar; # you will get VariableError: undefined variable %somevar (because it is deleted by free command)
```

also you can free more than one variable with `free` command:

```bash
free %var1 %var2 %var3; # ...
```

###### NOTE: in that example, we used `copy` command like this:

```bash
mem 'some value';
copy %somevar;
# that is alias of
copy ^ %somevar;
```

when you give just a variable to copy command, the mem will be copy in that variable

look at this example:

```bash
set %var1 %var2;

mem 'hi'; copy %var1;
mem 'bye'; copy %var2; # this is alias of `copy ^ %var2`

out %var1; # output: hi
out %var2; # output: bye

copy %var1 %var2; # copy a variable in variable

out %var1; # output: hi
out %var2; # output: hi

```

### checking a variable isset
you can check a variable exists with `isset` command

look at this example:

```bash
set %somevar %v;

isset %somevar; out ^; # output: True
isset %this_var_not_found; out ^; # output: False
isset %somevar %sassadffgdty; out ^; # output: False
isset %somevar %v; out ^; # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exists, put `True` in  memory and if all or one/more of them are not exists, put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` command

look at this example:

```bash
set %mystr %myint %myfloat %mybool;

mem 'hi'; copy %mystr;
mem 20; copy %myint;
mem 15.32; copy %myfloat;
mem False; copy %mybool;

typeof %mystr; out ^;   # output: str
typeof %myint; out ^;   # output: int
typeof %myfloat; out ^; # output: float
typeof %mybool; out ^;  # output: bool
```

this command puts the typeof variable in mem


### required command

the required command requiring an variable existing.

look at this example:

```bash
set %name;

required %name;
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#set %name;
required %name;
```

now name variable is not set, and you will get this error:

```
RequireError:
    undefined variable %name
```

the required command checks a variable is exists, if no, raising RequireError

you will know why this command is usable in the aliases section



## Read Input From User

you can read a input from user in stdin

look at this example:

```bash
set %name; # set the name variabl
mem 'what is your name? '; out ^; # print
read %name; # read a input and copy this in %name variable
mem 'hello ' + %name + '\n'; out ^; # say hello to %name :)
```

when we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for a input, and when you type some thing and press enter, program says `hello <your-input>`

for example in here i entered `parsa` as input and program says `hello parsa`

we can get input from user like this example


also look at this example:

```bash
set %num1 %num2;

mem 'enter first number: '; out ^;
read %num1;

mem 'enter second number: '; out ^;
read %num2;

# now, %num1 and %num2 are string. we convert string to int:
mem int(%num1); copy %num1;
mem int(%num2); copy %num2;

# now we want to plus them
set %sum;
mem %num1 + %num2; copy %sum;

mem str(%sum) + '\n'; out ^;
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two number from user and shows sum of them



# Sections
section is a system to make a pointer to a part of code. it will use for create loop, if and...

look at this example:
```bash
section my_loop;
    mem 'hello world\n'; out ^;
goto my_loop;
```

this code prints `hello world` non stop

actually when my code starts, prints hello world and then `goto` commands direct program step to the `my_loop` section and it will repeat again and again.

###### NOTE: that <TAB> before `mem 'hello world'...` line is not required. this wrote only to have beautiful code

look at this example:

```bash
set %i; mem 1; copy %i;

section loop;
    mem str(%i) + '\n'; out ^; # print %i
    mem %i + 1; copy %i; # add 1 to %i
mem %i < 10; gotoif loop; # check the condition in `mem` and use gotoif command
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
this command gets a name of section as parameter like that examples. this is for declare the section

### goto
goto gets a name as section name and goto to that section.

### gotoif
gotoif checks `mem` and if mem is True, will goto to wanted section. if not, do nothing and continue


look at this example:

```bash
# read age from user
mem 'enter your age: '; out ^;
set %age;
read %age;
mem int(%age); copy %age;

mem %age > 18; gotoif age_is_more_than_18; # if age is more than 18, goto age_is_more_than_18 section

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
alias is a system to make alias for some codes.

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


you can declare a alias and call it from every where. when you call a alias, all of codes inside that alias will run

for declare a alias you have to write `alias <name-of-alias>`. and write codes. then for close alias write `endalias` after codes

look at this smarter alias:
```bash
mem 'program started\n'; out ^;

alias say_hello; required %say_hello_name; # declare alias and require variable %say_hello_name
    mem 'hello ' + %say_hello_name + '\n'; out ^;
    free %say_hello_name;
endalias;

set %say_hello_name; mem 'parsa'; copy %say_hello_name;
call say_hello;
```

program output:

```
program started
hello parsa
```



# Work with files
to work with files in pashmak, is simple operations

### read a file
```bash
mem '/path/to/file.txt'; fread ^;
set %content; copy %content;
mem 'content of file is: ' + %content; out ^;
```

the content of `/path/to/file.txt'` is:
```
hello world. this is my content
by
```

output of the program:

```
content of file is: hello world. this is my content
by
```

you can put a variable instead ^ in `fread ^` as path of file to read

after fread command, content of readed file will put in the mem and you can access that

### write on file
```bash
set %filepath; mem '/path/to/file.txt'; copy %filepath;

mem 'content of file';
fwrite %filepath ^; # write mem (^) on the %filepath (/path/to/file.txt)
```



# Arrays
arrays are a list from variables

look at this example:

```bash
set %names;
mem ['parsa' , 'pashmak' , 'jack'];
copy %names;

out %names; # output: ['parsa' , 'pashmak' , 'jack']
mem %names[0]; out ^; # output: parsa
mem %names[1]; out ^; # output: pashmak
mem %names[2]; out ^; # output: jack
```

this is a example about array and loop:

```bash
set %names;
mem ['parsa' , 'pashmak' , 'jack'];
copy %names;

set %i; mem 0; copy %i;

section loop;
    mem %names[%i] + '\n'; out ^;
    mem %i + 1; copy %i;
mem %i < len(%names); gotoif loop;
```

output:

```
parsa
pashmak
jack
```

that prints names one by one

### arraypush
you can add a item to array:

```bash
set %myarray; mem ['red' , 'green' , 'blue']; copy %myarray;
out %myarray; # output: ['red' , 'green' , 'blue']

mem 'yellow'; arraypush %myarray ^; # add mem (^) to the %myarray
out %myarray; # output: ['red' , 'green' , 'blue' , 'yellow']
```

### arraypop
you can delete a item from array:

```bash
set %myarray; mem ['red' , 'green' , 'blue']; copy %myarray;
out %myarray; # output: ['red' , 'green' , 'blue']

mem 1; arraypop %myarray ^; # remove index mem (^) from %myarray
out %myarray; # output: ['red' , 'blue']
```



# Try and Endtry statement

we may get some errors in some places in program. for example:

```bash
out %this_var_not_found;
```

output:

```
VariableError:
    undefined variable %this_var_not_found
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
    out %somevar;
endtry;

goto after_error;

section handle_error;

mem 'some errors raised\n'; out ^;

section after_error;
```

when you write code between `try <section-name> ... endtry`, if there is some errors, error will not raised and the section passed to try command will run.

this is helpful.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error;
    out %somevar;
endtry;

goto after_error;

section handle_error;

set %ex; copy %ex;
out %ex; # output: {"type": "VariableError" , "message": "undefined variable %somevar"}...

section after_error;
```



