# Functions
function is a system to make alias for some codes (function).

look at this example:
```bash
func say_hello;
    println 'hello world';
endfunc;

say_hello;
```

output:

```
hello world
```

```bash
func say_hello;
    println 'hello world';
endfunc;

say_hello;
say_hello;
```

output:

```
hello world
hello world
```


you can declare a function and call it from everywhere. when you call a function, all of codes inside that function will run

for declare a function you have to write `func <name-of-function>;`. and write codes. then for close function write `endfunc;` after codes

look at this smarter function:
```bash
mem 'program started\n'; out ^;

func say_hello;
    $name = ^; # copy mem to $name
    println 'hello ' + $name;
endfunc;

mem 'parsa'; say_hello;
```

program output:

```
program started
hello parsa
```

### passing argument to Functions
for pass argument to the Functions, you can put value after name of function:

```bash
func myfunc;
    out ^;
endfunc;

myfunc "hello";
```

output:

```
hello
```

##### how it works?
you can put a value after name of function. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
func say_hello;
    $name = ^; # copy mem(the passed argument to function) to $name
    println 'hello ' + $name;
endfunc;

say_hello 'parsa';
```

output:

```
hello parsa
```

also you can pass more than 1 argument to functions:

```bash
func say_hello;
    $args = ^; # copy mem to $args
    $first_name = $args[0];
    $last_name = $args[1];
    println 'hello ' + $first_name + ' ' + $last_name;
endfunc;

say_hello 'parsa', 'shahmaleki';
```

arguments should be split with `,` and this will make a array in mem and function can access that array and use arguments.

we to copy function argument (in mem) to a variable, using this syntax:

```bash
func say_hello;
    $name = ^;
    println 'hello ' + $name;
endfunc;

say_hello 'parsa';
```

but also we can use this syntax to copy function argument to variable with better syntax:

```bash
func say_hello ($name);
    println 'hello ' + $name;
endfunc;

say_hello 'parsa';
```

we can put `($varname)` after name of function (with a space between them) and mem will copy automatic in that variable.
also you can don't use `()` and you can write above code like this:

```bash
func say_hello $name; # without ()
    println 'hello ' + $name;
endfunc;

say_hello 'parsa';
```

### local variables & global variables

look at this example:

```bash
func myfunc;
    $name = 'new name';
    println $name;
endfunc;

$name = 'parsa';
println $name;

myfunc;

println $name;
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
func myfunc;
    $name = 'new name';
    gset 'name', $name;
    println $name;
endfunc;

$name = 'parsa';
println $name;

myfunc;

println $name;
```

output:

```
parsa
new name
new name
```

here, `gset` command (from stdlib) gets two parameters: first, global variable name and second, new value for that

this command sets value of that variable globaly.

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)

### handle functions output

when you calling a function, that function may return a output. this value as output should be save in mem

look at this example:

```bash
func add_two_nums ($nums);
    $sum = $nums[0] + $nums[1]; # add two numbers
    mem $sum; # put result to mem
endfunc;

# now we call this function
$result = ^ add_two_nums 10, 5; # function output is in mem and we copy mem to variable $result
println $result;
```

output:

```
15
```

now, above syntax is ugly. we can write this code like this:

```bash
func add_two_nums ($nums);
    $sum = $nums[0] + $nums[1]; # add two numbers
    mem $sum; # put result to mem
endfunc;

# now we call this function
$result = ^ add_two_nums 10, 5;
println $result;
```

we write two operations in one operation to have better syntax. calling function and assigning mem (function output) to `$result`.
we just have to write variable name and an `=`, and next write `^` and them write our code after this.

like it:

```bash
$variable = ^ my_command_or_function 'my', 'arguments';
```

and them this code will run and mem value will put into the variable
