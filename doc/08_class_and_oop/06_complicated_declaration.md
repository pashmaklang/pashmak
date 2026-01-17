# Complicated class declaration
You can declare class-in-class (like functions).

Look at this example:

```bash
class Foo
    $name = 'the foo'

    class Bar
        $name = 'the bar'
    endclass
endclass

println(Foo()->name)
println(Bar()->name)
```

output:

```
the foo
the bar
```

Also look at this example:

```bash
class First
    $name = 'first'
    class Second
        $name = 'second'

        class Last
            $name = 'last'
        endclass

        class Person
            $name = 'person'
        endclass
    endclass

    $the_second = Second()
endclass

println(First()->name)
println(Second()->name)
println(Last()->name)
println(Person()->name)

println(First()->the_second->name)
```

output:

```
first
second
last
person
second
```
