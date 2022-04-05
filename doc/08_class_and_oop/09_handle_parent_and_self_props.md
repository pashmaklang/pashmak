# Handling parent/self propeties/methods
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
