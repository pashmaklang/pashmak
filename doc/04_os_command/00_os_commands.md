# OS Commands

Here are some commands about OS.

### cwd
Get current working directory.

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

This command puts current working directory path into the mem.

### system
You can run shell commands by this command:

```bash
system('ls /tmp')
```

Also after run `system` function, exit code will put in `mem`:

```bash
system('ls /')
println(^) # output: 0
```

or:

```bash
println(system('ls /'))
```

### exit
This command exits program

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

Exit code of program will be `1`
