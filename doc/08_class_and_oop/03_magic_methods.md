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
