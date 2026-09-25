# Namespaces

A namespace is a very useful system to split the sections of a program.

Look at this example:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endnamespace

App.say_hello
```

Note: You can use the keyword `end` instead of `endnamespace`. There is no difference.

Output:

```
hello world
hello world
```

Actually, everything which is declared between `namespace <something>` and `endnamespace` will be under it.

In the above example, we declared a namespace named `App`. And we declared the `say_hello` function in it.

Next, we called `say_hello` inside the namespace, and one time we called `say_hello` outside the namespace.

When we are calling a member of a namespace from outside of that namespace, we have to put the name of the namespace with a `.` before the name of that function.

For example here, our namespace name is `App` and our function name is `say_hello`. We can write only `say_hello` inside the namespace, but to call it from outside of the namespace, we have to write `App.say_hello`.

Also look at this example:

```bash
namespace First
    func dosomething
        println('I am from First')
    endfunc
endnamespace

namespace Last
    func dosomething
        println('I am from Last')
    endfunc
endnamespace

First.dosomething()
Last.dosomething()
```

output:

```
I am from First
I am from Last
```

Also you can use the `endns` keyword instead of `endnamespace`:

```bash
namespace App
    func say_hello
        println('hello world')
    endfunc

    say_hello()
endns

App.say_hello()
```

Also the namespace system is in sync with variables:

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

Also you can use the `ns` alias instead of the `namespace` keyword. For example:

```bash
ns app
    # ...
endns
```

##### NOTE: a variable name should not contain the `()+-/*%=}{<>[],. ` characters (literal characters)
