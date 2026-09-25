# Importing inside namespaces
You can import a script inside a namespace.

for example, we have `foo.pashm` and `bar.pashm` scripts.

#### `foo.pashm`:

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

#### `bar.pashm`:

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

In the above example, we imported `foo.pashm` inside a namespace and the content of `foo.pashm` is loaded under that namespace. For example, the `foo.hello` function is loaded under the `App` namespace, so finally it will be set as `App.foo.hello`.
