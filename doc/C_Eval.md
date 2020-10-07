# Eval

you can run pashmak code from string.

look at this example:

```bash
mem 'mem "hello world from string\n"\; out ^;'\; eval ^;
```

output:

```
hello world from string
```

this code is runed from a string

look at this example:

```bash
set $code;
mem 'enter some code: '; out ^;
read $code;

eval $code;
```

output:

```
enter some code: <input>mem 'hi\n'; out ^;
hi
```

the above code gets a string from user and runs that as pashmak code.

also you can use `std.eval` function to have easier syntax:

```bash
# you can pass value directly
std.eval '<some-code>';
```

## run python code
you can run python code like `eval` with `python` command:

```bash
set $code; mem 'print("hello world from python")'; copy $code;
python $code;
```

output:

```
hello world from python
```

also you can use `py` function to pass value directly:

```bash
py 'print("hello world")';
```

output:

```
hello world
```
