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
