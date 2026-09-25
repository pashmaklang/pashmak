# Variables

Variables are like pots which you can save data in.

Look at this example:

```bash
$myvar = 'this is data'

println($myvar) # output: this is data
```

##### NOTE: always put $ before the name of a variable everywhere

Declaring variables is very easy; you only have to write `$<name_of_variable>`.

Also you can declare variables without a value like in this example:

```bash
$var1
$var2; $var3 # default value is null
```

##### NOTE: a variable name should not contain the `()+-/*%=}{<>[], ` characters (literal characters)

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

### Copying variables into other variables

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
$message = 'hello ' + $name # you can use all of the mem calculation features here
println($message) # output: hello parsa
```

#### NOTE: the allowed characters for a variable name are `A-Za-z` (or any alphabet characters in other languages) and the `&._` characters.

### Put the `mem` value into a variable

We can set the value of the mem into variables with this code:

```bash
mem 'something'
$myvar = ^
```

If you put `^` (the mem symbol) as the value, the memory value will be put in the variable.

Also you can use that mem alongside other values.

for example:

```bash
mem 'parsa'
$message = 'my name is ' + ^
println($message) # output: my name is parsa

mem 10
println((^ + 5) * 2) # output: 30
```

### Free (delete) variables
When you set a variable, that var is in memory. You can delete that var with the `free` command:

```bash
$somevar = 'some value'
println($somevar) # output: some value

free('somevar')

println($somevar) # you will get VariableError: undefined variable $somevar (because it was deleted by the free command)
```

Also you can free more than one variable with the `free` command:

```bash
free('var_name')
```

### Checking if a variable is set
You can check a variable's existence with the `isset` command.

Look at this example:

```bash
$somevar; $v # set `somevar` and `v` variables

println(isset('somevar')) # True
println(isset('v')) # True
println(isset('not_found')) # False
```

(The `True` and `False` are Python booleans).

#### How does it work?

The isset command gets one or more variable names, and if all of those vars exist, it will put `True` in memory, and if one or more of them do not exist, it will put `False` in memory

### typeof command

You can get the data type of a variable with the `typeof` function.

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
# also you can use this syntax and use the function directly
println(typeof($myint))
```

This command puts the type of the variable in the mem.

(All Pashmak datatypes are handled by Python and you can use all of Python's variable features).

### Python datatype methods
The datatypes of Pashmak variables are handled by Python. This means you can use all Python methods on them.

For example:

```bash
$mystring = '  hello world          '
println($mystring->strip()) # output: `hello world`
```

#### NOTE: in Python, for calling a function or accessing a property of an object, we use the `.` character, but in Pashmak we use the `->` symbol (like PHP)

### `get()` and `set()` functions
The `get()` function can return the value of a variable by its name as a string.

For example:

```bash
$name = 'parsa'

println(get('name'))
```

output:

```
parsa
```

Also the `set` function sets the value of a variable by name and value:

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
