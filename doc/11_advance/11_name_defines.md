# Name Defines
The name define system is similar to variables, but defines have some differences:
- Defines are global, accessible everywhere, and are not isolated in function frames.
- Defines are not synchronized with namespaces.
- Defines are constants and cannot be changed.
- You do not need to put `$` before a define's name to access it.

Look at this example:

```bash
define('THE_NAME', 'parsa')

println(THE_NAME)
```

output:

```
parsa
```

In the example above, I defined `THE_NAME` and assigned it the value `parsa`.

##### NOTE: We recommend writing define names in uppercase.

### `is_defined()`
This function checks whether a name is defined and returns a boolean.

```bash
println(is_defined('SOMETHING'))

define('SOMETHING', 'the value')

println(is_defined('SOMETHING'))
```

output:

```
False
True
```

### `undefine()`
This function removes a define.

```bash
define('SOMETHING', 'the value')

println(is_defined('SOMETHING'))

undefine('SOMETHING')

println(is_defined('SOMETHING'))
```

output:

```
True
False
```

### `all_defines()`
This function returns all defines as a dictionary.

```bash
println(all_defines())
```

output:

```
{'FOO': 'BAR', ...}
```

### `redefine()`
Defines cannot be defined again. For example:

```bash
define('NAME', 'parsa')
define('NAME', 'pashmak')
```

output:

```
DefineError: name "NAME" already defined...
```

To redefine a name:

- Check whether the name is currently defined.
- If it is defined, undefine it.
- Define the new value.

The above steps are provided as a function named `redefine()`:

```bash
define('NAME', 'parsa')
println(NAME)

redefine('NAME', 'pashmak')
println(NAME)
```

output:

```
parsa
pashmak
```
