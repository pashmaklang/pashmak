# The Jit Compiler
What does Jit compiler?
Jit means `Just in time`.
This system is for speed up interpreting process.

While you running a code at First time,
Jit loads source code and parses and lexes this,
Then caches the parsed code.

Then, at the second, third... time you run the same code,
Jit checks that is any cache available for that code.
If yes, do not parse the code again and load the cache
Also jit checks file change. Jit stores sha256 hash of the script in the cache
In the next times, checks that is file changed(using sha256), if yes, parses code again.

How to use it?
The jit is in `src/core/jit.py`.
Instead of parsing code directly using parser, use the jit.

While you are using parser directly:

```python
f = open('script.pashm', 'r')
content = f.read()
f.close()
parsed_code = parser.parse(content)
```

But if you want to use Jit:

```python
from . import jit

parsed_code = jit.load('/path/to/script.pashm', '/path/to/script.pashm', program_object)
```

The first and second argument are one thing, but why they are seprated?
The first argument is the real file path that you want to load.
But the second argument is a path to set on parsed core result(code_location).
The second will be used by error raiser system to show that this line of code is loaded from which file.
But usually, both of them are one thing.

Also there is other arguments for `jit.load` function:

```
path(str): the real file path
code_location(str): that file path you want to set on parsed code commands(will be passed to parser)
self(Program): the current program object
is_jit_disabled(bool): If Jit should be disabled, put True on this and then this function will parse code and do not uses the cache
ismain_default(bool): default value of $__ismain__ variable
```
