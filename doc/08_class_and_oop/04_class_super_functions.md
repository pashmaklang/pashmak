# Class super functions
There are several **super functions** for handling classes at runtime.

### Checking class exists
You can check a class exists with `class.exists` function:

```bash
if class.exists('some_class')
    # ...
endif
```

### Getting a list of all classes
You can get a list of all classes with the `class.list` function:

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
You can delete a class at runtime with the `class.delete` function:

```bash
class.delete('some_class')
```

### Putting classes into variables
Classes are like variables: you can store them in variables and use them.

Look at this example:

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

# putting the class into a variable
$myclass = Person

# calling the variable
$person1 = $myclass('pashmak')
$person1->say_hi()
```

output:

```
hello pashmak
```

You can also change the value of a class. Classes are like variables and can be reassigned.

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
