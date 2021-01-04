# function `printf()`
This function prints on a specify FILE.

By default, this works like normal `print` function. for example:

```bash
printf('hello world\n')
```

output:

```
hello world
```

But you can pass a Second argument as file. for example:

```bash
$file = open('/path/to/file.txt', 'a') # append mode

printf('hello', $file)
```

Now, string `hello` is appended to content of the file.

