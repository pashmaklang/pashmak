# Labels
Labels are a system to make a pointer to a part of the code. This is useful for creating loops, ifs, etc. and is used to handle the program flow.

Actually, a program's flow may be changed by conditions and loops...
The label system is used to control the program flow.

Look at this example:
```bash
label my_loop
    println('hello world')
goto my_loop
```

This code prints `hello world` non-stop.

Actually when the code starts, it prints hello world and then the `goto` command directs the program step to the `my_loop` label, and it will repeat again and again.

###### NOTE: the TAB before the `println('hello world')...` line is not required. It is written only to have beautiful code

Look at this example:

```bash
$i = 1

label loop
    println($i) # print($i)
    $i = $i + 1 # add 1 to $i
mem $i < 10; gotoif loop # check the condition in `mem` and use the gotoif command
```

The output of this code is:

```
1
2
3
4
5
6
7
8
9
```

We have 3 functions for the label system:
- label
- goto
- gotoif

### label
This command gets the name of the label as a parameter like in the above examples. This is for declaring the label.

### goto
The goto command gets a name as the label name and sets the program's current step to that label.

### gotoif
gotoif checks `mem` and if the mem is True, it will go to the wanted label. If not, it does nothing and continues.

Look at this example:

```bash
# read age from user
print('enter your age: ')
$age = read()
$age = int($age)
# OR
$age = int(read())

mem $age > 18; gotoif age_is_more_than_18 # if age is more than 18, goto the age_is_more_than_18 label

# if not, this line will run and program goes to age_is_less_than_18
goto age_is_less_than_18

label age_is_more_than_18

    println('you are more than 18')
    goto after_if

label age_is_less_than_18

    println('you are less than 18')

label after_if

println('program ends')
```

We run the program:

```bash
enter your age: <input>22
you are more than 18
program ends
```

Run again:
```bash
enter your age: <input>14
you are less than 18
program ends
```

The above example is used to create conditions.
That code gets the age of the user as an integer, checks conditions on it and does something based on those conditions.
