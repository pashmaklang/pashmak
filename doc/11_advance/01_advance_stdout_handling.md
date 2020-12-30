# output handling magic functions
There is some magic functions in pashmak to handle program output dynamically.

For example, we want to write a program to run a function and return that thing that function is printed.

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

In the above example, we handled program stdout output in advance level.

List of `out_*` functions:

- `out_start`: says to pashmak that from here do not print directly and save printed values
- `out_end`: says to pashmak to end saving printed values and enable print from here
- `out_get`: returns printed values
- `out_clean`: clears the buffer of printed values
- `out_get_clean`: clears the buffer and returns printed values

Also this system is useful to disabling print:

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
