## Puting functions into variables
Functions are like variables, you can put them into variables and use them.

look at this example:

```bash
func hello($name)
    println('hello ' + $name)
endfunc

hello('parsa')

# puting the function into the variable
$myfunc = hello

# calling the variable
$myfunc('pashmak')
```

output:

```
hello parsa
hello pashmak
```

another example:

```bash
func somefunc()
    println('hello. I was runed')
endfunc

$myfunc = somefunc
$myfunc()
```


also look at this example:

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

Also you can change value of functions. functions are like variables and can be changed.

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

Now We can change value of this functions:

```bash
hi = bye
hi()
```

output:

```
Bye
```

Actually, in above example, We are setting `bye` into `hi`.
