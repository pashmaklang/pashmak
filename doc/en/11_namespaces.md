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

##### NOTE: name of namespace should not have `.` character. if you want to do this, use [subnamespace](#namespace-in-namespace-subnamespace).

this system is very useful.

### use command
the `use` command is a command to use content of a namespace.

look at this example:

```bash
namespace App
    func dosomething
        println('hello world')
    endfunc

    $name = 'parsa'
endns

App.dosomething()
println($App.name)
```

output:

```
hello world
parsa
```

we have to put `App.` before `dosomething` to run this function.
but i want to don't use namespace prefix and just type name of function to call this. what i have to do?

look at this example:

```bash
namespace App
    func dosomething
        println('hello world')
    endfunc

    $name = 'parsa\n'
endns

use App

App.dosomething()
dosomething()

println($App.name)
println($name)
```

output:

```
hello world
hello world
parsa
parsa
```

when i use `use` command and give a namespace as argument to that, i can call all of that namespace members without namespace prefix.

for example if there is a namespace named `App` and have a function named `dosomething`, for call that function i have to write `App.dosomething`. but if i run `use App`, after that i can call this function just by typing `dosomething;`

### namespace in namespace (subnamespace)
you can declare a namespace in a namespace

look at this example:

```bash
namespace App
    func hello
        println('hello world')
    endfunc

    # declare namespace `Core` under `App`
    namespace Core
        func run
            println('the core')
        endfunc
    endns
endns

# now we use it
App.hello()

App.Core.run()
```

output:

```
hello world
the core
```

### importing inside namespaces
you can import an script inside an namespace.

for example, we have `foo.pashm` and `bar.pashm` scripts.

##### `foo.pashm`:

```bash
namespace foo
    func hello
        println('hello world')
    endfunc
endns

func bye
    println('good bye')
endfunc
```

##### `bar.pashm`:

```bash
import('foo.pashm')

namespace App
    import('foo.pashm')
endns

foo.hello() # output: hello world
bye() # output: good bye

App.foo.hello() # output: hello world
App.bye() # output: good bye
```

in above example, we imported `foo.pashm` inside an namespace and content of `foo.pashm` is loaded under that namespace. for example, `foo.hello` function is loaded under `App` namespace, so finally will be set as `App.foo.hello`.
