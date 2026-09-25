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

The `raise` function can raise errors in the program.

You should pass an object of the class `Error` as the argument for this.

To do this, you need to write `Error('TypeOfError', 'message of error')`. You will learn about classes in the next sections.
