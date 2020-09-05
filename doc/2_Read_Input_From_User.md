# Read Input From User

you can read a input from user in stdin

look at this example:

```bash
set %name; # set the name variabl
mem 'what is your name? '; out ^; # print
read %name; # read a input and copy this in %name variable
mem 'hello ' + %name + '\n'; out ^; # say hello to %name :)
```

when we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for a input, and when you type some thing and press enter, program says `hello <your-input>`

for example in here i entered `parsa` as input and program says `hello parsa`

we can get input from user like this example


also look at this example:

```bash
set %num1 %num2;

mem 'enter first number: '; out ^;
read %num1;

mem 'enter second number: '; out ^;
read %num2;

# now, %num1 and %num2 are string. we convert string to int:
mem int(%num1); copy %num1;
mem int(%num2); copy %num2;

# now we want to plus them
set %sum;
mem %num1 + %num2; copy %sum;

mem str(%sum) + '\n'; out ^;
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two number from user and shows sum of them
