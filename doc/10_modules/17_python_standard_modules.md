# Python standard modules
You can use these Python standard modules directly in your Pashmak code:

- `os`
- `sys`
- `time`
- `hashlib`
- `random`
- `datetime`
- `json`
- `http`
- `base64`
- `socket`
- `socketserver`
- `math`
- `pprint`
- `subprocess`
- `sqlite3`
- `urllib`
- `platform`
- `mimetypes`
- `re`
- `pickle`

for example:

```bash
println(os.getuid())
println(random.random())
println('hash is ' + hashlib.sha256('hello'.encode()).hexdigest())
$cwd = os.getcwd()
$time = time.time() - 100
# ...
```

This can be useful when you need functionality from Python's standard library.

Also you can use `py_load_module` function.
If you want to import a module that is not imported by default, you can use this function.

Example:

```bash
$module = py_load_module('module_name')
$module->func_1()
# ...
```
