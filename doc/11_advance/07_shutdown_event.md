# Shutdown event
Shutdown event is a system to set some functions to be ran in end of program.

For example:

```bash
# this function will be ran in the end of program
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

In the above example, we used `register_shutdown` function to set function `the_end` as shutdown event. this function will be ran in the end of program.

Also you can set more than 1 function:

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
