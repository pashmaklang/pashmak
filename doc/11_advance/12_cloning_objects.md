# Cloning objects
When you assign an object to another variable, the new variable refers to the original object.

Look at this example:

```bash
$a = {'foo': 'bar'} # a dictionary
$b = $a

println($a['foo']) # `bar`
println($b['foo']) # `bar`

# we change `$b`:
$b['foo'] = 'new'

println($b['foo']) # `new`

println($a['foo']) # `new`!
```

In the example above, changing `$b` also changes `$a` because both variables refer to the same object. Assigning `$a` to `$b` does not create a copy.

To create a separate copy of an object, use the `clone` function:


```bash
$a = {'foo': 'bar'} # a dictionary

# using clone function
$b = clone($a)

println($a['foo']) # `bar`
println($b['foo']) # `bar`

# we change `$b`:
$b['foo'] = 'new'

println($b['foo']) # `new`

println($a['foo']) # `bar` (the old value)
```
