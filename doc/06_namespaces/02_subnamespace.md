# namespace in namespace (subnamespace)
you can declare a namespace in a namespace

look at this example:

```bash
namespace App
    func hello()
        println('hello world')
    endfunc

    # declare namespace `Core` under `App`
    namespace Core
        func run()
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
