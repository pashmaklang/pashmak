# Functions
function is a system to make alias for some codes (function).

look at this example:
```bash
func say_hello;
    mem 'hello world\n'; out ^;
endfunc;

say_hello;
```

output:

```
hello world
```

```bash
func say_hello;
    mem 'hello world\n'; out ^;
endfunc;

say_hello;
say_hello;
```

output:

```
hello world
hello world
```


you can declare a function and call it from everywhere. when you call a function, all of codes inside that function will run

for declare a function you have to write `func <name-of-function>;`. and write codes. then for close function write `endfunc;` after codes

look at this smarter function:
```bash
mem 'program started\n'; out ^;

func say_hello;
    set $name; copy $name
    mem 'hello ' + $name + '\n'; out ^;
    free $name;
endfunc;

mem 'parsa'; say_hello;
```

program output:

```
program started
hello parsa
```

### passing argument to Functions
for pass argument to the Functions, you can put value after name of function:

```bash
func myfunc;
    out ^;
endfunc;

myfunc "hello";
```

output:

```
hello
```

##### how it works?
you can put a value after name of function. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
func say_hello;
    set $name; copy ^ $name;
    mem 'hello ' + $name + '\n'; out ^;
endfunc;

say_hello 'parsa';
```

output:

```
hello parsa
```


### local variables & global variables

look at this example:

```bash
func myfunc;
    mem 'new name'; copy $name;
    mem $name + '\n'; out ^;
endfunc;

set $name; mem 'parsa'; copy $name;
mem $name + '\n'; out ^;

myfunc;

mem $name + '\n'; out ^;
```

output:

```
parsa
new name
parsa
```

there is a note. why when we changed `$name` variable in `myfunc` function, this was the old value after function?

the `$name` where was set in `myfunc`, is local. means that do not points to global `$name` in out program.

the seted variables in Functions, are local. also Functions cannot change global variables

the variable environment in Functions are isolated.

so, how to change a global variable from a function?

the answer is in `gset`:

```bash
func myfunc;
    set $name; mem 'new name'; copy $name;
    gset 'name' , $name;
    mem $name + '\n'; out ^;
endfunc;

set $name; mem 'parsa'; copy $name;
mem $name + '\n'; out ^;

myfunc;

mem $name + '\n'; out ^;
```

output:

```
parsa
new name
new name
```

here, `gset` command (from stdlib) gets two parameters: first, global variable name and second, new value for that

this command sets value of that variable globaly.

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)
