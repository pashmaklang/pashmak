# Loops
Loops allow you to run code more than one time.

For example, you want to print the numbers from `1` to `10`.

The bad way is this:

```bash
println(1)
println(2)
println(3)
# ...
println(9)
println(10)
```

But the better way is using loops:

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

Note: You can use the keyword `end` instead of `endwhile`. There is no difference.

Also you learned about loops in the **labels** part. The `while` loop makes the syntax easier.

The structure of a while loop:

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

    # add one to the counter
    $i = $i + 1
endwhile
```

output:

```
parsa
pashmak
jack
```

### Loop inside loop
You can use loops inside loops.


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
There is a keyword named `break`. You can use this keyword inside a loop and it breaks the loop.

For example, we have a loop and we want to handle it so that if the counter is `5`, the loop finishes:

```bash
$i = 0
while $i < 10
    println($i)

    if $i == 5
        println('counter was 5. loop broken.')
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
counter was 5. loop broken.
```

This keyword helps you to finish the loop in some special cases.

### `continue` keyword
There is a keyword named `continue`. This command goes back to the start of the loop and continues the loop. You can use this in special cases.

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

In the above example, the even numbers are ignored.
