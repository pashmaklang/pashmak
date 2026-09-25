# Arrays
Arrays are lists of variables.

Look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack']

println($names) # output: ['parsa', 'pashmak', 'jack']
println($names[0]) # output: parsa
println($names[1]) # output: pashmak
println($names[2]) # output: jack
```

This is an example of arrays and loops:

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

The above code prints the names one by one.

## Adding a new item to an array
You can add a new item to an array by using the Python `append` and `insert` methods:

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

Also with the `insert` method you can set the location of the new item:

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

## Removing an item from an array
You can delete an item from an array by using the Python `pop` method:

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

Also the `pop` method without an argument removes the last item by default.

## Setting the value of an item in an array
Look at this example:

```bash
$abc = ['a', 'b', 'c']
println($abc) # output: ['a', 'b', 'c']

$abc[0] = '000'
println($abc) # output: ['000', 'b', 'c']
```

Like in the above example, we can set a specific item of an array with a syntax like this: `$my_list[<index>] = <value>`.

Also you can do this on a subitem. Look at this example:

```bash
$my_list = []
$my_list->append(['a'])

println($my_list[0]) # output: ['a']

$my_list[0][0] = 'AAA'

println($my_list[0]) # output: ['AAA']
```

## Dictionaries
Dictionaries are like lists, but in dicts you can set a string as the key instead of an index number.

Look at this example:

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict) # output: {'hello': "Hello world", 'bye': 'Good bye!'}

println($my_dict['hello']) # output: Hello world
```

Like in the above example, we can use a string as the key instead of an index number. In the above example, `hello` is the key.

Also you can set the keys like in lists (arrays):

```bash
$my_dict = {'hello': "Hello world", 'bye': 'Good bye!'}
println($my_dict['hello']) # output: Hello world

$my_dict['hello'] = 'new hello'

println($my_dict['hello']) # output: new hello
```

The **list (array)** and **dict** are Python datatypes (which means you can use all of the Python list and dict methods on them).
