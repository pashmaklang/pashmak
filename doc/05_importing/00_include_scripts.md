# Importing scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a function to show fibonaccy algo.

##### fib.pashm:
```bash
# this function prints fibonacci pattern
func fib
    $a = 1
    $b = 1

    section loop;
        println($a)

        $tmp_a = $a
        $tmp_b = $b

        $a = $tmp_b

        $b = $tmp_a + $tmp_b
    mem $a < 10000; gotoif loop
endfunc
```

###### app.pashm:
```bash
import 'fib.pashm'

fib()
```

when we run `import` function and pass a file path to that, content of that file will be included in our code and will be runed. for example, here we used a function from the `fib.pashm` file.

also you can import more than 1 scripts in one command:

```bash
# seprate them with `,` (actially a tuple or list)
import('a.pashm', '/path/to/b.pashm', 'dir/c.pashm')
```

### import_once function
there is a command named `import_once`. this is excatly like `import` function, but this function do not repeats for import one script.

for example, we have a file named `foo.pashm`:

##### foo.pashm:

```bash
func hello
    println('hello')
endfunc
```

now, we import this file Two times:

```bash
import('foo.pashm')
import('foo.pashm')
```

we will get this error:

```
FunctionError: function "hello" already declared...
```

because i imported this script two times and my code tryied to declare function `hello` two times, so, we get the error.

but if i use the `import_once` function:

```bash
import_once('foo.pashm')
import_once('foo.pashm')
```

the above code will be runed successfully.

because, `import_once` function checks the file, and if files already imported, don't imports again.

### `$__ismain__` variable
the `$__ismain__` variable, is a general Boolean variable. this variable is used to check the current file, is the **Main runed file** or not.

for example, we have two files, `my_program.pashm` and `lib.pashm`. we want to know that in our scripts **Is the current script main directly runed file?**.

when you run in terminal:

```bash
pashmak my_program.pashm
```

the `my_program.pashm` file is runed directly.

##### my_program.pashm:

```bash
println($__ismain__)

import('lib.pashm')
```

the above code, prints value of this variable and also imports `lib.pashm` file.

##### lib.pashm:

```bash
println($__ismain__)
```

when i run `my_program.pashm`, output is this:

```
True
False
```

actually, value of this variable in `my_program.pashm` is `True`, but in `lib.pashm` is `False`.

now, when i run `pashmak lib.pashm`, output is `True`.

**The `$__ismain__` variable says that the current file is main runed file or not and you can check this**.

for example, if we want to run a code only if our script is directly runed and is not imported from other script:

```bash
if $__ismain__
    # do something
endif
```
