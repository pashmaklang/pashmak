# Internal Modules
Pashmak has some internal libraries to use. That modules are helpful for you.

## How to import module
You can import modules with `import` function.

Look at this example:

```bash
import '@hash'
import "@module_name"
import "@module1", '@module2'

# also you can import modules without quotes
import @sys
import @hash, @mymodule

# also you can import modules like scripts under the namespaces
namespace Foo
    import '@hash'
endns

# ...
```

You have to give name of module with a `@` before that to the include command.
