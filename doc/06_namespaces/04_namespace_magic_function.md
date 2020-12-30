# `__namespace__()` function
There is function named `__namespace__`. this function returns the current namespace as string.

Look at this example:

```bash
namespace app
    namespace core
        println(__namespace__())
    endns
endns

println(__namespace__())
```

output:

```
app.core.

```
