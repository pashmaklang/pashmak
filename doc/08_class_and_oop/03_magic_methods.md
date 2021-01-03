# Class magic methods
now, you know what is the class methods. some methods in classes are special.

### `__init__`
the `__init__` method, will be runed when an object is created from a class.

look at this example:

```bash
class Person
    func __init__
        println('a new Person is created')
    endfunc
endclass

$p = Person()
```

output:

```
a new Person is created
```

also you can pass argument to `__init__` method. look at this example:

```bash
class Person
    func __init__($name)
        $this->name = $name
        println('hello ' + $this->name)
    endfunc
endclass

$p = Person('parsa')
println($p->name)
```

output:

```
hello parsa
parsa
```

### `__str__`
the `__str__` method, is a method to customize object string value.

look at this example:

```bash
class Person
    $name
endclass

$p = Person()
$p->name = 'parsa'
println($p)
# OR
println(Person())
```

output:

```
[PashmakObject name="Person"]
```

in the above example, when we print a object, default string value is the above output.

but we can customize this string with `__str__` method.

look at this example:

```bash
class Person
    $name

    func __str__
        return 'hello. my name is ' + $this->name
    endfunc
endclass

$p = Person()
$p->name = 'parsa'
println($p)
```

output:

```
hello. my name is parsa
```

in the above example, we declared `__str__` method for the class. then, when class is printed, output of `__str__` method will be used instead of that default string.

### Comparsion magic methods

- `__eq__($other)`: Handles the equality operator, `==`
- `__ne__($other)`: Handles the inequality operator, `!=`
- `__lt__($other)`: Handles the less-than operator, `<`
- `__gt__($other)`: Handles the greater-than operator, `>`
- `__le__($other)`: Handles the less-than-or-equal-to operator, `<=`
- `__ge__($other)`: Handles the greater-than-or-equal-to operator, `>=`

Example:

```bash
class Person
    func __init__($args)
        $args = format_args($args)
        $this->age = int($args[0])
    endfunc

    func __eq__($other)
        # compare the ages and return the boolean result
        return $this->age == $other->age
    endfunc

    func __lt__($other)
        return $this->age < $other->age
    endfunc

    # ...
endclass

println(Person(20) == Person(18)) # output: False
println(Person(70) > Person(30)) # output: True
println(Person(40) < Person(24)) # output: False
```

### Numeric magic methods

- `__pos__()`: Implements behavior for unary positive (e.g. +$some_object)
- `__neg__()`: Implements behavior for negation (e.g. -$some_object)
- `__abs__()`: Implements behavior for the built in abs() function.
- `__invert__()`: Implements behavior for inversion using the ~ operator.
- `__round__($n)`: Implements behavior for the built in round() function. n is the number of decimal places to round to.
- `__floor__()`: Implements behavior for math.floor(), i.e., rounding down to the nearest integer.
- `__ceil__()`: Implements behavior for math.ceil(), i.e., rounding up to the nearest integer.
- `__trunc__()`: Implements behavior for math.trunc(), i.e., truncating to an integral. 
