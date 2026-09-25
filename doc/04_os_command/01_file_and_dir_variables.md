# `$__file__` and `$__dir__` variables
The `$__file__` and `$__dir__` variables are two variables that contain the script's own file path and directory path.

For example, if you run a script at `/home/parsa/myscript.pashm` with this content:

```bash
println($__file__)
println($__dir__)
```

The output is:

```
/home/parsa/myscript.pashm
/home/parsa
```

The `$__file__` variable contains the file path of the currently running script.

The `$__dir__` variable contains the directory path of the currently running script.
