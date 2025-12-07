# Labels
Labels are a system to make pointer to a part of code. This is useful to create loop, if and... and is used to handle program flow.

Actually, programs flow maybe changed by conditions and loop...
The label system is used to control program flow.

Look at this example:
```bash
label my_loop
    println('hello world')
goto my_loop
```

This code prints `hello world` non-stop.

Actually when my code starts, prints hello world and then `goto` commands directs program step to the `my_loop` label and it will repeat again and again.

###### NOTE: that TAB before `println('hello world')...` line is not required. This is written only to have beautiful code

Look at this example:

```bash
$i = 1

label loop
    println($i) # print($i)
    $i = $i + 1 # add 1 to $i
mem $i < 10; gotoif loop # check the condition in `mem` and use gotoif command
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

We have 3 functions about label system:
- label
- goto
- gotoif

### label
This command gets name of label as parameter like above examples. This is for declaring the label.

### goto
goto command gets a name as label name and sets program current step to that label.

### gotoif
gotoif checks `mem` and if mem is True, will go to wanted label. If not, does nothing and continue.

Look at this example:

```bash
# read age from user
print('enter your age: ')
$age = read()
$age = int($age)
# OR
$age = int(read())

mem $age > 18; gotoif age_is_more_than_18 # if age is more than 18, goto age_is_more_than_18 label

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
That code gets age of user as a integer, and checks conditions on that and does something by that conditions.
