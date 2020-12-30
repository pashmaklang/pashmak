## sys module
this module has some functions to manage pashmak internal envrinonment.

#### sys.path module
this module is for manage module paths. you can add new module paths and load modules from everywhere at runtime with this module.

to know about this module, go to next section [Module path system](#module-path-system).

#### `$sys.pashmakinfo`, access to pashmakinfo

if you want to access to pashmak interpreter info, `sys` module has a variable named `pashmakinfo`:

```bash
import @sys

println($sys.pashmakinfo)
```

output is something like this:

```
{'version': 'vx.y.z', 'pythoninfo': 'x.y.z (default, Jul x y, a:b:c) [GCC x.y.x]'}
```

this variable is a dictonary.
for example, to access pashmak version:

```bash
import @sys

println($sys.pashmakinfo['version'])
```

output:

```
v1.x.y
```

and `$sys.pashmakinfo['pythoninfo']` shows info of python.
