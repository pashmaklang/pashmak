# Sections
section is a system to make pointer to a part of code. this is useful to create loop, if and...

look at this example:
```bash
section my_loop
    println 'hello world'
goto my_loop
```

this code prints `hello world` non-stop

actually when my code starts, prints hello world and then `goto` commands directs program step to the `my_loop` section and it will repeat again and again.

###### NOTE: that TAB before `println 'hello world'...` line is not required. this is writen only to have beautiful code

look at this example:

```bash
$i = 1

section loop
    println $i # print $i
    $i = $i + 1 # add 1 to $i
mem $i < 10; gotoif loop # check the condition in `mem` and use gotoif command
```

the output of this code is
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

we have 3 operations about section system:
- section
- goto
- gotoif

### section
this command gets name of section as parameter like above examples. this is for declare the section

### goto
goto gets a name as section name and goto to that section.

### gotoif
gotoif checks `mem` and if mem is True, will go to wanted section. if not, do nothing and continue

look at this example:

```bash
# read age from user
print 'enter your age: '
$age; read $age
$age = int($age)

mem $age > 18; gotoif age_is_more_than_18 # if age is more than 18, goto age_is_more_than_18 section

# if not, this line will run and program goes to age_is_less_than_18
goto age_is_less_than_18

section age_is_more_than_18

    println 'you are more than 18'
    goto after_if

section age_is_less_than_18

    println 'you are less than 18'

section after_if

println 'program ends'
```

we run the program:

```bash
enter your age: <input>22
you are more than 18
program ends
```

run again:
```bash
enter your age: <input>14
you are less than 18
program ends
```
