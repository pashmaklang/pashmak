# Traits
The Pashmak classes can inherit one class as a parent.
All of the parent's properties and methods will be binded to the child class.
Also, all of the parent's parent's properties and methods...

But what if you want to include properties and methods from several classes?
Something like "inheriting from more than one classes".

For sovling this challange, there is something named *Trait system*.

Look at this example:

```bash
class FirstTrait
    func a()
        println 'A'
    endfunc
endclass

class SecondTrait
    func hello()
        println "Hello " + $this->name
    endfunc
endclass

class MyClass + FirstTrait, SecondTrait
    $name = "Parsa"
endclass

$obj = MyClass()

$obj->a()
$obj->hello()
```

The output is:

```
a
Hello Parsa
```

You see, the methods and properties are included from two classes!

Also you can keep normal inheriting type:

```bash
class Child < Parent + Trait1, Trait2...
```

### Inheritance in traits is impossible
Look at this example:

```bash
class Trait1
    func a()
    endfunc
endclass

class Trait2 < Trait1 # second trait extends from first trait
    func b()
    endfunc
endclass

class MyClass + Trait2
endclass

$a = MyClass()
$a->b() # ok
$a->a() # ERROR!
```

In the above example calling method `a` in that object raised an error.
But why?

Because `MyClass` included only trait `Trait2`.
Even `Trait2` extends from `Trait1`, but this does not works for trait.
Only the trait self methods and properties will be included, not it's parents.

### Priority in traits
Look at this example:

```bash
class T1
    func hello()
        println 'T1: hello'
    endfunc
endclass

class T2
    func hello()
        println 'T2: hello'
    endfunc
endclass

class MyClass + T2, T1
endclass

$a = MyClass()

$a->hello() # output: T2: hello
```

As you can see, both of the used traits have method `hello`.
But when we called it on our object, method `hello` in trait `T2` has been called.
Why?
Because of the priority of the traits. Priority is with first used traits.

### `__traits__` attribute
This attribute in classes contains list of binded traits to a class.

Look at this example:

```bash
class T1
endclass

class T2
endclass

class MyClass + T1, T2
endclass

println MyClass->__traits__
```

output:

```
['T1', 'T2']
```

### `isinstanceof`
The Traits will be handled in method `isinstanceof`.

Look at this example:

```bash
class Trait
endclass

class MyClass + Trait
endclass

$a = MyClass()
println $a->isinstanceof(Trait)
```

output:

```
True
```
