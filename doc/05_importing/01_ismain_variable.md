# `$__ismain__` variable
The `$__ismain__` variable, is a general Boolean variable. This variable is used to check the current file, is the **Main ran file** or not.

For example, we have two files, `my_program.pashm` and `lib.pashm`. We want to know that in our scripts **Is the current script main directly ran file?**.

When you run in terminal:

```bash
pashmak my_program.pashm
```

the `my_program.pashm` file is ran directly.

#### my_program.pashm:

```bash
println($__ismain__)

import('lib.pashm')
```

The above code, prints value of this variable and also imports `lib.pashm` file.

#### lib.pashm:

```bash
println($__ismain__)
```

When I run `my_program.pashm`, output is this:

```
True
False
```

Actually, value of this variable in `my_program.pashm` is `True`, but in `lib.pashm` is `False`.

Now, when I run `pashmak lib.pashm`, output is `True`.

**The `$__ismain__` variable says that the current file is main ran file or not and you can check this**.

For example, if we want to run a code only if our script is directly ran and is not imported from other script:

```bash
if $__ismain__
    # do something
endif
```

### `import_run` and `import_run_once` functions
Now, you understand the `$__ismain__` variable, But sometimes you need to run a file with `True` value for `$__ismain__`! This is too easy, you should use `import_run` instead of `import` and `import_run_once` instead of `import_once`.

For example, in `main.pashm`:

```bash
println('i am main program')
import $__dir__ + '/other.pashm'
import_run $__dir__ + '/other.pashm'
```

content of `other.pashm`:

```bash
println($__ismain__)
```

output of `main.pashm`:

```
False
True
```

Why? Because in second import we used `import_run` instead of `import`, so, value of `$__ismain__` is `True`.
