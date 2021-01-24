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

## passing argument to Functions
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

### how it works?
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

Also you can pass more than 1 argument to functions:

```bash
func say_hello($name, $family)
    println('hello ' + $name + ' ' + $family)
endfunc

say_hello('parsa', 'shahmaleki')
```

You should split them with `,`.

### Arguments default values
You can set some default values for arguments:

```bash
func hello($name, $end='!')
    println('Hello ' + $name + $end)
endfunc

hello('parsa')
```

output:

```
Hello parsa!
```

Also we can change default:

```bash
func hello($name, $end='!')
    println('Hello ' + $name + $end)
endfunc

hello('parsa', '.')
```

output:

```
Hello parsa.
```

### Keyword arguments
Also functions can get **Keyword arguments**.

For example:

```bash
func hello($name, $word='Hello', $end='!')
    println($word + ' ' + $name + $end)
endfunc

hello('parsa') # output: Hello parsa!
hello('parsa', 'Hi') # output: Hi parsa!
hello('parsa', 'Hi', '.') # output: Hi parsa.

# But you can use keyword arguments:
hello('parsa', end='.') # output: Hello parsa.
```

Like above example, keyword arguments allows you to set exactly value of a specify argument by name of argument.

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

also you can Get a global variable using `gget` function:

```bash
println(gget('var_name'))
```

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)

### handle functions output

when you calling a function, that function may return a output. this value as output should be save in mem

look at this example:

```bash
func add_two_nums($num1, $num2)
    $sum = $num1 + $num2 # add two numbers
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
func add_two_nums($num1, $num2)
    return $num1 + $num2
endfunc

$result = add_two_nums(10, 5)
println('sum is ' + str($result))
```


### Dynamic arguments
You can get arguments dynamically as a list.

For example:

```bash
func myfunc(*$args)
    println($args)
endfunc

myfunc('foo', 'bar')
myfunc('hello', 100, False)
```

output:

```
('foo', 'bar')
('hello', 100, False)
```

If you put only a single variable as argument and put a `*` before variable name, like `*$args`, All of arguments will be passed as a tuple(list) to the function.

For example:

```bash
func myfunc(*$args)
    return $args[0] + $args[1]
endfunc
```

The problem is that, when function has Only One Argument, `$args/etc` is not a Tuple(list). in the above example, this is show.

But how to fix this? When i run `hello('hi')`, argument variable should be `('hi',)`(a tuple) but this is `'hi'`self of variable) I want to do something to always(With any argument count) arguments be a tuple.

To do this, you can use `format_args` function.

for example:

```bash
func hello(*$args)
    $args = format_args($args)
    # ...
endfunc

hello('hello') # output: ('hello',)
```

With this function, this problem will be solved.
