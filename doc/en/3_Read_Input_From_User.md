## Read Input From User

you can read input from user in stdin

look at this example:

```bash
$name # set the name variable
print 'what is your name? '
read $name # read a input and copy that in $name variable
println 'hello ' + $name # say hello to $name :)
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
$num1; $num2

print 'enter first number: '
read $num1

print 'enter second number: '
read $num2

# now, $num1 and $num2 are string. we convert string to int:
$num1 = int($num1)
$num2 = int($num2)

# now we want to plus them
$sum = $num1 + $num2

println str($sum)
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them

also you can read value directly:

```bash
print 'enter your name: '
$name = ^ read ^
println 'hello ' + $name
```

the `^ read ^` reads value and puts that in the variable.

### read command line arguments
to access command line arguments, you can use `$argv` variable.

look at this example:

```bash
println $argv[1]
```

we run above code:

```bash
pashmak mycode.pashm hello
```

output:

```
hello
```

actualy, `$argv` is an array contains command line arguments.
