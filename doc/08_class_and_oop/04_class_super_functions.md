# Class super functions
there is some **Super functions** to handle classes at runtime.

### Checking class exists
You can check a class exists with `class.exists` function:

```bash
if class.exists('some_class')
    # ...
endif
```

### Geting list of all of classes
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

### Deleting a class
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

    func say_hi()
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
