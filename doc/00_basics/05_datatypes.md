# Datatypes
The whole Pashmak variable datatype system is handled by Python. Python is the programming language Pashmak is written in.

### What is a datatype?
In the previous parts, you learned about **Variables**.

For example:

```bash
$name = 'hello'
$age = 15
$gender = False
# ...
```

**Values of variables have different types.**

For example, numbers, strings (text), booleans (True or False), floats...

This is a table of all the datatypes:

|Name|Description|Example|
|----|-----------|-------|
|`str`|The string (text) is a list of characters|For example `"hello world"`, `'parsa'`... You should write them between `""` or `''` (there is no difference)|
|`int`|The integer numbers|`12`, `146433`...|
|`float`|The float numbers|`124.345`, `1.543657`...|
|`list`, `tuple`, `dict`|List of variables|Learn about them in the next part, [Arrays](06_arrays.md)
|`bool`|The `True` or `False`. This type is used in the condition system|`True`, `False`

[You can see the FULL documentation of Python datatypes here](https://docs.python.org/3/library/stdtypes.html).

### null (None)
`null` or `None` is a type of value. They mean empty.

For example:

```bash
$something = None
$something = null
```

The `None` and `null` keywords are exactly the same (`null` is an alias for `None`).
