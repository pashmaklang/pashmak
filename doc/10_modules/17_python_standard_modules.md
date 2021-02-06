# Python standard modules
you can use this python standard modules in pashmak directly in your code:

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

this is very useful!

Also you can use `py_load_module` function.
if you want to import a module that not imported by default, you can use this function.

Example:

```bash
$module = py_load_module('module_name')
$module->func_1()
# ...
```

