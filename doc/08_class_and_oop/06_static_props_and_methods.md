# class Static methods & properties
Classes can have **Static** methods or properties. The static means that for using them we not need to create a object from them and we can use them directly on class.

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

The static properties and functions are EVENT LIKE normal declaration of them.

Also they can recive the value:

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

Also they are accessible in objects:

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
