# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
mem '/tmp'; chdir ^

# or

$path = '/tmp'
chdir $path # use variable
```

also you can use `std_chdir` function:

```bash
# in this function you can pass path directly and not need to set path in mem before it
std_chdir '/tmp'
# or
std_chdir $path
# or
std_chdir $path + '/path'
```

### cwd
get current working directory.

```bash
cwd
out ^
```

output:

```
/tmp
```

or:

```bash
cwd
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
mem 'ls /tmp'; system ^

# or

$cmd = 'ls /tmp'
system $cmd # use variable
```

also you can use `sys` function to have easier function:

```bash
sys 'ls /tmp'
# or
sys $cmd
```

you can pass value directly to `sys`

also after run `system` or `sys`, command exit code will put in `mem`:

```bash
sys 'ls /'
out ^ # output: 0
```

### return
this command exits program

look at this example:

```bash
mem 'first print\n'; out ^

return

mem 'last print\n'; out ^ # this will not print
```

output:

```
first print
```

###### return with exit code:

```bash
mem 'hello world\n'; out ^
return 1
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
