# Function `match()`
This function is a helper to make this syntax easier:

```bash
$result = null

if $value == 'A'
    $result = 'The A'
elif $value == 'B'
    $result = 'The B'
else
    $result = 'Other'
endif
```

The above syntax is long. You can use `match()`:

```bash
$result = match($value, [
    ['A', 'The A'],
    ['B', 'The B'],
])
```

Also you can use `default` argument for set the `else`:

```bash
$result = match($value, [
    ['A', 'The A'],
    ['B', 'The B'],
], default='Other')
```

