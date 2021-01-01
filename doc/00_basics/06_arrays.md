# Arrays
arrays are a list from variables.

look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack']

println($names) # output: ['parsa', 'pashmak', 'jack']
println($names[0]) # output: parsa
println($names[1]) # output: pashmak
println($names[2]) # output: jack
```

this is a example about array and loop:

```bash
$names = ['parsa', 'pashmak', 'jack']

$i = 0

while $i < len($names)
    println($names[$i])
    $i = $i + 1
endwhile
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

## adding new item to array
you can add new item to an array by using python `append` and `insert` methods:

```bash
$myarray = ['first', 'second']
println($myarray)

$myarray->append('new item')
println($myarray)
```

output:

```
['first', 'second']
['first', 'second', 'new item']
```

also with `insert` method you can set the location of new item:

```bash
$myarray = ['one', 'two', 'four']
println($myarray)

$myarray->insert(2, 'three')
println($myarray)
```

output:

```
['one', 'two', 'four']
['one', 'two', 'three', 'four']
```

## removing an item from array
you can delete an item from array by using python `pop` method:

```bash
$myarray = ['first', 'second']
println($myarray)

$myarray->pop(1)
println($myarray)
```

output:

```
['first', 'second']
['first']
```

also `pop` method without argument removes last item by default.

## setting value of an item in array
look at this example:

```bash
$abc = ['a', 'b', 'c']
println($abc) # output: ['a', 'b', 'c']

$abc[0] = '000'
println($abc) # output: ['000', 'b', 'c']
```

like above example, we can set a specify item of array with a syntax like this: `$my_list[<index>] = <value>`.

also you can do this on a subitem. look at this example:

```bash
$my_list = []
$my_list->append(['a'])

println($my_list[0]) # output: ['a']

$my_list[0][0] = 'AAA'

println($my_list[0]) # output: ['AAA']
```

## Dictonaries
dictonaries are like lists, but in dicts you can set a string as key instead of index number.

look at this example:

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict) # output: {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict['hello']) # output: Hello world
```

like above example, we can use string as key instead of index number. in the above example, `hello` is the key.

also you can set the keys like lists(arrays):

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}
println($my_dict['hello']) # output: Hello world

$my_dict['hello'] = 'new hello'

println($my_dict['hello']) # output: new hello
```

The **list(Array)** and **dict** are python datatypes(means you can use all of python list and dict methods on them).
