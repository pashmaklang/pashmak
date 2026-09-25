# The Pashmak compiler (mixer)
This program compiles or mixes Pashmak scripts.

It can combine many scripts in your project into one file.

If your project has many files that import one another, this tool can combine them into a single file.

## Get started
Let's get started:

```bash
$ pashmak @compiler /path/to/my-program/main.pashm out.pashm
```

Then you can run `out.pashm`:

```bash
$ pashmak out.pashm
```

Consider an example with three files: `app.pashm`, `lib.pashm`, and `core.pashm`.

##### `app.pashm`:

```bash
println('App: start')

import $__dir__ + '/core.pashm'

println('App: end')
```

##### `core.pashm`:

```bash
println('Core: start')

import $__dir__ + '/lib.pashm'

println('Core: end')
```


##### `lib.pashm`:

```bash
println('Lib: hello')
```

When I run `app.pashm` normally, the output is:

```
App: start
Core: start
Lib: hello
Core: end
App: end
```

Now I can mix these three files into one file:

```bash
$ pashmak @compiler app.pashm out.pashm
```

When I run the generated `out.pashm`, the output is:

```
App: start
Core: start
Lib: hello
Core: end
App: end
```

This is exactly the same as the output from a normal run.

This helps you build your project from many files into one file.
