# The Jit Compiler
What does the JIT compiler do? JIT means `Just in time`.
This system speeds up the interpretation process.

The first time you run code, the JIT loads, parses, and lexes the source,
then caches the parsed code.

On later runs, the JIT checks whether a cache is available for the code.
If so, it loads the cache instead of parsing the code again.
The JIT also checks whether the file has changed. It stores a SHA-256 hash of the script in the cache
and parses the code again if the hash changes.

How do you use it? The JIT is in `src/core/jit.py`.
Use it instead of parsing code directly with the parser.

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

The first and second arguments may be the same, but they serve different purposes.
The first is the actual file path to load. The second is the path recorded in the parsed result (`code_location`).
The error reporting system uses it to show which file a line of code came from. Usually, both arguments are the same.

The `jit.load` function also accepts these arguments:

```
path(str): the actual file path
code_location(str): the path to record on parsed commands (passed to the parser)
self(Program): the current program object
is_jit_disabled(bool): set to True to parse the code without using the cache
ismain_default(bool): the default value of the `$__ismain__` variable
```
