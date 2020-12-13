# Importing scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a function to show fibonaccy algo.

###### fib.pashm:
```bash
# this function prints fibonacci pattern
func fib
    $a = 1
    $b = 1

    section loop;
        println $a

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

fib
```

when we run `import` function and pass a file path to that, content of that file will be included in our code and will be runed. for example, here we used a function from the `fib.pashm` file.

also you can import more than 1 scripts in one command:

```bash
# seprate them with `,` (actially a tuple or list)
import 'a.pashm', '/path/to/b.pashm', 'dir/c.pashm'
# or with () is not different
import('a.pashm', '/path/to/b.pashm', 'dir/c.pashm')
```
