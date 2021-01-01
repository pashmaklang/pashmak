# Function super functions
there is some **Super functions** to handle functions at runtime.

## Checking function exists
You can check a function exists with `func.exists` function:

```bash
if func.exists('some_func')
    some_func()
endif
```

## Geting list of all of functions
You can get list of all of functions with `func.list` function:

```bash
$funcs = func.list()

println($funcs)
```

output:

```
['a', 'b', '...']
```

The output is a list.

## Deleting a function
You can delete a function at runtime with `func.delete` function:

```bash
func.delete('some_func')
```
