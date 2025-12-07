# Variables

Variables are like a pot which you can save data in them.

Look at this example:

```bash
$myvar = 'this is data'

println($myvar) # output: this is data
```

##### NOTE: always put $ before name of variable everywhere

Declaring variables is so easy, only you have to write `$<name_of_variable>`.

Also you can set variables without value like this example:

```bash
$var1
$var2; $var3 # default value is null
```

##### NOTE: variable name should not contains `()+-/*%=}{<>[], ` chars(literal chars)

## Using variables in mem calculation

look at this example:

```bash
$name = 'parsa' # set name variable

println('hello ' + $name) # output: hello parsa

$num = 12
println($num * 5) # output: 60

$num2 = 4

println($num * $num2 + 1) # output: 49
```

### Copy variables in other variables

Look at this example:

```bash
$var1 = 'hi'
$var2 = 'bye'

println($var1) # output: hi
println($var2) # output: bye

$var2 = $var1

println($var1) # output: hi
println($var2) # output: hi

$name = 'parsa'
$message = 'hello' + $parsa # you can use all of mem calculation features in here
println($message) # output: hello parsa
```

#### NOTE: allowed characters for variable name are `A-Za-z`(or any alpha-bet characters in other languages), `&._` characters.

### Put `mem` value to variable

We can set value of mem to variables with this code:

```bash
mem 'something'
$myvar = ^
```

If you put `^` (mem symbol) as value, memory value will put in the variable.

Also you can use that mem alongside another values.

for example:

```bash
mem 'parsa'
$message = 'my name is ' + ^
println($message) # output: my name is parsa

mem 10
println((^ + 5) * 2) # output: 30
```

### Free (delete) variables
When you set a variable, that var is in memory. You can delete that var with `free` command:

```bash
$somevar = 'some value'
println($somevar) # output: some value

free('somevar')

println($somevar) # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
```

Also you can make free more than one variables with `free` command:

```bash
free('var_name')
```

### Checking if a variable is set
You can check a variable existence with `isset` command.

Look at this example:

```bash
$somevar; $v # set `somevar` and `v` variables

println(isset('somevar')) # True
println(isset('v')) # True
println(isset('not_found')) # False
```

(The `True` and `False` are Python booleans).

#### How it works?

The isset command gets one or more variable names and if all of those vars exist, it will put `True` in memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

You can get the data type of a variable with `typeof` function.

Look at this example:

```bash
$mystr = 'hi'
$myint = 20
$myfloat = 15.32
$mybool = False

typeof($mystr); println(^) # output: <class 'str'>
typeof($myint); println(^) # output: <class 'int'>
typeof($myfloat); println(^) # output: <class 'float'>
typeof($mybool); println(^) # output: <class 'bool'>
# also you can use this syntax and use function directly
println(typeof($myint))
```

This command puts the typeof variable in mem.

(All of Pashmak datatypes are handled by python and you can use all of python variables features).

### Python datatype methods
The datatype of the Pashmak variables, is handled by python. This means you can use all python methods on them.

For example:

```bash
$mystring = '  hello world          '
println($mystring->strip()) # output: `hello world`
```

#### NOTE: in python, for calling function or access to property of a object, we use `.` character, but in Pashmak we use `->` symbol(like php)

### `get()` and `set()` functions
`get()` function can return value of a variable by name as string.

For example:

```bash
$name = 'parsa'

println(get('name'))
```

output:

```
parsa
```

Also `set` function sets value of a variable by name and value:

```bash
$name = 'parsa'
println(get('name'))

set('name', 'pashmak')

println($name)
```

output:

```
parsa
pashmak
```
