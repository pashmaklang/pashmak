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

#### print ;
for print `;` character, put a `\` before semicolon:

```bash
mem 'this is \; semicolon\n'; out ^;
```

output:

```
this is ; semicolon
```
