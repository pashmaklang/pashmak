## Variables

variables are like a put where you can save a data on them

to set and handle variables in pashmak, we work with three commands: `set`, `copy`, `free`

```bash
set %myvar; # set a variables named %myvar
mem 'this is data'; # bring string 'this is data' to mem
copy ^ %myvar; # copy mem (^) to %myvar

out %myvar; # output: this is data
```

###### NOTE: always put % before name of variable every where

also you can set more than one variables with `set` command:

```bash
set %var1 %var2 %var3;
```

### use variables in mem

look at this example:

```bash
set %name; # set name variable
mem 'parsa'; copy ^ %name; # copy 'parsa' string to name variable

mem 'hello ' + %name + '\n'; out ^; # output: hello parsa

set %num; mem 12; copy ^ %num;
mem %num*5; out ^; # output: 60

set %num2; mem 4; copy ^ %num2;

mem %num * %num2 + 1; out ^; # output: 49
```

#### how it works?
we declared a %name variable and put `'parsa'` string in that

next, in mem we maked a string and paste %name variable value to `'hello '` with a \n in end of that, and we printed that mem

you can use variables in mem like that example


### free variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
set %somevar;
mem 'some value'; copy %somevar;

out %somevar; # output: some value

free %somevar;

out %somevar; # you will get VariableError: undefined variable %somevar (because it is deleted by free command)
```

also you can free more than one variable with `free` command:

```bash
free %var1 %var2 %var3; # ...
```

###### NOTE: in that example, we used `copy` command like this:

```bash
mem 'some value';
copy %somevar;
# that is alias of
copy ^ %somevar;
```

when you give just a variable to copy command, the mem will be copy in that variable

look at this example:

```bash
set %var1 %var2;

mem 'hi'; copy %var1;
mem 'bye'; copy %var2; # this is alias of `copy ^ %var2`

out %var1; # output: hi
out %var2; # output: bye

copy %var1 %var2; # copy a variable in variable

out %var1; # output: hi
out %var2; # output: hi

```

### checking a variable isset
you can check a variable exists with `isset` command

look at this example:

```bash
set %somevar %v;

isset %somevar; out ^; # output: True
isset %this_var_not_found; out ^; # output: False
isset %somevar %sassadffgdty; out ^; # output: False
isset %somevar %v; out ^; # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exists, put `True` in  memory and if all or one/more of them are not exists, put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` command

look at this example:

```bash
set %mystr %myint %myfloat %mybool;

mem 'hi'; copy %mystr;
mem 20; copy %myint;
mem 15.32; copy %myfloat;
mem False; copy %mybool;

typeof %mystr; out ^;   # output: str
typeof %myint; out ^;   # output: int
typeof %myfloat; out ^; # output: float
typeof %mybool; out ^;  # output: bool
```

this command puts the typeof variable in mem


### required command

the required command requiring an variable existing.

look at this example:

```bash
set %name;

required %name;
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#set %name;
required %name;
```

now name variable is not set, and you will get this error:

```
RequireError:
    undefined variable %name
```

the required command checks a variable is exists, if no, raising RequireError

you will know why this command is usable in the aliases section
