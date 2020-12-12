# Eval

you can run pashmak code from string.

look at this example:

```bash
eval 'println "hello world from string"'
```

output:

```
hello world from string
```

this code is runed from a string.

look at this example:

```bash
print 'enter some code: '
$code; read $code

eval $code
```

output:

```
enter some code: <input>mem 'hi\n'; print ^;
hi
```

the above code gets a string from user and runs that as pashmak code.

## run python code
you can run python code like `eval` with `python` command:

```bash
$code = 'print("hello world from python")'
python $code
```

output:

```
hello world from python
```
