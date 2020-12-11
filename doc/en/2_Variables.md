## Variables

variables are like a pot where you can save data in it

we work with three commands: `set`, `copy`, `free`, to set and handle variables in pashmak

```bash
$myvar = 'this is data'

println $myvar # output: this is data
```

###### NOTE: always put $ before name of variable everywhere

also you can set more than one variable with `set` command:

```bash
set $var1
# or
$var1
$var2; $var3 # default value is null
```

### use variables in mem

look at this example:

```bash
$name = 'parsa' # set name variable

println 'hello ' + $name # output: hello parsa

$num = 12
println $num * 5 # output: 60

$num2 = 4 # alias of `copy ^ $num2`

println $num * $num2 + 1 # output: 49
```

#### copy variables in other variables

look at this example:

```bash
$var1 = 'hi'
$var2 = 'bye'

println $var1 # output: hi
println $var2 # output: bye

$var2 = $var1

out $var1 # output: hi
out $var2 # output: hi

```

#### NOTE: allowed characters for variable name are `A-Z`, `a-z`, `&._` characters.

### put `mem` value to variable

we can set value of mem to variables with this code:

```bash
mem 'something'
$myvar = ^
```

if you put `^` (mem symbol) as value, memory value will put in the variable

also you can use that mem alongside another values.

for example:

```bash
mem 'parsa'
$message = 'my name is ' + ^
println $message # output: my name is parsa

mem 10
println (^ + 5) * 2 # output: 30
```

### free(delete) variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
$somevar = 'some value'
println $somevar # output: some value

free $somevar

println $somevar # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
```

also you can make free more than one variable with `free` command:

```bash
free $var1 $var2 $var3 # ...
```

### checking a variable isset
you can check a variable existens with `isset` command

look at this example:

```bash
$somevar; $v # set `somevar` and `v` variables

isset $somevar; println ^ # output: True
isset $this_var_not_found; println ^ # output: False
isset $somevar $sassadffgdty; println ^ # output: False
isset $somevar $v; println ^ # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exist, it will put `True` in  memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` function.

look at this example:

```bash
$mystr = 'hi'
$myint = 20
$myfloat = 15.32
$mybool = False

typeof $mystr; println ^ # output: <class 'str'>
typeof $myint; println ^ # output: <class 'int'>
typeof($myfloat); println ^ # output: <class 'float'>
typeof($mybool); println ^ # output: <class 'bool'>
# NOTE: the `()` is not required
```

this command puts the typeof variable in mem

### required command

the required command requiring an variable existens.

look at this example:

```bash
$name

required $name
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#$name
required $name
```

now $name variable is not set, and you will get this error:

```
VariableError:
    undefined variable $name
```

the `required` command checks a variable is exists, if no, raising RequireError

### python datatype methods
datatype of the pashmak variables, is handled by python. this means you can use all python methods on them.

for example:

```bash
$mystring = '  hello world          '
println $mystring->strip() # output: `hello world`
```

#### NOTE: in python, for calling function or access to property of a object, we use `.` character, but in pashmak we use `->` symbol(like php)

## Constants
constants (consts) are even like variables, but one thing is different in constants, **Constants values cannot be changed**.

for example:

```bash
# declare the const
$&name = 'the value'

println $&name
```

output:

```
the value
```

to declare consts, you only need to put a `&` in the name of variable(location of that is not important).

```bash
$&const1 = 123
$&const2 = 'fsgdf'
# ...
```

when we try to change value of the const, we will get error:

```bash
$&name = 'the name'

$&name = 'new value'
```

output:

```
ConstError: "$&name" is const and cannot be changed...
```

also you can **declare** a constant, but set value of that later.

for example:

```bash
$&name # only declare constant, default value is `None`

# set value
$&name = 'parsa'

println $&name
```

output:

```
parsa
```
