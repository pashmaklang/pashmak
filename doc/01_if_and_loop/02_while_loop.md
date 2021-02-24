# Loops
Loops allows you to run a code more than one times.

for example, you want to print numbers from `1` to `10`.

The bad way is this:

```bash
println(1)
println(2)
println(2)
# ...
println(9)
println(10)
```

but the best way is using loops:

```bash
$i = 1
while $i <= 10
    println($i)
    $i = $i + 1
endwhile
```

output:

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
10
```

Also you learned about loops in the **labels** part. The `while` loop makes the syntax easier.

Structure of while loop:

```bash
while <condition>
    # code...
endwhile
```

For example:

```bash
$names = ['parsa', 'pashmak', 'jack']

# set the counter
$i = 0

# the loop
while $i < len($names)
    # print the current name
    println($names[$i])

    # add one two counter
    $i = $i + 1
endwhile
```

output:

```
parsa
pashmak
jack
```

### Loop in loop
You can use loops in loops.


In this example, we print a square using the loops:

```bash
$i = 0
while $i < 10
    $j = 0
    while $j < 30
        print('*')
        $j = $j + 1
    endwhile
    print('\n')
    $i = $i + 1
endwhile
```

output:

```
******************************
******************************
******************************
******************************
******************************
******************************
******************************
******************************
******************************
******************************
```

### `break` keyword
There is keyword named `break`. you can use this keyword between the loop and that breaks the loop.

For example, we have a loop and we want to handle that if counter is `5`, finish the loop:

```bash
$i = 0
while $i < 10
    println($i)

    if $i == 5
        println('counter was 5. loop breaked.')
        break
    endif

    $i = $i + 1
endwhile
```

output:

```
0
1
2
3
4
5
counter was 5. loop breaked.
```

This keyword helps you to finish the loop in some exceptions.

### `continue` keyword
There is a keyword named `continue`. this command backs to first of loop and continues the loop. You can use this is exceptions.

```bash
$i = 0
while $i < 10
    if $i % 2 == 0
        $i = $i + 1
        continue
    endif
    println($i)
    $i = $i + 1
endwhile
```

In the above example, odd numbers ignored.
