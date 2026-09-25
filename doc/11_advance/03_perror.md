# perror()
There is a difference between normal output (printed to STDOUT) and error output (printed to STDERR). The `print` and `println` functions write to STDOUT. Use `perror` to write to STDERR; it works like `print`.

For example:

```bash
perror('hello world. this is a error and is printed on STDERR')
```
