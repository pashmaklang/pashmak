# command `use`
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
