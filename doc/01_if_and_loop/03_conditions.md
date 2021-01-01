# Conditions
In the previous parts, you learned about `if` and program control flow methods.

All of them are using **Conditions**. Conditions help you to handle program flow.

for example:

```bash
if <this is condition>
    # ...
endif
```

Here, you can learn all of condition features.

## Operators

### `<`: less than operator
This operator checks **Is a value less than other value**.

for example:

```bash
if 10 < 100
endif

if 900 < 5
endif

$age = 40
if $age < 70
endif
```

### `>`: grater than operator
This operator checks **Is a value grater than other value**.

for example:

```bash
if 40 > 30
endif

if 7 > 50
endif

$age = 90
if $age > 18
endif
```

### `<=` less or equals operator, `>=` grater or equals operator
this operator checks **is a value less/grater or equals another value**.

for example:

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
This operator checks that **Is a value equals/not equals another value**.

for example:

```bash
$age = 39

if $age == 39
endif

if $age != 100
endif
```

### `and` & `or`
This is a very important and useful logic. this helps you to combination conditions.

for example:

```bash
$age = 18
$country = 'somecountry'
if $age >= 18 and $country == 'somecountry'
endif
```

in the above example, both of condtions should be `True` to result of all of condition return `True`. if one or both of them are false, result is false.

```bash
$age = 18
$country = 'somecountry'
if $age >= 18 or $country == 'somecountry'
endif
```

In the above example, if ONE OR BOTH of the conditions seprated with `or` are True, result is True.

Also you can use both of `and` and `or`:

```bash
if $age > 18 and $age < 50 or $name == 'manager'
endif
```

### `not` keyword
The `not` keyword in the first of condition, reverses that.

for example:

```bash
if not $age > 18
endif
```

### Condition order
To set order of conditions(Like math operators), you should use `()`.

for example:

```bash
if $x and ($y or $x)
endif
```

The pashmak condition system is handled by python.
[You can read more about conditions here](https://docs.python.org/3/reference/expressions.html#conditional-expressions).
