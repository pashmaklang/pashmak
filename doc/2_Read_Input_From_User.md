## Read Input From User

you can read input from user in stdin

look at this example:

```bash
set $name; # set the name variable
mem 'what is your name? '; out ^; # print
read $name; # read a input and copy that in $name variable
print 'hello ' + $name + '\n'; # say hello to $name :)
```

when we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for input, and when you type something and press enter, program prints `hello <your-input>`

for example here I entered `parsa` as input and program printed `hello parsa`

we can get input from user like above example


also look at this example:

```bash
set $num1 $num2;

mem 'enter first number: '; out ^;
read $num1;

mem 'enter second number: '; out ^;
read $num2;

# now, $num1 and $num2 are string. we convert string to int:
mem int($num1); copy $num1;
mem int($num2); copy $num2;

# now we want to plus them
set $sum;
mem $num1 + $num2; copy $sum;

print str($sum) + '\n';
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them
