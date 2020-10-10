# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
mem '/tmp'; chdir ^;

# or

$path = '/tmp';
chdir $path; # use variable
```

also you can use `std.chdir` function:

```bash
# in this function you can pass path directly and not need to set path in mem before it
std.chdir '/tmp';
# or
std.chdir $path;
# or
std.chdir $path + '/path';
```

### cwd
get current working directory.

```bash
cwd;
out ^;
```

output:

```
/tmp
```

this command puts current working directory path in mem

### system
you can run shell commands by this command:

```bash
mem 'ls /tmp'; system ^;

# or

$cmd = 'ls /tmp';
system $cmd; # use variable
```

also you can use `sys` function to have easier function:

```bash
sys 'ls /tmp';
# or
sys $cmd;
```

you can pass value directly to `sys`

### return
this command exits program

look at this example:

```bash
mem 'first print\n'; out ^;

return;

mem 'last print\n'; out ^; # this will not print
```

output:

```
first print
```

###### return with exit code:

```bash
mem 'hello world\n'; out ^;
return 1;
```

exit code of program will be `1`

or you can use `exit` command:

```bash
exit; # with 0 default exit code
exit 10; # with 10
```
