# Output handling magic functions
Pashmak provides magic functions for handling program output dynamically.

For example, suppose we want a program to run a function and capture the text it prints.

Look at this example:

```bash
func do_something
    print('this is something')
endfunc

println('program starts')

out_start()

do_something()

out_end()

$what_function_printed = out_get()

println('function printed "' + $what_function_printed + '"')

println('program ends')
```

output:

```
program starts
function printed "this is something"
program ends
```

In the example above, we handled the program's standard output.

List of `out_*` functions:

- `out_start`: stops printing directly and begins saving printed values
- `out_end`: stops saving printed values and resumes printing directly
- `out_get`: returns the saved printed values
- `out_clean`: clears the buffer of printed values
- `out_get_clean`: clears the buffer and returns the printed values

This system is also useful for suppressing output:

```bash
println('start')

out_start()

println('This will not be printed')

out_clean()
out_end()

println('end')
```

output:

```
start
end
```
