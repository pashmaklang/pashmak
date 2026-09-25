# Command `use`
The `use` command is a command to use the content of a namespace.

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

We have to put `App.` before `dosomething` to run this function.
But I don't want to use the namespace prefix and just want to type the name of the function to call it. What do I have to do?

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

When I use the `use` command and give a namespace as an argument to it, I can call all of that namespace's members without the namespace prefix.

For example, if there is a namespace named `App` which has a function named `dosomething`, to call that function I have to write `App.dosomething`. But if I run `use App`, after that I can call this function just by typing `dosomething;`
