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

We can handle errors with `try-endtry` statement.

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

When you write code between `try <label-name> ... endtry`, errors will not raised in them and if an error is raised, that label where passed to try command will run.
Actually, we say to the Pashmak to don't show error to user and do that thing I'm saying you instead of default error showing.

Note: You can use keyword `end` instead of `endtry`. It is not different.

### How to access raised error data?

When error is raised in try statement, error data will put in mem (^):

```bash
try handle_error
    println($somevar)
endtry

goto after_error

label handle_error

$ex = ^ # copy mem (^) to $ex variable (this includes information about raised error)
println($ex) # output: VariableError: undefined variable $somevar

label after_error
```

The raised error data has more properties. This is a [Class object](#classes). You will learn about classes in next sections.

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
