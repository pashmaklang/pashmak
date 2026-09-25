# function `printf()`
This function prints to a specified file.

By default, it works like the regular `print` function. For example:

```bash
printf('hello world\n')
```

output:

```
hello world
```

You can also pass a file as the second argument. For example:

```bash
$file = open('/path/to/file.txt', 'a') # append mode

printf('hello', $file)
```

The string `hello` is appended to the file's contents.
