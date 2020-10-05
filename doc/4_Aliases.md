# Aliases
alias is a system to make alias for some codes (function).

look at this example:
```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

say_hello;
```

output:

```
hello world
```

```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

say_hello;
say_hello;
```

output:

```
hello world
hello world
```


you can declare a alias and call it from everywhere. when you call a alias, all of codes inside that alias will run

for declare a alias you have to write `alias <name-of-alias>`. and write codes. then for close alias write `endalias` after codes

look at this smarter alias:
```bash
mem 'program started\n'; out ^;

alias say_hello;
    set $name; copy $name
    mem 'hello ' + $name + '\n'; out ^;
    free $name;
endalias;

mem 'parsa'; say_hello;
```

program output:

```
program started
hello parsa
```

### passing argument to aliases
for pass argument to the aliases, you can put value after name of alias:

```bash
alias myalias;
    out ^;
endalias;

myalias "hello";
```

output:

```
hello
```

##### how it works?
you can put a value after name of alias. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
alias say_hello;
    set $say_hello_name_tmp; copy ^ $say_hello_name_tmp;
    mem 'hello ' + $say_hello_name_tmp + '\n'; out ^;
endalias;

say_hello 'parsa';
```

output:

```
hello parsa
```


### local variables & global variables

look at this example:

```bash
alias myalias;
    mem 'new name'; copy $name;
    mem $name + '\n'; out ^;
endalias;

set $name; mem 'parsa'; copy $name;
mem $name + '\n'; out ^;

myalias;

mem $name + '\n'; out ^;
```

output:

```
parsa
new name
parsa
```

there is a note. why when we changed `$name` variable in `myalias` alias, this was the old value after alias?

the `$name` where was set in `myalias`, is local. means that do not points to global `$name` in out program.

the seted variables in aliases, are local. also aliases cannot change global variables

the variable environment in aliases are isolated.

so, how to change a global variable from a alias?

the answer is in `gset`:

```bash
alias myalias;
    set $name; mem 'new name'; copy $name;
    gset ['name' , $name];
    mem $name + '\n'; out ^;
endalias;

set $name; mem 'parsa'; copy $name;
mem $name + '\n'; out ^;

myalias;

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
