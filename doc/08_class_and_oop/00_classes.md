# Classes
class is a system to declare a structure of data. actually, class is a model with some fields.

for example, we want to declare a model from **Car**. we can declare a class:

```bash
class Car
    $name
    $color
endclass
```

Note: you can use keyword `end` instead of `endclass`. It is not different.

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

default value for that properties is `null`(`None`).

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

## classes in namespaces
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

## Advance property usage
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

## Class methods
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

    func say_hi()
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
