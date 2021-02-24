# Interpreter Core Structure
Here, we explore in structure of interpreter Core.

## Interpreter Flow
The main CLI entry point of interpreter is `src/pashmak.py`.
This script gets the file name that user want to run. Then, loads content of this file, parses the code, and then gives the parsed code to class `Program` in `src/core/program.py`. This class is the main executor of the Pashmak.

##### NOTE: actually, `src/pashmak.py` uses `Jit` to load and parse the file, but you learn about it in the next parts.

The parser, gets the code as string. Splits the lines by `\n` and `;`(using new line and `;` for seprating operations is not different). Then, handles mutliline syntax and mixes that operations writen in mutliple lines in one line. Then, gives the lines one by one to the lexer(`src/core/lexer.py`'s `parse_op` function). Lexer splits some parts of the code and returns a `dict`. Then, parser makes ready a list from `dict`s. Also does something else on the output list(for example, converts `if..elif..else` statements to `label` system).

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
Frame system is very very important thing. This system is related to importing other scripts or calling functions. for example, this is my Pashmak code:

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

This is the frame system: When a function is called, a new frame will be created and the body of the function will be runed in the new frame, when this frame was finished, program backs to run previous frame.

Also frames help to isolate variables, used namespaces, etc.
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

When program is running code line by line, if there is a function call, creates a new frame and starts running new frame. when the new frame running was finished, backs to running previous frame.

Structure of `self.frames` variable is a `list[dict]`.

There is lot of more notes about this system that you will learn about them in next parts of developer guide.
