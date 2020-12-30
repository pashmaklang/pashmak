# Classes
class is a system to declare a structure of data. actually, class is a model with some fields.

for example, we want to declare a model from **Car**. we can declare a class:

```bash
class Car
    $name
    $color
endclass
```

in above example, we declared a class named `Car` with `name` and `color` properties.

let's use this:

```bash
class Car
    $name
    $color
endclass

$my_car = Car()

println($my_car)
```

output:

```
[PashmakObject name="Car"]
```

now, we want to set the properties:

```bash
class Car
    $name
    $color
endclass

$my_car = Car()
$my_car->name = 'BMW'
$my_car->color = 'white'

println($my_car->name + ' ' + $my_car->color)
```

output:

```
BMW white
```

so, let's review the classes. for declaring the classes, we have to use `class` and `endclass` commands:

```bash
class TheClassName
    # declare the properties
endclass
```

between them, you have to declare properties like normal variables:

```bash
class TheClassName
    # declare the properties
    $prop1
    $prop2
    $prop3; $prop4
endclass
```

default value for that properties is `None`.

also you can set the default value:

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass
```

now, we declared our class, how to create a instance from that? actually, we can create infinitivly object from that. for example we have a thing named `Car`, this is a class and we have much many objects with `Car` class.

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass

$my_object = TheClassName()
```

now, we can create object from a class. how to access to the properties? look at this example:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = Car()

println($my_car->name) # output: default name
```

we can access to the object properties by writing `$varname->property_name`

the `->` symbol is important.

also you can set the value with this syntax:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = Car()

println($my_car->name) # output: default name

# setting the new value
$my_car->name = 'new name'
println($my_car->name) # output: new name
```

##### NOTE: class name should not contains `()+-/*%=}{<>[],. ` chars(literal chars)

### classes in namespaces
you can declare classes inside the namespaces like variables and functions.

for example:

```bash
namespace Models
    class Car
        $name
        $color
    endclass
endns

$my_car = Models.Car()
```

all of laws for **classes in namespaces** is like `functions` and `variables`.

### Advance property usage
you can use more features of the properties. actually, you can create any structure in your properties.

look at this example:

```bash
class Brand
    $title = 'the brand name'
endclass

class Car
    $name
    $color

    # the brand property is a object from Brand class
    $brand = Brand()
endclass

$my_car = Car()
$my_car->name = 'my car'
$my_car->brand->title = 'BMW'

println($my_car->name)
println($my_car->brand->title)
```

output:

```
my car
BMW
```

actually, your property value can be a object from other property and this process can be continued recursivly.

you can access to properties by `->` symbol:

```bash
# access to `prop3` of `prop2` of `prop1` of $obj
$obj->prop1->prop2->prop3
```

also you can set new properties on a object:


```bash
class Car
    $name
    $color
endclass

$my_car = Car()
$my_car->name = 'my car'
$my_car->color = 'red'

$my_car->the_new_prop = 'the value'

println($my_car->the_new_prop)
```

output:

```
the value
```

in the above example, property `the_new_prop` is not declared in class by default, but you can add props without any problem in objects.

also you can use **Consts** in classes.

for example:

```bash
class Person
    $name = 'parsa'
    $_age = 100 # age is const
endclass

$p = Person()

$p->_age = 50
```

output:

```
ClassConstError:...
```

if you want to set a peoperty as constant, you have to put a `_` in the start of that name.

### inheritance
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

#### All of classes extends `Object` class
all of classes by default extedns from a class named `Object`. this class is a internal pashmak class.
all of classes are child of this class.

### Class methods
you can declare function inside classes. the class's function is named **Method**.

look at this example:

```bash
class Cat
    $name

    func mio
        println('miooo...')
    endfunc
endclass

# create a object from Cat
$my_cat = Cat()

$my_cat->mio()
```

output:

```
miooo...
```

actually, you can call functions of a class.

another example:

```bash
class Cat
    $name

    func mio
        println('miooo... my name is ' + $this->name)
    endfunc
endclass

# create a object from Cat
$my_cat = Cat()
$my_cat->name = 'gerdoo'
$my_cat->mio()
```

output:

```
miooo... my name is gerdoo
```

in above example, we used a variable named `$this`. this variable is a pointer to self of object.

another example:

```bash
class Person
    $name

    func set_name($name)
        $this->name = $name
    endfunc

    func say_hi
        println('hello. my name is ' + $this->name)
    endfunc
endclass

$p = Person()

$p->set_name('parsa')

$p->say_hi()
```

output:

```
hello. my name is parsa
```

**You can set object self properties by using $this variable like above examples**

total syntax:

```bash
$object->method_name('arguments...', 'arg2...')
```

also all of classes extends parent methods.

for example:

```bash
class Father
    func hi
        # returnns this string
        return 'hello world'
    endfunc
endclass

class Child < Father; endclass

$obj = Child()

println($obj->hi())
```

output:

```
hello world
```
### Classes general attributes
classes has some general properties:

- `__name__`: name of the class
- `__parent__`: name of parent of class
- `__props__`: all of object properties as Dictonary
- `__methods__`: all of object methods as Dictonary
- `__theclass__`: the object class type

for example:

```bash
class Person

endclass

$person = Person()

println($person->__name__) # output: Person
```

### Class magic methods
now, you know what is the class methods. some methods in classes are special.

#### `__init__`
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

#### `__str__`
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

in the above example, we declared `__str__` method for the class. then, when class is printed, output of `__str__` method will be used instead of that default string (output of method should be put in `mem`).

### Class super functions
there is some **Super functions** to handle classes at runtime.

#### Checking class exists
You can check a class exists with `class.exists` function:

```bash
if class.exists('some_class')
    # ...
endif
```

#### Geting list of all of classes
You can get list of all of classes with `class.list` function:

```bash
$classes = class.list()

println($classes)
```

output:

```
['a', 'b', '...']
```

The output is a list.

#### Deleting a class
You can delete a class at runtime with `func.delete` function:

```bash
class.delete('some_class')
```

### Puting classes into variables
Classes are like variables, you can put them into variables and use them.

look at this example:

```bash
class Person
    $name

    func __init__($name)
        $this->name = $name
    endfunc

    func say_hi
        println('hello ' + $this->name)
    endfunc
endclass

# puting the class into the variable
$myclass = Person

# calling the variable
$person1 = $myclass('pashmak')
$person1->say_hi()
```

output:

```
hello pashmak
```

Also you can change value of classes. classes are like variables and can be changed.

For example:

```bash
class Foo
    $name = 'the foo'
endclass

class Bar
    $name = 'the bar'
endclass

$a = Foo()
$b = Bar()
println($a->name)
println($b->name)

Foo = Bar

$a = Foo()
$b = Bar()
println($a->name)
println($b->name)
```

output:

```
the foo
the bar
the bar
the bar
```

### Complicated class declaration
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

### class Static methods & properties
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

### `isinstanceof` method
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

### Handling parent/self propeties/methods
In inheritance system, Maybe we need to use some properties/methods in parent/other classes.

to undrestand this, look at this example:

```bash
class Father
    $name = 'the father'
endclass

class Child < Father
    $name = 'the child'
endclass

$a = Child()
println($a->name)
```

output:

```
the child
```

In the above example, the `name` property points to `Child` class name. But how we can access to `Father` name? We should use `super` method:

```bash
class Father
    $name = 'the father'
endclass

class Child < Father
    $name = 'the child'
endclass

$a = Child()
println($a->name)
println($a->super('Father')->name)
```

output:

```
the child
the father
```

Also this is useful for methods:

```bash
class Father
    func hello
        println('Father: hello!')
    endfunc
endclass

class Child < Father
    func hello
        println('Child: hello!')
    endfunc
endclass

$a = Child()
$a->hello()
$a->super('Father')->hello()
```

output:

```
Child: hello!
Father: hello!
```

Also you can use this for MORE THAN ONE LAYER:

```bash
class A
    func hello
        println('A: hello')
    endfunc
endclass

class B < A
    func hello
        println('B: hello')
    endfunc
endclass

class C < B
    func hello
        $this->super('A')->hello()
        $this->super('B')->hello()
        println('C: hello')
    endfunc
endclass

$c = C()
$c->hello()
```

output:

```
A: hello
B: hello
C: hello
```

Also sometimes we are using some methods in parent classes which they need to use self methods/props.

for understand it, look at this example:

```bash
class Father
    func foo
        $this->super('Father')->bar() # not child's `bar`
    endfunc
endclass
```
