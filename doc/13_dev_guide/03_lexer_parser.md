# Lexer and Parser API

## Lexer
Lexer is in `src/core/lexer.py`.

#### `parse_op`: Parses one operation
Args:
- `op_str(str)`: The command as string
- `file_path(str)`: Which file this line is loaded from
- `line_number(int)`: Which line number this code loaded from

returns a dict.
Strructure:
```json
{
    "command": "<the command>",
    "args_str": "arguments of command as string",
    "str": "all of command as string",
    "args": ["arguments", "as", "list"], // seprated by ` ` space
    "file_path": "/path/to/file/that/this/line/loaded/from",
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
    "args": ["('hello", "world')"], // seprated by ` ` space
    "file_path": "/path/to/file/that/this/line/loaded/from",
    "line_number": 12
}
```

#### `parse_string`: Splits strings and codes
Args:
- `command(str)`: That thing you want to parse

Returns a list from other lists:

```json
[
    [false, "println("],
    [true, "'hello world'"],
    [false, ")"],
]
```

(the above output is for `println('hello world')`).
The first boolean item, if is True, means that this part is a string,
But if is False, means this is a native code.
And the second item is the code as string.

This function is useful when you want to replace/etc something on a code,
But only in native code and not on strings.

#### `parse_eval`: Converts the Pashmak eval code Python code
Args:
- `command(str)`: The command
- `self(program.Program)`: The program object

Returns a string from generated python code.

Example:
- `$name + '.'` -> `self.get_var('name') + '.'`
- `some_func($i + 1)` -> `self.functions['some_func'](self.get_var('i') + 1)`

```python
# inside class program.Program
eval(lexer.parse_eval('$name + '.'', self))
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

Also you can give the count:

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
This is The main parser function.

Args:
- `content(str)`: The code you want to parse
- `filepath(str)`: The file path you loaded file from
- `only_parse(bool)`: if is True, do not parses `if` statement(default is False)

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

If output is a list with 1 item, means this is a not `<a> = <b>`.
But if yes, first item is `<a>`(before `=`) and second it after `=`.

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
