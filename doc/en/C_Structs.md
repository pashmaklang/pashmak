# Structs
struct is a system to declare a structure of data. actually, struct is a model with some fields.

for example, we want to declare a model from **Car**. we can declare a struct:

```bash
struct Car
    $name
    $color
endstruct
```

in above example, we declared a structure named `Car` with `name` and `color` properties.

let's use this:

```bash
struct Car
    $name
    $color
endstruct

$my_car = ^ new Car

println $my_car
```

output:

```
[PashmakStruct name="Car"]
```

now, we want to set the properties:

```bash
struct Car
    $name
    $color
endstruct

$my_car = ^ new Car
$my_car->name = 'BMW'
$my_car->color = 'white'

println $my_car->name ' ' + $my_car->color
```

output:

```
BMW white
```

so, let's review the structures. for declaring the structs, we have to use `struct` and `endstruct` commands:

```bash
struct TheStructName
    # declare the properties
endstruct
```

between them, you have to declare properties like normal variables:

```bash
struct TheStructName
    # declare the properties
    $prop1
    $prop2
    $prop3; $prop4
endstruct
```

default value for that properties is `None`.

also you can set the default value:

```bash
struct TheStructName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endstruct
```

now, we declared our struct, how to create a instance from that? actually, we can create infinitivly object from that. for example we have a thing named `Car`, this is a structure and we have much many objects with `Car` structure.

```bash
struct TheStructName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endstruct

$my_object = ^ new TheStructName
```

the `new` command gets name of struct and creates an instance from that and puts that in the mem temp value.
means, if i want to put created object in a variables, i need to write `$var = ^ new StructName`.

also we can create that with another syntax:

```bash
$my_object # declare the variable
new StructName # create the object
copy $my_object # copy created object to variable

# finally
$my_object; new StructName; copy $my_object
```

now, we can create object from a struct. how to access to the properties? look at this example:

```bash
struct Car
    $name = 'default name'
    $color
endstruct

$my_car = ^ new Car

println $my_car->name # output: default name
```

we can access to the object properties by writing `$varname->property_name`

the `->` symbol is important.

also you can set the value with this syntax:

```bash
struct Car
    $name = 'default name'
    $color
endstruct

$my_car = ^ new Car

println $my_car->name # output: default name

# setting the new value
$my_car->name = 'new name'
println $my_car->name # output: new name
```

### structs in namespaces
you can declare structs inside the namespaces like variables and functions.

for example:

```bash
namespace Models
    struct Car
        $name
        $color
    endstruct
endns

$my_car = ^ new Models.Car
```

all of laws for **structs in namespaces** is like `functions` and `variables`.

### Advance property usage
you can use more features of the properties. actually, you can create any structure in your properties.

look at this example:

```bash
struct Brand
    $title = 'the brand name'
endstruct

struct Car
    $name
    $color

    # the brand property is a object from Brand struct
    $brand = ^ new Brand
endstruct

$my_car = ^ new Car
$my_car->name = 'my car'
$my_car->brand->title = 'BMW'

println $my_car->name
println $my_car->brand->title
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
struct Car
    $name
    $color
endstruct

$my_car = ^ new Car
$my_car->name = 'my car'
$my_car->color = 'red'

$my_car->the_new_prop = 'the value'

println $my_car->the_new_prop
```

output:

```
the value
```

in the above example, property `the_new_prop` is not declared in struct by default, but you can add props without any problem in objects.

also you can use **Consts** in structs.

for example:

```bash
struct Person
    $name = 'parsa'
    $_age = 100 # age is const
endstruct

$p = ^ new Person

$p->_age = 50
```

output:

```
StructConstError:...
```

if you want to set a peoperty as constant, you have to put a `_` in the start of that name.

### inheritance
the inheritance in structs means structs can be child of another structs. this means the child struct has all of he's/she's parent properties.

look at this example:

```bash
struct Thing
    $name
endstruct

struct Animal < Thing
    $title
    $size
    $color
    $gender
endstruct

struct Cat<Animal
    $mioo
endstruct

struct Human<Animal
    $height
endstruct
```

in the above example, we used `<` symbol to make a struct child of another struct:

```bash
struct Parent

endstruct

# the `Child < Parent` sets this struct as child of the `Parent`
struct Child < Parent

endstruct
```

the child struct, has all of properties of the parent.

for example:

```bash
struct Father
    $name = 'hello world'
endstruct

struct Child < Father
    $age = 100
endstruct

$child = ^ new Child

println $child->name # output: hello world
println $child->age # output: 100
```

actually, the parent struct has not properties of he's childs, but childs has all of parent's props.

#### All of structs extends `Object` struct
all of structs by default extedns from a struct named `Object`. this struct is a internal pashmak struct.
all of structs are child of this struct.
