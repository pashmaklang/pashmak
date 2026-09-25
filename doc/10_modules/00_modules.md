# Internal Modules
Pashmak includes several built-in modules that provide useful functionality.

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

Pass the module name to the `import` command with `@` before it.
