# Conditions
In the previous parts, you learned about `if` and program control flow methods.

All of them use **Conditions**. Conditions help you to handle the program flow.

For example:

```bash
if <this is condition>
    # ...
endif
```

Here, you can learn all of the condition features.

## Operators

### `<`: less than operator
This operator checks **whether a value is less than another value**.

For example:

```bash
if 10 < 100
endif

if 900 < 5
endif

$age = 40
if $age < 70
endif
```

### `>`: greater than operator
This operator checks **whether a value is greater than another value**.

For example:

```bash
if 40 > 30
endif

if 7 > 50
endif

$age = 90
if $age > 18
endif
```

### `<=` less or equals operator, `>=` greater or equals operator
These operators check **whether a value is less than/greater than or equal to another value**.

For example:

```bash
if 100 <= 100
endif

# ...

println(100 <= 100) # True
println(100 >= 200) # False
$age = 18
println($age <= 18) # True
println($age >= 18) # True
println($age >= 100) # False
# ...
```

### `==` equals operator, `!=` not equals operator
These operators check **whether a value is equal/not equal to another value**.

For example:

```bash
$age = 39

if $age == 39
endif

if $age != 100
endif
```

### `and` & `or`
This is a very important and useful logic. This helps you to combine conditions.

For example:

```bash
$age = 18
$country = 'somecountry'
if $age >= 18 and $country == 'somecountry'
endif
```

In the above example, both of the conditions should be `True` for the result of the whole condition to be `True`. If one or both of them are false, the result is false.

```bash
$age = 18
$country = 'somecountry'
if $age >= 18 or $country == 'somecountry'
endif
```

In the above example, if ONE OR BOTH of the conditions separated with `or` are True, the result is True.

Also you can use both `and` and `or`:

```bash
if $age > 18 and $age < 50 or $name == 'manager'
endif
```

### `not` keyword
The `not` keyword at the beginning of a condition reverses it.

For example:

```bash
if not $age > 18
endif
```

### Condition order
To set the order of conditions (like math operators), you should use `()`.

For example:

```bash
if $x and ($y or $x)
endif
```

The Pashmak condition system is handled by python.
[You can read more about conditions here](https://docs.python.org/3/reference/expressions.html#conditional-expressions).
