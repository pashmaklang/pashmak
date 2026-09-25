# Read Input From User

You can read input from the user on stdin.

Look at this example:

```bash
print('what is your name? ')
$name = read() # read an input and put it in the $name variable
println('hello ' + $name) # say hello to $name :)
```

When we run this code, the output is this:

```
what is your name? <input>parsa
hello parsa
```

After printing `what is your name? ` the program waits for input, and when you type something and press enter, the program prints `hello <your-input>`.

For example, here I entered `parsa` as the input and the program printed `hello parsa`.

We can get input from the user like in the above example.

Also look at this example:

```bash
$num1; $num2

print('enter first number: ')
$num1 = int(read())

print('enter second number: ')
$num2 = int(read())

# now we want to add them together
$sum = $num1 + $num2

println(str($sum))
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

This example gets two numbers from the user and shows their sum.

You can also pass a message argument to the function `read`. This argument will be printed before the input.

For example:

```bash
$name = read('enter your name: ')
println $name
```

## Reading command line arguments
To access command line arguments, you can use `$argv` variable.
This variable is a public variable and is a list containing the command line arguments.

Look at this example:

```bash
println($argv[1])
```

We run the above code:

```bash
pashmak mycode.pashm hello
```

output:

```
hello
```

The type of `$argv` is the Python `list`.
