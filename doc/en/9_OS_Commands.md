# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
chdir '/tmp'
```

### cwd
get current working directory.

```bash
cwd
println ^
```

output:

```
/tmp
```

or:

```bash
cwd # or `cwd()`
$cwd = ^
println $cwd
```

or:

```bash
$cwd = ^ cwd
println $cwd
```

this command puts current working directory path in mem

### system
you can run shell commands by this command:

```bash
system 'ls /tmp'
```

also after run `system` function, exit code will put in `mem`:

```bash
system 'ls /'
println ^ # output: 0
```

### exit
this command exits program

look at this example:

```bash
println 'first print\n'

exit

println 'last print\n' # this will not print
```

output:

```
first print
```

###### exit with exit code:

```bash
println 'hello world\n'
exit 1
```

exit code of program will be `1`

or you can use `exit` command:

```bash
exit # with 0 default exit code
exit 10 # with 10
```

### `$__file__` and `$__dir__` variables
`$__file__` and `$__dir__` variables are two variables contains self script filepath and dirpath.

for example, if you run an script in `/home/parsa/myscript.pashm` with this content:

```bash
println $__file__
println $__dir__
```

output is:

```
/home/parsa/myscript.pashm
/home/parsa
```

The `$__file__` variable contains filepath of current running script.

The `$__dir__` variable contains dirpath of current running script.
