# Static methods and properties
Classes can have **static** methods or properties. You can use them directly on the class without creating an object.

For example:

```bash
class Person
    $static_prop = 'the static prop'

    func some_static_method
        println('the static method')
    endfunc
endclass

println(Person->static_prop)
Person->some_static_method()
```

output:

```
the static prop
the static method
```

Static properties and functions are declared just like regular properties and functions.

You can also assign values to static properties:

```bash
class Person
    $someprop = 'hello world'
endclass

println(Person->someprop)

Person->someprop = 'new value'

println(Person->someprop)
```

output:

```
hello world
new value
```

They are also accessible through objects:

```bash
class Person
    $static_prop

    func show_static_prop
        println('value: ' + $this->static_prop)
    endfunc
endclass

Person->static_prop = 'hello world'

$p = Person()

$p->show_static_prop()
```

output:

```
value: hello world
```
