# Loading shared objects (DLLs)
You can load shared libraries with the `load_so` function. These files use the `.so` extension on Linux and other Unix-like systems, and `.dll` on Windows.

```bash
$dll = load_so('/path/to/file.so')

$dll->some_func()
# ...
```
