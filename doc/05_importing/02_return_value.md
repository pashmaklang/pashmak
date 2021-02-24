# Script return value
Scripts can return some values (like functions).

For example, we have `foo.pashm`:

```bash
# ...

return 'hello world'
```

Now, if i import this file:

```bash
$output = import('foo.pashm')

println 'output: ' + $output
```

Output:

```
output: hello world
```

As you can see, function `import` (or `import_once`, `import_run`...) will return the returned value
by command `return` in the script. By this feature, we can return values by scripts like functions.
