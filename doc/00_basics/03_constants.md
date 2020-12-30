# Constants
Constants (consts) are even like variables, but one thing is different in constants, **Constant value cannot be changed**.

for example:

```bash
# declare the const
$&name = 'the value'

println($&name)
```

output:

```
the value
```

To declare consts, you only need to put a `&` in the name of variable(location of that is not important).

```bash
$&const1 = 123
$&const2 = 'fsgdf'
# ...
```

When we try to change value of the const, we will get error:

```bash
$&name = 'the name'

$&name = 'new value'
```

output:

```
ConstError: "$&name" is const and cannot be changed...
```

also you can **declare** a constant, but set value of that later.

for example:

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

But in the second time, error will be raised.
