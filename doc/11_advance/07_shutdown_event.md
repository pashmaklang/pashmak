# Shutdown event
A shutdown event lets you register functions to run when the program ends.

For example:

```bash
# this function runs when the program ends
func the_end
    println('The end')
endfunc

# register this function to shutdown event
register_shutdown(the_end)

println('hello')
println('world')
```

output:

```
hello
world
the end
```

In the example above, we used `register_shutdown` to register `the_end` as a shutdown event. It runs when the program ends.

You can also register more than one function:

```bash
func end1
    println('first end')
endfunc

func end2
    println('second end')
endfunc

register_shutdown(end1)
register_shutdown(end2)
```

output:

```
first end
second end
```
