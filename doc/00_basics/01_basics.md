# Basics

A simple printing in Pashmak:

```bash
mem 'something to print\n'; print(^)
```

or

```bash
print('something to print\n')
```

### How does it work?

First, we go through the Pashmak syntax structure.
The base structure of the Pashmak syntax is this:

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

##### NOTE: the `;` at the end of lines is not required. You can write your code without `;` IF you don't want to write two or more commands on one line

Here, `mem` is a command and `'something to print\n'` is its argument, and
`print` is a command and `^` is its argument.

But what does this code do?

When you run the script in the terminal:

```bash
pashmak myscript.pashm # or any filename you saved the code in
```

##### NOTE: the `.pashm` extension for Pashmak scripts is not required. You can run any file with any name as a Pashmak script

You will get this output:

```
something to print
```

This code prints `'something to print'` on the stdout.
But how?

First, the `mem` command brings the string `'something to print'` into memory, and then the `print` command prints the memory value on the screen.

## What is `mem`?
The mem is a temporary place to make and calculate values.

```bash
mem 'hello world'
print(^) # the ^ is the pointer to the mem
```

The `^` is the pointer to the mem.

You can also write the code like this to have shorter code (we have to use `;` to separate them):

```bash
mem 'hello world\n'; print(^)
```

###### NOTE: remember to put \n when you want to go to the next line

### The mem is temporary

Look at this example:

```bash
mem 'some thing\n'

print(^) # output: some thing

print(^) # output: None
```

Why was the value printed correctly on the screen the first time the mem value was read, but `None` was printed the second time?

Because the memory is a temporary place. When you read the memory, it is emptied automatically after the read.

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

###### NOTE: the # character is the comment symbol. You can put comments in your code after the # character. Comments have no effect on the program

### More about mem
You can calculate everything in the `mem`.

For understanding this, look at the following examples:

```bash
mem 'hi there'; print(^) # output: hi there

# you can concatenate strings
mem 'first string ' + 'last string'; print(^) # output: first string last string

# run math calculations
mem 2*7; print(^) # output: 14

mem 3*(2+1); print(^) # output: 9

mem str(7*7) + ' is sum'; print(^) # output: 49 is sum
# the `str` function gets a value and converts it to a string.
# here you can not concatenate a number with a string. first you need to convert the num to a str with str()
```

**The mem structure is handled by Python (the eval function) and you can use all of Python's features in the mem calculation**

### Printing without using mem
This is an easier syntax for printing:

```bash
mem 'hello world\n'; print(^)

# this is easier
print('hello world\n')

print(str(2*2))

print('hello ' + 'parsa\n')

print('num is ' + str(100+7))
```

You can use all of the features of `mem` in the arguments of commands like in the above example.

After this, we never use `mem <something>; print(^)` pattern for printing, and we just use `print` command.

### println

If you want to print something and go to the next line, you have to put `\n` at the end of the string.

But with the `println` function, you don't need to use `\n`; it will be added automatically:

```bash
println('hello world')
```

output:

```
hello world<nextline>
```

Also there is an alias for `println`, which is `printl`:

```bash
#println("hello world")
printl("hello world")
```

### Multiline
You can write one command on more than one line. This helps you to write clean code.

example:

```bash
println(
    'Hello ' +
    'World'
)
```

#### Writing a multiline string
The multiline syntax for strings (text) is different. You should put a `\` at the end of lines.

For example:

```bash
println('hello\
 world')
```

output:

```
hello world
```

another example:

```bash
println(\
    'hello world\
\nthis is a simple multiline\
    '\
)
```

output:

```
hello world
this is a simple multiline
```

You need to put a `\` at the end of lines to continue them on the next line.
