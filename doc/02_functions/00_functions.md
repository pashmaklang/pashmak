# Functions
A function is a system to make an alias for some code.

Look at this example:
```bash
func say_hello
    println('hello world')
endfunc

say_hello()
```

Note: You can use the keyword `end` instead of `endfunc`. There is no difference.

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


You can declare a function and call it from anywhere. When you call a function, all of the code inside that function will be run.

To declare a function you have to write `func <name-of-function>` and write the code. Then, to close the function, write `endfunc` after the code.

Look at this smarter function:
```bash
mem 'program started\n'; print(^)

func say_hello
    $name = ^ # copy the mem to $name
    println('hello ' + $name)
endfunc

mem 'parsa'; say_hello()
```

The program output:

```
program started
hello parsa
```

##### NOTE: a function name should not contain the `()+-/*%=}{<>[],. ` characters (literal characters)

## Passing arguments to functions
To pass an argument to a function, you can put the value after the name of the function:

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

But with a better syntax, you only need to run `some_func('something')`.

### How does it work?
You can put a value after the name of the function. This value will be put in the mem and you can access this argument from the mem.

Look at this example:

```bash
func say_hello
    $name = ^ # copy the mem (the argument passed to the function) to $name
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

output:

```
hello parsa
```

Also you can pass more than 1 argument to functions:

```bash
func say_hello
    $args = ^ # copy the mem to $args
    $first_name = $args[0]
    $last_name = $args[1]
    println('hello ' + $first_name + ' ' + $last_name)
endfunc

say_hello('parsa', 'shahmaleki')
```

Arguments should be separated with `,`. This will make an array in the mem and the function can access that array and use the arguments.

To copy the function argument (in the mem) to a variable, use this syntax:

```bash
func say_hello
    $name = ^
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

But we can also use this syntax to copy the function argument to a variable more easily:

```bash
func say_hello ($name)
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

#### NOTE: the space between `hello` and `($name)` is not required.

We can put `($varname)` after the name of the function (with a space between them) and the mem will be copied automatically into that variable.

Also you can pass more than 1 argument to functions:

```bash
func say_hello($name, $family)
    println('hello ' + $name + ' ' + $family)
endfunc

say_hello('parsa', 'shahmaleki')
```

You should separate them with `,`.

### Argument default values
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

Also we can change the default:

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

Like in the above example, keyword arguments allow you to set the exact value of a specific argument by the name of the argument.

### Local variables & global variables

Look at this example:

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

There is a note here. Why, when we changed the `$name` variable in the `myfunc` function, was it still the old value after the function?

The `$name` that was set in `myfunc` is local. This means that it does not point to the global `$name` in our program.

The variables set in functions are local. Also functions cannot change global variables.

The variable environment in functions is isolated.

So, how to change a global variable from a function?

The answer is in `gset`:

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

Here, the `gset` function gets two parameters: first, the global variable name and second, the new value for it.

This command sets the value of that variable globally.

Also you can get a global variable using the `gget` function:

```bash
println(gget('var_name'))
```

##### NOTE: after running gset, the new value will be set for the global variable, but it will not be set locally. So, after using gset, also update the local value if you want

### Handling the output of functions

When you call a function, that function may return an output. This output value should be saved in the mem.

Look at this example:

```bash
func add_two_nums($num1, $num2)
    $sum = $num1 + $num2 # add two numbers
    mem $sum # put the result into the mem
endfunc

# now we call this function
add_two_nums(10, 5)
$result = ^ # the function output is in the mem and we copy the mem to the $result variable
println($result)
```

output:

```
15
```

Also you can use the `return` command instead of the above method.

For example:

```bash
func get_data
    println('start')
    return 'the data'
    println('end') # this will not be run
endfunc

println(get_data())
```

output:

```
start
the data
```

Actually, with the `return` command, the value will be put in the mem as the output and the function will be finished (commands after return will not be run).

### Calling functions inline
You can call a function as an argument of another function.

Look at this example:

```bash
# the say_hi function returns the string `hello <$name>`
func say_hi($name)
    return 'hello ' + $name
endfunc

# we want to call this function and print its output
println(say_hi("parsa"))
```

output:

```
hello parsa
```

In the above example, we directly called a function and passed its output as an argument of the `println` function.

Another example:

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

Another example:

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

If you put only a single variable as the argument and put a `*` before the variable name, like `*$args`, all of the arguments will be passed to the function as a tuple.

For example:

```bash
func myfunc(*$args)
    return $args[0] + $args[1]
endfunc
```

### Typed arguments
Typed arguments are arguments whose type is declared.

Normally, you can pass any type of value as arguments. For example:

```bash
func hello($something)
    println($something)
endfunc

hello('hi')
hello(100)
hello(True)
```

But sometimes you want to get only a specific type of value as an argument:

```bash
func hello(string $name, int $age)
    println($name + ' ' + str($age))
endfunc

hello('parsa', 15)
hello('pashmak', 1)
```

output:

```
parsa 15
pashmak 1
```

But if you give something other than the declared type, you will get an error:

```bash
func hello(string $name, int $age)
    println($name + ' ' + str($age))
endfunc

hello(100, 100) # the first argument should be string, but int given
```

Error output:

```
InvalidArgument: ....
```

The syntax of argument type declaration:

```bash
func func_name(<type> $name, <type> $other...)
```

For example:

```bash
func hello(string $name, $age)
    # ...
endfunc
```

### Advanced typed arguments
You can use the `|` character for setting the type of arguments with an OR operation:

```bash
func hello(str|int $a)
    println($a)
endfunc

hello('hello') # output: hello
hello(12) # output: 12

# something other than str and int
hello(True) # error: Invalid argument
```

You can separate them with `|`. The type of the argument should be one of them.

Also you can use the array item type:

```bash
func hello(str|list[int] $a)
    println($a)
endfunc

hello('hello') # output: hello
hello([]) # output: []
hello([1, 2]) # output: [1, 2]

hello([1, 2, '']) # error: InvalidArgument
```

When you write `list[int]`, it means that the argument should be a list whose items are `int`.
Also you can write `list[int|str]`, which means you want a list whose items are `int` OR `str`.
Also you can use this system in a complicated way like `list[int|list[str|int]]`...

### Return types
You can also declare the return type of functions like the arguments.

For example:

```bash
func string::hello(string $name)
    return 'hello ' + $name
endfunc

println hello('parsa')
```

output:

```
hello parsa
```

You should write return type before `::`:

```bash
func <type>::<name>...
```

Another example:

```bash
func list[int|str]::hello()...
```

If you return invalid data, the error `InvalidReturnType` will be raised.
