# Eval

you can run pashmak code from string.

look at this example:

```bash
mem 'mem "hello world from string\n"; out ^;'; eval ^;
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