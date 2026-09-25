# Putting functions into variables
Functions are like variables; you can put them into variables and use them.

Look at this example:

```bash
func hello($name)
    println('hello ' + $name)
endfunc

hello('parsa')

# putting the function into the variable
$myfunc = hello

# calling the variable
$myfunc('pashmak')
```

output:

```
hello parsa
hello pashmak
```

Another example:

```bash
func somefunc()
    println('hello. I have been run')
endfunc

$myfunc = somefunc
$myfunc()
```


Also look at this example:

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

Also you can change the value of functions. Functions are like variables and can be changed.

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

Now we can change the value of these functions:

```bash
hi = bye
hi()
```

output:

```
Bye
```

Actually, in the above example, we are setting `bye` into `hi`.
