# `isinstanceof` method
The `isinstanceof` method is available on all classes. It checks whether an object is an instance of a class.

For example:

```bash
class Hi
endclass

$a = Hi()

println($a->isinstanceof(Hi))
```

output:

```
True
```

The output above (`True`) means that `$a` is an instance of the `Hi` class.

Another example:

```bash
class Father
endclass

# class Child is child of class Father
class Child < Father
endclass

$a = Child()

println($a->isinstanceof(Father))
```

output:

```
True
```

The output above means that `$a` is an instance of the `Father` class.

But in this example:

```bash
class Foo
endclass

class Bar
endclass

$a = Bar()

println($a->isinstanceof(Foo))
```

output:

```
False
```

This is because the `Bar` class has no relation to the `Foo` class.

You can also pass the class name to this method as a string:

```bash
class Foo
endclass

$foo = Foo()
println($foo->isinstanceof('Foo')) # the `Foo` is a string
#println($foo->isinstanceof(Foo))
```

## Use classes for function typed arguments
For example:

```bash
class Person
    func __init__(string $name)
        $this->name = $name
    endfunc
endclass

func hello(Person $person)
    println('Hello ' + $person->name)
endfunc

hello(Person('parsa'))
```
