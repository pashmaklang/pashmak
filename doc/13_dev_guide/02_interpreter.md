# Interpreter Core Structure
Here, we explore in structure of interpreter Core.

## Interpreter Flow
The main CLI entry point of interpreter is `src/pashmak.py`.
This script gets the file name that user want to run. Then, loads content of this file, parses the code, and then gives the parsed code to class `Program` in `src/core/program.py`. This class is the main executor of the Pashmak.

##### NOTE: actually, `src/pashmak.py` uses `Jit` to load and parse the file, but you learn about it in the next parts.

The parser receives the code as a string and splits it on `\n` and `;` (using a newline or `;` to separate operations is equivalent). It then handles multiline syntax, combining operations written across multiple lines into one line. Next, it passes each line to the lexer's `parse_op` function in `src/core/lexer.py`. The lexer splits parts of the code and returns a dictionary. The parser then builds a list from these dictionaries and processes the list further, for example, converting `if..elif..else` statements to a `label` system.

Finally, parser returns the parsed code.

Now, a new object from class `program.Program`(in `src/core/program.py`) will be created and parsed code will be passed to this object:

```python
prog = program.Program([]) # the argument to __init__ is the cli arguments
prog.set_commands(parsed_commands)
```

Now, its time to start running this code:

```python
prog.start()
```

the `start` method starts running commands one by one.

## Frames
The frame system is important for importing scripts and calling functions. For example, consider this Pashmak code:

```bash
func get_sum($a, $b)
    return $a + $b
endfunc

$a = 10
$b = 5
$sum = get_sum($a, $b)
println($sum)
```

when executor is running this code line by line, what about calling `get_sum` and `println` functions?

This is how the frame system works: when a function is called, a new frame is created and the function body runs in it. When that frame finishes, the program returns to the previous frame.

Frames also help isolate variables, namespaces in use, and other state.
In the `Program` class, frames are accessible in:

```python
self.frames # this is a list
```

The main frame is set by default on program.

```
self.frames: [<main-frame>]

# after calling a function:
self.frames: [<main-frame>, <inner-frame>]

# after calling new function inside other function
self.frames: [<main-frame>, <inner-frame>, <other>...]
```

This is the general structure.

When the program runs code line by line and encounters a function call, it creates a new frame and starts running it. When that frame finishes, execution returns to the previous frame.

Structure of `self.frames` variable is a `list[dict]`.

There is lot of more notes about this system that you will learn about them in next parts of developer guide.
