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

Also you can change value of functions. functions are like variables and can be changed.

For example:

```bash
func hi
    println('Hi')
endfunc

func bye
    println('Bye')
endfunc

hi()
bye()
```

output:

```
Hi
Bye
```

Now We can change value of this functions:

```bash
hi = bye
hi()
```

output:

```
Bye
```

Actually, in above example, We are setting `bye` into `hi`.

### Function super functions
there is some **Super functions** to handle functions at runtime.

#### Checking function exists
You can check a function exists with `func.exists` function:

```bash
if func.exists('some_func')
    some_func()
endif
```

#### Geting list of all of functions
You can get list of all of functions with `func.list` function:

```bash
$funcs = func.list()

println($funcs)
```

output:

```
['a', 'b', '...']
```

The output is a list.

#### Deleting a function
You can delete a function at runtime with `func.delete` function:

```bash
func.delete('some_func')
```

### Complicated function declaration
You can declare functions-in-functions.

Look at this example:

```bash
func foo
    func bar
        println('bar')
    endfunc

    bar()

    println('foo')
endfunc

foo()
bar()
```

output:

```
bar
foo
bar
```

Also look at this example:

```bash
func first
    println('first start')
    func second
        println('second start')
        func last
            println('last')
        endfunc
        last()
        println('second end')
    endfunc
    second()
    println('first end')
endfunc

first()
```

output:

```
first start
second start
last
second end
first end
```

**The declared function in function is accessible from outside.**

For example:

```bash
func foo
    func bar
        println('the bar')
    endfunc
endfunc

foo()

bar()
```

**How to make a function in function local?**

You should delete the function in end of parent function:

```bash
func foo
    func bar
        println('the bar')
    endfunc

    # use the function...

    func.delete(__namespace__() + 'bar')
endfunc

foo()

bar()
```

output:

```
NameError: undefined 'bar'...
```

> You will learn about that `__namespace__()` function in next sections...
