# Arrays
arrays are a list from variables.

look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack']

println $names # output: ['parsa', 'pashmak', 'jack']
println $names[0] # output: parsa
println $names[1] # output: pashmak
println $names[2] # output: jack
```

this is a example about array and loop:

```bash
$names = ['parsa', 'pashmak', 'jack']

$i = 0

section loop
    println $names[$i]
    $i = $i + 1
mem $i < len($names); gotoif loop
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### adding new item to array
you can add new item to an array by using python `append` and `insert` methods:

```bash
$myarray = ['first', 'second']
println $myarray

mem $myarray->append('new item')
println $myarray
```

output:

```
['first', 'second']
['first', 'second', 'new item']
```

also with `insert` method you can set the location of new item:

```bash
$myarray = ['one', 'two', 'four']
println $myarray

mem $myarray->insert(3, 'three')
println $myarray
```

output:

```
['one', 'two', 'four']
['one', 'two', 'three', 'four']
```

### removing an item from array
you can delete an item from array by using python `pop` method:

```bash
$myarray = ['first', 'second']
println $myarray

mem $myarray->pop(1)
println $myarray
```

output:

```
['first', 'second']
['first']
```

also `pop` method without argument removes last item by default.
