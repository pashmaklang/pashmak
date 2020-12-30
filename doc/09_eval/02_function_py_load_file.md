# `py_load_file`
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

