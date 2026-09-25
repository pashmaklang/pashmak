# Try and Endtry statement

We may receive some errors in our program. For example:

```bash
println($this_var_not_found)
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined function
printlgdfgfd(^)
```

output:

```
NameError: undefined "printlgdfgfd"
```

They are errors.

### But how to handle errors?

We can handle errors with the `try-endtry` statement.

Look at this example:

```bash
try handle_error
    println($somevar)
endtry

goto after_error

label handle_error

println('some errors raised')

label after_error
```

When you write code between `try <label-name> ... endtry`, errors will not be raised in it, and if an error is raised, the label that was passed to the try command will run.
Actually, we are telling Pashmak not to show the error to the user and to do what we say instead of the default error output.

Note: You can use the keyword `end` instead of `endtry`. There is no difference.

### How to access the raised error data?

When an error is raised in a try statement, the error data will be put in the mem (^):

```bash
try handle_error
    println($somevar)
endtry

goto after_error

label handle_error

$ex = ^ # copy the mem (^) to the $ex variable (this includes information about the raised error)
println($ex) # output: VariableError: undefined variable $somevar

label after_error
```

The raised error data has more properties. This is a [Class object](#classes). You will learn about classes in the next sections.

```bash
try error
    gfgdhf
endtry

label error

$ex = ^ # raised error
println($ex->type) # output: VariableError
println($ex->message) # output: undefined variable $not_found
println($ex->file_path) # output: /path/to/script.pashm
println($ex->line_number) # output: 2
```
