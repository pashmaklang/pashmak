# `isinstanceof` method
The `isinstanceof` method is a general method for all of classes. this method can check that an object is in instanceof a class.

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

the above output(True) means that the `$a` object is a instance from class `Hi`.

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

The above output means that the `$a` object is instance of class `Father`.

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

Because class `Bar` haven't any relation with class `Foo`.

Also you can pass argument of this method as string:

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
