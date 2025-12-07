# Functions
Function is a system to make alias for some codes (function).

Look at this example:
```bash
func say_hello
    println('hello world')
endfunc

say_hello()
```

Note: You can use keyword `end` instead of `endfunc`. It is not different.

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


You can declare a function and call it from everywhere. When you call a function, all of codes inside that function will be ran.

To declare a function you have to write `func <name-of-function>` and write codes. Then to close function write `endfunc` after codes.

Look at this smarter function:
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

## Passing argument to Functions
To pass argument to the Functions, you can put value after name of function:

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

But with better syntax, you only need to run `some_func('something')`.

### How it works?
You can put a value after name of function. This value will put in mem and you can access this argument from mem.

Look at this example:

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

Also you can pass more than 1 argument to functions:

```bash
func say_hello
    $args = ^ # copy mem to $args
    $first_name = $args[0]
    $last_name = $args[1]
    println('hello ' + $first_name + ' ' + $last_name)
endfunc

say_hello('parsa', 'shahmaleki')
```

Arguments should be split with `,` and this will make a array in mem and function can access that array and use arguments.

To copy function argument (in mem) to a variable, using this syntax:

```bash
func say_hello
    $name = ^
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

But also we can use this syntax to copy function argument to variable with better syntax:

```bash
func say_hello ($name)
    println('hello ' + $name)
endfunc

say_hello('parsa')
```

#### NOTE: that space between `hello` and `($name)` is not required.

We can put `($varname)` after name of function (with a space between them) and mem will copy automatically in that variable.

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

There is a note. Why when we changed `$name` variable in `myfunc` function, this was the old value after function?

The `$name` where was set in `myfunc`, is local. Means that do not points to global `$name` in out program.

The set variables in Functions, are local. Also Functions cannot change global variables

The variable environment in Functions are isolated.

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

Here, `gset` function gets two parameters: first, global variable name and second, new value for that

This command sets value of that variable globally.

Also you can get a global variable using `gget` function:

```bash
println(gget('var_name'))
```

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)

### Handle functions output

When you call a function, that function may return a output. This value as output should be save in mem

Look at this example:

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

Also you can use `return` command instead of above method.

For example:

```bash
func get_data
    println('start')
    return 'the data'
    println('end') # this will not be ran
endfunc

println(get_data())
```

output:

```
start
the data
```

Actually, in `return` command, value will be put in the mem as output and function will be finished(commands after return will not be ran).

### Inline calling functions
You can call a function as argument of another function.

Look at this example:

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

In the above example, we directly called a function and passed the output of that as argument of `println` function.

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

If you put only a single variable as argument and put a `*` before variable name, like `*$args`, All of arguments will be passed as a tuple to the function.

For example:

```bash
func myfunc(*$args)
    return $args[0] + $args[1]
endfunc
```

### Typed arguments
Typed arguments, are arguments that type of them are declared.

Normally, you can pass any type of value as arguments. For example:

```bash
func hello($something)
    println($something)
endfunc

hello('hi')
hello(100)
hello(True)
```

But, sometimes you want get only a specific type of value as argument:

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

But if you give something else of declared type, you will give error:

```bash
func hello(string $name, int $age)
    println($name + ' ' + str($age))
endfunc

hello(100, 100) # first argument should be string, but int given
```

Error output:

```
InvalidArgument: ....
```

Syntax of argument type defining:

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
You can use `|` char for setting type of arguments with OR operation:

```bash
func hello(str|int $a)
    println($a)
endfunc

hello('hello') # output: hello
hello(12) # output: 12

# something else of str and int
hello(True) # error: Invalid argument
```

You can separate them with `|`. Type of argument should be one of them.

Also you can use array item type:

```bash
func hello(str|list[int] $a)
    println($a)
endfunc

hello('hello') # output: hello
hello([]) # output: []
hello([1, 2]) # output: [1, 2]

hello([1, 2, '']) # error: InvalidArgument
```

When you write `list[int]`, means that argument should be a list that items should be `int`.
Also you can write `list[int|str]` means you want a list that items should be `int` OR `str`.
Also you can use this system complicated like `list[int|list[str|int]]`...

### Return types
You can also declare return type of functions like arguments.

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

If you return a invalid data, error `InvalidReturnType` will be raised.
