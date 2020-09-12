# Try and Endtry statement

we may get some errors in some places in program. for example:

```bash
out %this_var_not_found;
```

output:

```
VariableError:
    undefined variable %this_var_not_found
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
    out %somevar;
endtry;

goto after_error;

section handle_error;

mem 'some errors raised\n'; out ^;

section after_error;
```

when you write code between `try <section-name> ... endtry`, if there is some errors, error will not raised and the section passed to try command will run.

this is helpful.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error;
    out %somevar;
endtry;

goto after_error;

section handle_error;

set %ex; copy %ex;
out %ex; # output: {"type": "VariableError" , "message": "undefined variable %somevar"}...

section after_error;
```
