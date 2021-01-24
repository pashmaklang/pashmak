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
    func __init__($age)
        $this->age = int($age)
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

- `__add__($other)`: Implements addition.
- `__sub__($other)`: Implements subtraction.
- `__mul__($other)`: Implements multiplication.
- `__floordiv__($other)`: Implements integer division using the // operator.
- `__div__($other)`: Implements division using the / operator.
- `__mod__($other)`: Implements modulo using the % operator.
- `__divmod__($other)`: Implements behavior for long division using the divmod() built in function.
- `__pow__()`: Implements behavior for exponents using the `**` operator.
- `__lshift__($other)`: Implements left bitwise shift using the << operator.
- `__rshift__($other)`: Implements right bitwise shift using the >> operator.
- `__and__($other)`: Implements bitwise and using the & operator.
- `__or__($other)`: Implements bitwise or using the | operator.
- `__xor__($other)`: Implements bitwise xor using the ^^ operator. 

- `__radd__($other)`: Implements reflected addition.
- `__rsub__($other)`: Implements reflected subtraction.
- `__rmul__($other)`: Implements reflected multiplication.
- `__rfloordiv__($other)`: Implements reflected integer division using the // operator.
- `__rdiv__($other)`: Implements reflected division using the / operator.
- `__rmod__($other)`: Implements reflected modulo using the % operator.
- `__rdivmod__($other)`: Implements behavior for long division using the divmod() built in function, when divmod(other, self) is called.
- `__rpow__()`: Implements behavior for reflected exponents using the ** operator.
- `__rlshift__($other)`: Implements reflected left bitwise shift using the << operator.
- `__rrshift__($other)`: Implements reflected right bitwise shift using the >> operator.
- `__rand__($other)`: Implements reflected bitwise and using the & operator.
- `__ror__($other)`: Implements reflected bitwise or using the | operator.
- `__rxor__($other)`: Implements reflected bitwise xor using the ^^ operator. 

- `__repr__()`: Defines behavior for when repr() is called on an instance of your class. The major difference between str() and repr() is intended audience. repr() is intended to produce output that is mostly machine-readable (in many cases, it could be valid Python code even), whereas str() is intended to be human-readable.
- `__unicode__()`: Defines behavior for when unicode() is called on an instance of your class. unicode() is like str(), but it returns a unicode string. Be wary: if a client calls str() on an instance of your class and you've only defined __unicode__(), it won't work. You should always try to define __str__() as well in case someone doesn't have the luxury of using unicode.
- `__format__($formatstr)`: Defines behavior for when an instance of your class is used in new-style string formatting. For instance, "Hello, {0:abc}!".format(a) would lead to the call a.__format__("abc"). This can be useful for defining your own numerical or string types that you might like to give special formatting options.
- `__hash__()`: Defines behavior for when hash() is called on an instance of your class. It has to return an integer, and its result is used for quick key comparison in dictionaries. Note that this usually entails implementing __eq__ as well. Live by the following rule: a == b implies hash(a) == hash(b).
- `__nonzero__()`: Defines behavior for when bool() is called on an instance of your class. Should return True or False, depending on whether you would want to consider the instance to be True or False.
- `__dir__()`: Defines behavior for when dir() is called on an instance of your class. This method should return a list of attributes for the user. Typically, implementing __dir__ is unnecessary, but it can be vitally important for interactive use of your classes if you redefine __getattr__ or __getattribute__ (which you will see in the next section) or are otherwise dynamically generating attributes.
- `__sizeof__()`: Defines behavior for when sys.getsizeof() is called on an instance of your class. This should return the size of your object, in bytes. This is generally more useful for Python classes implemented in C extensions, but it helps to be aware of it.
