# Namespaces

name space is a very useful system to split sections of program.

look at this example:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endnamespace

App.say_hello
```

Note: you can use keyword `end` instead of `endnamespace`. It is not different.

output:

```
hello world
hello world
```

actualy, everything which is declared between `namespace <something>` and `endnamespace` will be under this.

in above example, we declared a namespace named `App`. and we declared `say_hello` function in that.

next, we called `say_hello` inside the namespace, and one time we called `say_hello` outside the namespace.

when we are calling a member of namespace from outside of that namespace, we have to put name of namespace with a `.` before name of that function

for example here, our namespace name is `App` and out function name is `say_hello`. we can write only `say_hello` inside the namespace but for call it from outside of namespace, we have to write `App.say_hello`.

also look at this example:

```bash
namespace First
    func dosomething
        println('i am from First')
    endfunc
endnamespace

namespace Last
    func dosomething
        println('i am from Last')
    endfunc
endnamespace

First.dosomething()
Last.dosomething()
```

output:

```
i am from First
i am from Last
```

also you can use `endns` keyword insted of `endnamespace`:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endns

App.say_hello()
```

also namespace system is sync with variables:

```bash
namespace App
    $name = 'parsa'
    println($name) # output: parsa
    println($App.name) # output: parsa
endns

println($App.name) # output: parsa

# but this has error:
println($name) # VariableError: undefined variable $name, because it is in App namespace and is accessible with `$App.name`
```

Also you can use `ns` alias instead of `namespace` keyword. for example:

```bash
ns app
    # ...
endns
```

##### NOTE: variable name should not contains `()+-/*%=}{<>[],. ` chars(literal chars)
