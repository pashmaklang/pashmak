# Name Defines
Name defining system is like variable system. but in name defines, something is different:
- defines are global and accessible in everywhere and are not isolated in function frames
- defines are not sync with namespace
- defines are constant and cannot be changed
- in the syntax, you don't need to put `$` before name of defines for access to them

Look at this example:

```bash
define('THE_NAME', 'parsa')

println(THE_NAME)
```

output:

```
parsa
```

In the above example, i defined `THE_NAME` and put `parsa` as value of that.

##### NOTE: we suggest you to write name of defines fully capitalized

### `is_defined()`
This function checks a name is defined and returns boolean.

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
This function deletes a define.

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
This function returns all of defines as a dictionary.

```bash
println(all_defines())
```

output:

```
{'FOO': 'BAR', ...}
```

### `redefine()`
Defines cannot be defined again. for example:

```bash
define('NAME', 'parsa')
define('NAME', 'pashmak')
```

output:

```
DefineError: name "NAME" already defined...
```

RE-Defining something is easy:

- check is the name currently defined
- if name is defined, undefine it
- then, define new value

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
