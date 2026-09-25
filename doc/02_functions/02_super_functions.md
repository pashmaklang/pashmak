# Function super functions
There are some **Super functions** to handle functions at runtime.

## Checking whether a function exists
You can check whether a function exists with the `func.exists` function:

```bash
if func.exists('some_func')
    some_func()
endif
```

## Getting a list of all functions
You can get a list of all functions with the `func.list` function:

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
You can delete a function at runtime with the `func.delete` function:

```bash
func.delete('some_func')
```
