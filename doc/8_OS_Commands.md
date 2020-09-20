# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
mem '/tmp'; chdir ^;

# or

set $path; mem '/tmp'; copy $path;
chdir $path; # use variable
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

set $cmd; mem 'ls /tmp'; copy $cmd;
system $cmd; # use variable
```

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
