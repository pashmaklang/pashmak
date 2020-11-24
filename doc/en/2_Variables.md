## Variables

variables are like a pot where you can save data in it

we work with three commands: `set`, `copy`, `free`, to set and handle variables in pashmak

```bash
set $myvar # set a variables named $myvar
mem 'this is data' # bring string 'this is data' to mem
copy ^ $myvar # copy mem (^) to $myvar

println $myvar # output: this is data
```

###### NOTE: always put $ before name of variable everywhere

also you can set more than one variable with `set` command:

```bash
set $var1 $var2 $var3 # default value is null
```

### use variables in mem

look at this example:

```bash
set $name # set name variable
mem 'parsa'; copy ^ $name # copy 'parsa' string to name variable

println 'hello ' + $name # output: hello parsa

set $num; mem 12; copy ^ $num
println $num * 5 # output: 60

set $num2; mem 4; copy $num2 # alias of `copy ^ $num2`

println $num * $num2 + 1 # output: 49
```

#### how it works?
we declare $name variable and put `'parsa'` string in that

next, in mem we maked a string and paste $name variable value to `'hello '` with a \n at the end of it, and we print that mem

you can use variables in mem like example above

###### NOTE: in above example, we used `copy` command like this:

```bash
mem 'some value'
copy $somevar
# that is alias of
copy ^ $somevar
```

if you give just one variable to copy command, the mem will be copy in that variable

look at this example:

```bash
set $var1 $var2

mem 'hi'; copy $var1
mem 'bye'; copy $var2 # this is alias of `copy ^ $var2`

out $var1 # output: hi
out $var2 # output: bye

copy $var1 $var2 # copy a variable in variable

out $var1 # output: hi
out $var2 # output: hi

```

### a better way to set variables value without using `mem` and `set` commands and with easier syntax

```bash
$name = 'parsa'
```

you just need to write name of variable with `$` and next assign value with `=` after this:

```bash
$name = 'parsa'

$num1 = 10
$num2 = 50

$sum = $num1 + $num2 # use variables in variables

println 'sum is ' + str($sum) # output: sum is 60

$msg = 'hello ' + $name
println $msg # output: hello parsa
```

also if you just write something like this:

```bash
$name # without `= <value>...`
out $name # output: None
```

variable will set and just get `None` as default value

### put `mem` value to variable

we can set value of mem to variables with this legacy way:

```bash
$myvar # set myvar
mem 'something' # load mem
copy $myvar # copy mem to variable
```

the better way is:

```bash
mem 'something'
$myvar = ^
```

if you put `^` (mem symbol) as value, memory value will put in the variable

### free variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
$somevar = 'some value'
out $somevar # output: some value

free $somevar

out $somevar # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
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

isset $somevar; out ^ # output: True
isset $this_var_not_found; out ^ # output: False
isset $somevar $sassadffgdty; out ^ # output: False
isset $somevar $v; out ^ # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exist, it will put `True` in  memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` command

look at this example:

```bash
$mystr = 'hi'
$myint = 20
$myfloat = 15.32
$mybool = False

typeof $mystr; out ^ # output: <class 'str'>
typeof $myint; out ^ # output: <class 'int'>
typeof $myfloat; out ^ # output: <class 'float'>
typeof $mybool; out ^ # output: <class 'bool'>
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
