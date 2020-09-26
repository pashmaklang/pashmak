# General Modules
pashmak has some general libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `include` operation.

look at this example:

```bash
mem '@hash'; include ^;
mem '@time'; include ^;
mem '@module_name'; include ^;

# or using stdlib
import '@hash';

# ...
```

you have to give name of module with a `@` before that to the include operation.

### hash module
with hash module, you can calculate hash sum of values:

```bash
mem '@hash'; include ^;

hash.sha256 "hello"; # also you can use hash.md5 and...
out ^; # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

###### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this alias calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

also you can use `hash.md5` aliases and...

### time module
with this module, you can work with time.

###### time.time
this alias gives you current UNIX timestamp:

```bash
mem '@time'; include ^;

time.time; # this is shorter of `call time.time`
out ^; # output is some thing like this: `1600416438.687201`
```

when you call this alias, this alias puts the unix timestamp into mem and you can access and use that.

###### time.sleep
this alias sleeps for secounds:

```bash
mem '@time'; include ^;

time.sleep 2; # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this alias, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` alias, then program will sleep for value of `mem` as secounds

## random module
this module makes random numbers

###### random.randint
```bash
mem '@random'; include ^;

random.randint [1, 10]; # generates a random int between 1 and 10

out ^; # and puts generated random number in mem and you can access that
```

###### random.random
```bash
mem '@random'; include ^;

random.random; # generates a random float less that 1

out ^; # and puts generated random number in mem and you can access that
```

###### more modules comming soon...
