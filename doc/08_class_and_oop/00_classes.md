# Classes
A class is a way to declare a data structure. It acts as a model with fields.

For example, we want to declare a model from **Car**. We can declare a class:

```bash
class Car
    $name
    $color
endclass
```

Note: You can use the keyword `end` instead of `endclass`. They are equivalent.

In the above example, we declared a class named `Car` with `name` and `color` properties.

Let's use this:

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

Now, we want to set the properties:

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

So, let's review the classes. For declaring the classes, we have to use `class` and `endclass` commands:

```bash
class TheClassName
    # declare the properties
endclass
```

Between them, you have to declare properties like normal variables:

```bash
class TheClassName
    # declare the properties
    $prop1
    $prop2
    $prop3; $prop4
endclass
```

The default value for these properties is `null` (`None`).

You can also set default values:

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass
```

Now that we have declared our class, how do we create an instance of it? We can create any number of objects from a class. For example, `Car` is a class, and we can create many objects of the `Car` class.

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass

$my_object = TheClassName()
```

Now we can create an object from a class. To access its properties, look at this example:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = Car()

println($my_car->name) # output: default name
```

We can access object properties by writing `$varname->property_name`.

The `->` symbol is important.

You can also set a property's value with this syntax:

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

##### NOTE: A class name must not contain any of these literal characters: `()+-/*%=}{<>[],. `.

## Classes in namespaces
You can declare classes inside the namespaces like variables and functions.

For example:

```bash
namespace Models
    class Car
        $name
        $color
    endclass
endns

$my_car = Models.Car()
```

All of laws for **classes in namespaces** is like `functions` and `variables`.

## Advanced property usage
You can use more features of the properties. Actually, you can create any structure in your properties.

Look at this example:

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

Property values can be objects, and this structure can be nested recursively.

You can access to properties by `->` symbol:

```bash
# access to `prop3` of `prop2` of `prop1` of $obj
$obj->prop1->prop2->prop3
```

You can also add new properties to an object:


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

In the above example, `the_new_prop` is not declared in the class, but you can add properties to objects.

You can also use **constants** in classes.

For example:

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

To make a property constant, put `_` at the start of its name.

## Class methods
You can declare functions inside classes. A function in a class is called a **method**.

Look at this example:

```bash
class Cat
    $name

    func mio
        println('miooo...')
    endfunc
endclass

# create an object from Cat
$my_cat = Cat()

$my_cat->mio()
```

output:

```
miooo...
```

You can call a class's functions as methods.

Another example:

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

In the above example, we used a variable named `$this`. It refers to the current object.

Another example:

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

**You can set an object's properties by using the `$this` variable, as in the examples above.**

total syntax:

```bash
$object->method_name('arguments...', 'arg2...')
```

Classes also inherit their parent classes' methods.

For example:

```bash
class Father
    func hi
        # returns this string
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
