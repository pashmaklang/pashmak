# Raising errors
You yourself can raise errors in the program.

For example:

```bash
println('program started')

raise(Error('MyError', 'this is my error'))

println('this will not print')
```

output:

```
program started
MyError: this is my error
```

The `raise` function can raise errors in program.

You should pass a object from class `Error` as argument for this.

To do this, you need to write `Error('TypeOfError', 'message of error')`. You will learn about classes in next sections.
