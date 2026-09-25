# OS Commands

Here are some commands related to the OS.

### cwd
Get the current working directory.

```bash
cwd()
println(^)
```

output:

```
/tmp
```

or:

```bash
$cwd = cwd()
println('The current working directory is ' + $cwd)
```

or:

```bash
println(cwd())
```

This command puts the current working directory path into the mem.

### system
You can run shell commands with this command:

```bash
system('ls /tmp')
```

Also after running the `system` function, the exit code will be put in the `mem`:

```bash
system('ls /')
println(^) # output: 0
```

or:

```bash
println(system('ls /'))
```

### exit
This command exits the program.

Look at this example:

```bash
println('first print')

exit()

println('last print') # this will not print
```

output:

```
first print
```

#### exit with exit code:

```bash
println('hello world')
exit(1)
```

The exit code of the program will be `1`.
