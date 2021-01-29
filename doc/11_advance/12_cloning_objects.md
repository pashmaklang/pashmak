# Cloning objects
If you put a object into other variables, that will be pointer to original variable.

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

In the above example, why after changing `$b`, also `$a` was changed? Because we put `$a` into `$b`. now, `$b` points to real `$a`.(means it is not a copy).

But how to clone objects? We should use `clone` function:


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

