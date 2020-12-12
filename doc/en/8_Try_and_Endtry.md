# Try and Endtry statement

we may recive some errors in our program. for example:

```bash
println $this_var_not_found
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined operation
printlgdfgfd ^
```

output:

```
SyntaxError:
        undefined operation "printlgdfgfd"
```

they are errors.

##### but how to handle errors?

we can handle errors with `try-endtry` statement.

look at this example:

```bash
try handle_error
    println $somevar
endtry

goto after_error

section handle_error

mem 'some errors raised\n'; out ^

section after_error
```

when you write code between `try <section-name> ... endtry`, errors will not raised in them and if an error is raised, that section where passed to try operation will run.
actually, we say to the Pashmak to don't show error to user and do that thing I'm saying you instead of default error showing.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error
    println $somevar
endtry

goto after_error

section handle_error

$ex = ^ # copy mem (^) to $ex variable (this includes information about raised error)
println $ex # output: {"type": "VariableError", "message": "undefined variable $somevar"}...

section after_error
```

#### raising errors
Your self can raise errors in the program.

for example:

```bash
println 'program started'

raise 'MyError', 'this is my error'
# or
raise('MyError', 'this is my error')

println 'this will not print'
```

output:

```
progrma started
MyError: this is my error
```

The `raise` function can raise errors in program.

first argument `'TheError'` is error type and second error `'this is my error'` is error message.
