# Importing scripts
You can distribute your code across more than 1 file.

For example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is the main file. `fib.pashm` contains a function to show the fibonacci algorithm.

#### fib.pashm:
```bash
# this function prints the fibonacci pattern
func fib
    $a = 1
    $b = 1

    while $a < 10000
        println($a)

        $tmp_a = $a
        $tmp_b = $b

        $a = $tmp_b

        $b = $tmp_a + $tmp_b
    endwhile
endfunc
```

#### app.pashm:
```bash
import 'fib.pashm'

fib()
```

When we run the `import` function and pass a file path to it, the content of that file will be included in our code and will be run. For example, here we used a function from the `fib.pashm` file.

Also you can import more than 1 script in one command:

```bash
# Separate them with `,` (actually a tuple or list)
import('a.pashm', '/path/to/b.pashm', 'dir/c.pashm')
```

### import_once function
There is a command named `import_once`. This is exactly like the `import` function, but this function does not import the same script more than once.

For example, we have a file named `foo.pashm`:

#### foo.pashm:

```bash
$a = 100
```

Now, we import this file two times:

```bash
import('foo.pashm')
println($a)
$a = 300
import('foo.pashm')
println($a)
```

output:

```
100
100
```

Because I imported this script two times and my code sets `$a` two times.

But if I use the `import_once` function:

```bash
import_once('foo.pashm')
println($a)
$a = 300
import_once('foo.pashm')
println($a)
```

output:

```
100
300
```

Because the `import_once` function checks the file, and if the file is already imported, it does not import it again.

### Importing a directory
You can import directories; the directory should have an `__init__.pashm` file.

For example:

```bash
import '/path/to/some/dir' # means import `/path/to/some/dir/__init__.pashm`
```

When you import a directory, the `__init__.pashm` file in that directory will be imported.
