# Developer Guide
In This guide, we'll browse about source code of pashmak interpreter. if you want to know logic of this code or contribute to the pashmak project, this is helpful.

## Interpreter Flow
The `src/pashmak.py` file is the main cli entry point of pashmak, program starts from here. this script gets the file path and runs that. this script gives filepath to `src/core/jit.py`. The **Jit** compiler loads content of the file and returns that. the content, is parsed by `src/core/parser.py`'s **parser.parse(code, filename)** function.

The returned data by Parser, is a list from dictonaries (`list[dict]`). the output is list of commands which parsed one by one, comments are deleted.

The output of parser is like this:

```json
{
    "command": "<name-of-command>",
    "str": "<full-command-as-string>",
    "args": ["list", "of", "command", "arguments"],
    "args_str": "<arguments-as-string>",
    "file_path": "/path/to/script/file/this/code/is/in/that",
    "line_number": 12344
}
```

for example, look at this code:

```
println 'hello world'
```

output of parser is this:

```json
{
    "command": "println",
    "str": "println 'hello world'",
    "args": ["'hello", "world'"],
    "args_str": "'hello world'",
    "file_path": "/path/to/script/file/this/code/is/in/that",
    "line_number": 1
}
```

After parsing process, parsed commands will be runed by `src/core/program.py`(`class Program`) object.

for example:

```python
from core import parser, program
commands = parser.parse('<the-code>') # parse the code
prog = program.Program() # create the program object
prog.set_commands(commands) # set the parsed commands on program object
prog.start() # run the program. this method starts running commands one by one
```

### Builtin functions
Normally, lot of pashmak Functions like `print`, `import`, etc. are declared as **Pashmak function**. but some commands are **internal and builtin**. They are declared in `src/core/builtin_functions.py`. for example, `class` command which is used to declare classes, is the `run_class` method. this methods get the parsed command as dictonary and program object.

For example, `goto` command code is this:

```python
self.require_one_argument(op, 'goto function requires section name argument') # require one argument should be passed to command
arg = op['args'][0] # get the first argument as name of section
try:
    # check section exists
    section_index = self.sections[arg]
except KeyError:
    # section is not exists, raise the error
    return self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)
# section exists, change the program current step to the section
self.states[-1]['current_step'] = section_index-1
```

The above code is a example.

### Internal modules
Pashmak has some internal modules, like `@hash`, `@time`, etc.

They are declared in `src/modules`.

for example, `src/modules/hash.pashm` is accessible with `@hash`.
