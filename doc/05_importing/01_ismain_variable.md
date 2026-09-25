# `$__ismain__` variable
The `$__ismain__` variable is a general boolean variable. This variable is used to check whether the current file is the **main run file** or not.

For example, we have two files, `my_program.pashm` and `lib.pashm`. We want to know in our scripts **whether the current script is the main, directly run file**.

When you run in terminal:

```bash
pashmak my_program.pashm
```

the `my_program.pashm` file is run directly.

#### my_program.pashm:

```bash
println($__ismain__)

import('lib.pashm')
```

The above code prints the value of this variable and also imports the `lib.pashm` file.

#### lib.pashm:

```bash
println($__ismain__)
```

When I run `my_program.pashm`, the output is this:

```
True
False
```

Actually, the value of this variable in `my_program.pashm` is `True`, but in `lib.pashm` it is `False`.

Now, when I run `pashmak lib.pashm`, the output is `True`.

**The `$__ismain__` variable tells you whether the current file is the main run file or not, and you can check this**.

For example, if we want to run code only if our script is run directly and is not imported from another script:

```bash
if $__ismain__
    # do something
endif
```

### `import_run` and `import_run_once` functions
Now you understand the `$__ismain__` variable, but sometimes you need to run a file with a `True` value for `$__ismain__`! This is very easy: you should use `import_run` instead of `import` and `import_run_once` instead of `import_once`.

For example, in `main.pashm`:

```bash
println('I am the main program')
import $__dir__ + '/other.pashm'
import_run $__dir__ + '/other.pashm'
```

The content of `other.pashm`:

```bash
println($__ismain__)
```

The output of `main.pashm`:

```
False
True
```

Why? Because in the second import we used `import_run` instead of `import`, so the value of `$__ismain__` is `True`.
