## Function super functions
there is some **Super functions** to handle functions at runtime.

#### Checking function exists
You can check a function exists with `func.exists` function:

```bash
if func.exists('some_func')
    some_func()
endif
```

#### Geting list of all of functions
You can get list of all of functions with `func.list` function:

```bash
$funcs = func.list()

println($funcs)
```

output:

```
['a', 'b', '...']
```

The output is a list.

#### Deleting a function
You can delete a function at runtime with `func.delete` function:

```bash
func.delete('some_func')
```

### Complicated function declaration
You can declare functions-in-functions.

Look at this example:

```bash
func foo
    func bar
        println('bar')
    endfunc

    bar()

    println('foo')
endfunc

foo()
bar()
```

output:

```
bar
foo
bar
```

Also look at this example:

```bash
func first
    println('first start')
    func second
        println('second start')
        func last
            println('last')
        endfunc
        last()
        println('second end')
    endfunc
    second()
    println('first end')
endfunc

first()
```

output:

```
first start
second start
last
second end
first end
```

**The declared function in function is accessible from outside.**

For example:

```bash
func foo
    func bar
        println('the bar')
    endfunc
endfunc

foo()

bar()
```

**How to make a function in function local?**

You should delete the function in end of parent function:

```bash
func foo
    func bar
        println('the bar')
    endfunc

    # use the function...

    func.delete(__namespace__() + 'bar')
endfunc

foo()

bar()
```

output:

```
NameError: undefined 'bar'...
```

> You will learn about that `__namespace__()` function in next sections...
