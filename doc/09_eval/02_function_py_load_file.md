# `py_load_file`
`py_load_file` is a function to load Python scripts as objects in Pashmak.

for example, we have `myscript.py`:

```python
def somefunc():
	print("hello world")

the_var = 'the value'

```

And our Pashmak script:

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

Also, if your Python script imports another Python module, you should add the path of that module to the `PYTHONPATH` env var. For example:

```bash
PYTHONPATH=/path/to/pypath pashmak myapp.pashm
```

