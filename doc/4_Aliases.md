# Aliases
alias is a system to make alias for some codes.

look at this example:
```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

call say_hello;
```

output:

```
hello world
```

```bash
alias say_hello;
    mem 'hello world\n'; out ^;
endalias;

call say_hello;
call say_hello;
```

output:

```
hello world
hello world
```


you can declare a alias and call it from every where. when you call a alias, all of codes inside that alias will run

for declare a alias you have to write `alias <name-of-alias>`. and write codes. then for close alias write `endalias` after codes

look at this smarter alias:
```bash
mem 'program started\n'; out ^;

alias say_hello; required %say_hello_name; # declare alias and require variable %say_hello_name
    mem 'hello ' + %say_hello_name + '\n'; out ^;
    free %say_hello_name;
endalias;

set %say_hello_name; mem 'parsa'; copy %say_hello_name;
call say_hello;
```

program output:

```
program started
hello parsa
```
