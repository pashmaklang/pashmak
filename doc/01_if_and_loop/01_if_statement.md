# If elif else statement
in the previous part, you learned how to use **labels** for creating **Conditions** and **Loops**.
but there is a easy way to create **Conditions**, that is **If..elif..else** statement. this system is very easy for creating conditions and handling program flow.

example:

```bash
if 2 == 2
    println('yes, 2 is 2')
endif
```

or:

```bash
if 3 == 7
    println('3 is 7')
else
    println('3 is NOT 7')
endif
```

in this part, we learn how to use this system.

The if syntax is this:

```bash
if <condition>
    # code
endif
```

for example:

```bash
$age = 30

if $age > 18
    println('Welcome!')
endif
```

output:

```
Welcome!
```

```bash
$age = 12

if $age > 18
    println('Welcome!')
endif

# above code haven't output
```

Also you can use keyword `end` instead of `endif`:

```bash
$age = 12

if $age > 18
    println('Welcome!')
end
```

also you can use `else`:

```bash
$age = 12

if $age > 18
    println('Welcome!')
else
    println('you cannot access')
endif
```

if condition of `if` is not true, `else` block will be ran.

also there is other keyword `elif`:

```bash
$num = 17

if $num == 5
    println('num is 5')
elif $num == 6
    println('num is 6')
elif $num == 17
    println('num is 17')
else
    println('nothing')
endif
```

output:

```
num is 17
```

actually, `elif` block will be checked one by one. `elif` means `else if`.

## If in If
you can write ifs in ifs.

look at this example:

```bash
$num = 15
$test = True

if $num == 18
    pass
elif $num == 15
    println('num is 15')

    # another if in the parent if
    if $test
        println('this is a test')
    else
        println('this is not test')
    endif
endif
```

output:

```
num is 15
this is a test
```
