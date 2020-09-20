# Try and Endtry statement

we may recive some errors in our program. for example:

```bash
out $this_var_not_found;
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined operation
outttt ^;
```

output:

```
SyntaxError:
        undefined operation "outttt"
```

they are errors

##### but how to handle errors?

we can handle errors with `try-endtry` statement.

look at this example:

```bash
try handle_error;
    out $somevar;
endtry;

goto after_error;

section handle_error;

mem 'some errors raised\n'; out ^;

section after_error;
```

when you write code between `try <section-name> ... endtry`, errors will not raised in them and if an error is raised, that section where passed to try operation will run.

this is helpful.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error;
    out $somevar;
endtry;

goto after_error;

section handle_error;

set $ex; copy $ex; # copy mem (^) to $ex variable (this includes information about raised error)
out $ex; # output: {"type": "VariableError" , "message": "undefined variable $somevar"}...

section after_error;
```
