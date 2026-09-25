# Lexer and Parser API

## Lexer
Lexer is in `src/core/lexer.py`.

#### `parse_op`: Parse one operation
Args:
- `op_str(str)`: The command as string
- `file_path(str)`: Which file this line is loaded from
- `line_number(int)`: Which line number this code loaded from

Returns a dictionary with this structure:
```json
{
    "command": "<the command>",
    "args_str": "arguments of command as string",
    "str": "all of command as string",
    "args": ["arguments", "as", "list"], // separated by spaces
    "file_path": "/path/to/file/that/this/line/loaded/from",
    "strings": ["<output of `parse_string`>"],
    "line_number": 12
}
```

Example:

```python
print(lexer.parse_op("println('hello world')", "/path/to/file/that/this/line/loaded/from", 12))
# OR: `println 'hello world'`
```

output:

```json
{
    "command": "println",
    "args_str": "('hello world')",
    "str": "println('hello world')",
    "args": ["('hello", "world')"], // separated by spaces
    "file_path": "/path/to/file/that/this/line/loaded/from",
    "strings": ["<output of `parse_string`>"],
    "line_number": 12
}
```

#### `parse_string`: Splits strings and codes
Args:
- `command(str)`: That thing you want to parse

Returns a list of lists:

```json
[
    [false, "println("],
    [true, "'hello world'"],
    [false, ")"],
]
```

(the above output is for `println('hello world')`).
If the first boolean item is `True`, this part is a string; if it is `False`, this part is native code.
The second item contains the code as a string.

This function is useful when you want to replace/etc something on a code,
But only in native code and not on strings.

#### `parse_eval`: Convert Pashmak eval code to Python code
Args:
- `command(str)`: The command

Returns a string from generated python code.

Example:
- `$name + '.'` -> `[['v', 'name', 'self.get_var("name")'], ['l', '.'], ['s', "'.'"]]`
- `some_func($i + 1)` -> `[]`

```python
output = lexer.parse_eval('$name + "."')

py_code = ''

for item in output:
    py_code += item[-1]

eval(py_code)
```

#### `multi_char_split`: Splits by more than 1 character

Example:

```python
print(lexer.multi_char_split('12+19*14', '+*'))
```

output:

```
['12', '19', '14']
```

You can also specify the count:

```python
print(lexer.multi_char_split('12+19*14', '+*'), 1)
```

output:

```
['12', '19*14']
```

## Parser
Parser is in `src/core/parser.py`.

#### `parse`: Parses a code
This is the main parser function.

Args:
- `content(str)`: The code you want to parse
- `filepath(str)`: The file path you loaded file from
- `only_parse(bool)`: if `True`, do not parse `if` statements (defaults to `False`)

Returns a list:

```
[
    {<output of lexer.parse_op>},
    {<output of lexer.parse_op>},
    {<output of lexer.parse_op>},
    ...
]
```

Handles multiline and if statements.

#### `split_by_equals`: Splits `<something> = <something>` syntax
Args:
- `string(str)`: The command

Returns a list.

Example for `$name = 'pashmak'`: ['$name', "'pashmak'"]

Example for `println($name)`: ['println($name)']

If the output is a one-item list, the command is not in the form `<a> = <b>`.
Otherwise, the first item is `<a>` (before `=`), and the second is `<b>` (after `=`).

Other example:

```python
print(parser.split_by_equals('$age = 30'))
```

output:

```json
["$age", "30"]
```

Also:

```python
print(parser.split_by_equals('somefunc()'))
```

output:

```json
["somefunc()"]
```
