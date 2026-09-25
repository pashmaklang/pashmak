# Inheritance
Inheritance allows a class to be a child of another class. A child class has all of its parent class's properties.

Look at this example:

```bash
class Thing
    $name
endclass

class Animal < Thing
    $title
    $size
    $color
    $gender
endclass

class Cat<Animal
    $mioo
endclass

class Human<Animal
    $height
endclass
```

In the above example, we used the `<` symbol to make one class a child of another:

```bash
class Parent

endclass

# the `Child < Parent` sets this class as child of the `Parent`
class Child < Parent

endclass
```

A child class has all of the parent's properties.

for example:

```bash
class Father
    $name = 'hello world'
endclass

class Child < Father
    $age = 100
endclass

$child = Child()

println($child->name) # output: hello world
println($child->age) # output: 100
```

The parent class does not have its children's properties, but each child has all of its parent's properties.

Also this system works for methods.

For example:

```bash
class Father
    func hello
        println('hello father')
    endfunc
endclass

class Child < Father
endclass

$a = Child()
$a->hello()
```

### All of classes extends `Object` class
All classes extend a class named `Object` by default. This is an internal Pashmak class, and every class is a child of it.
