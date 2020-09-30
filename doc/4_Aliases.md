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
    set $say_hello_name; copy $say_hello_name
    mem 'hello ' + $say_hello_name + '\n'; out ^;
    free $say_hello_name;
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
