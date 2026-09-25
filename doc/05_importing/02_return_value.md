# Script return value
Scripts can return some values (like functions).

For example, we have `foo.pashm`:

```bash
# ...

return 'hello world'
```

Now, if I import this file:

```bash
$output = import('foo.pashm')

println 'output: ' + $output
```

Output:

```
output: hello world
```

As you can see, the `import` function (or `import_once`, `import_run`...) will return the value returned
by the `return` command in the script. With this feature, we can return values from scripts, just like from functions.
