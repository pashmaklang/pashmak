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
