# Eval

you can run pashmak code from string.

look at this example:

```bash
eval('println("hello world from string")')
```

output:

```
hello world from string
```

this code is runed from a string.

look at this example:

```bash
print('enter some code: ')
$code = read()

eval($code)
```

output:

```
enter some code: <input>mem 'hi\n'; print(^);
hi
```

the above code gets a string from user and runs that as pashmak code.

## run python code
you can run python code like `eval` with `python` command:

```bash
$code = 'print("hello world from python")'
python($code)
```

output:

```
hello world from python
```

### `py_load_file`
The `py_load_file` is a function to load python scripts as object in pashmak.

for example, we have `myscript.py`:

```python
def somefunc():
	print("hello world")

the_var = 'the value'

```

and our pashmak script:

```bash
$pyobj = py_load_file('/path/to/myscript.py')

println($pyobj->the_var)
$pyobj->somefunc()
```

output:

```
the value
hello world
```

also if your python script imports another python module, you should add path of that module to `PYTHONPATH` env var. for example:

```bash
PYTHONPATH=/path/to/pypath pashmak myapp.pashm
```

