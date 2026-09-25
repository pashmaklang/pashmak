# Handling parent and self properties and methods
With inheritance, you may need to use properties or methods from parent or other classes.

To understand this, look at this example:

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

In the above example, the `name` property refers to the `Child` class's value. To access the `Father` value, use the `super` method:

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

This is also useful for methods:

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

You can also use this across multiple levels of inheritance:

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

To understand this, look at this example:

```bash
class Father
    func foo
        $this->super('Father')->bar() # not child's `bar`
    endfunc
endclass
```
