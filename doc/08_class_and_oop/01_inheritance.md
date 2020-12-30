## inheritance
the inheritance in classes means classes can be child of another classes. this means the child class has all of he's/she's parent properties.

look at this example:

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

in the above example, we used `<` symbol to make a class child of another class:

```bash
class Parent

endclass

# the `Child < Parent` sets this class as child of the `Parent`
class Child < Parent

endclass
```

the child class, has all of properties of the parent.

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

actually, the parent class has not properties of he's childs, but childs has all of parent's props.

Also this system works for methods.

for example:

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

#### All of classes extends `Object` class
all of classes by default extedns from a class named `Object`. this class is a internal pashmak class.
all of classes are child of this class.
