# importing inside namespaces
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
