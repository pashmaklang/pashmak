# Include scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a function to show fibonaccy algo.

###### fib.pashm:
```bash
func fib;
    set $a $b;
    mem 1; copy $a;
    mem 1; copy $b;

    section 10;
        print str($b) + '\n';

        set $tmp_a $tmp_b;
        copy $a $tmp_a;
        copy $b $tmp_b;

        copy $tmp_b $a;

        mem $tmp_a + $tmp_b; copy $b;
    mem $b < 10000; gotoif 10;
endfunc;
```

###### app.pashm:
```bash
mem 'fib.pashm'; include ^;

fib;
```

when we run `include` command and pass a file path from mem (^) or variable to that, content of thet file will include in our code and will run. for example, here we used a function from the `fib.pashm` file.

also you can use `import` function to have easier syntax:

```bash
# you can pass value directly to this
import 'fib.pashm';

fib;
```

this is very useful.
