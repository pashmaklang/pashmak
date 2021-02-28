# Hiding Errors
You can hide the error renders in the Pashmak.
For doing this, you only need to define `HIDE_ERRORS`.
([read name defining system](doc/11_advance/11_name_defines.md)).

For example:

```bash
println $not_found
```

Error output:

```
VariableError: undefined variable "not_found":
  in <stdin>:1:
        println $not_found
```

But if you change your code to this:

```bash
# hide the errors
define('HIDE_ERRORS', true)

println $not_found
```

The above code has not output.

You only need to set `HIDE_ERRORS` to `true`
