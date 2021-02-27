# Loading shared objects (DLLs)
You can load DLLs (`.so` files on linux/other and `.dll` in windows) using function `load_so`.

```bash
$dll = load_so('/path/to/file.so')

$dll->some_func()
# ...
```
