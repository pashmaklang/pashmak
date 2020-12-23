## Read Input From User

You can read input from user in stdin.

look at this example:

```bash
print('what is your name? ')
$name = read() # read a input and put that in $name variable
println('hello ' + $name) # say hello to $name :)
```

When we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for input, and when you type something and press enter, program prints `hello <your-input>`.

for example here I entered `parsa` as input and program printed `hello parsa`.

We can get input from user like above example.

also look at this example:

```bash
$num1; $num2

print('enter first number: ')
$num1 = int(read())

print('enter second number: ')
$num2 = int(read())

# now we want to plus them
$sum = $num1 + $num2

println(str($sum))
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them.

### Reading command line arguments
To access command line arguments, you can use `$argv` variable.
this variable is a public variable and is list contains command line arguments.

look at this example:

```bash
println($argv[1])
```

we run above code:

```bash
pashmak mycode.pashm hello
```

output:

```
hello
```

Type of `$argv` is the python `list`.
