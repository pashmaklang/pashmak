# Constants
Constants (consts) are like variables, but one thing is different in constants: **the value of a constant cannot be changed**.

For example:

```bash
# declare the const
$&name = 'the value'

println($&name)
```

output:

```
the value
```

To declare consts, you only need to put a `&` in the name of the variable (its location is not important).

```bash
$&const1 = 123
$&const2 = 'fsgdf'
# ...
```

When we try to change the value of the const, we will get an error:

```bash
$&name = 'the name'

$&name = 'new value'
```

output:

```
ConstError: "$&name" is const and cannot be changed...
```

Also you can **declare** a constant but set its value later.

For example:

```bash
$&name # only declare constant, default value is `None`

# set value
$&name = 'parsa'

println($&name)
```

output:

```
parsa
```

But the second time, an error will be raised.
