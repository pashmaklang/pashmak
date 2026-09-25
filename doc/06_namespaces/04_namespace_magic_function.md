# `__namespace__()` function
There is a function named `__namespace__`. This function returns the current namespace as a string.

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
