# The Pashmak Jit Compiler
The **JIT** (or **just-in-time**) compiler caches and compresses code to speed up the interpreter.

This system compresses scripts and saves them in the `__pashmam__` directory. When a file is run again, the JIT loads the compressed content from the cache.

You can find the `__pashmam__` directory alongside your scripts. It contains cached code.

Also, make sure to add the `__pashmam__` directory to your `.gitignore` file.

To disable the JIT, set the `PASHMAK_DISABLE_JIT` environment variable to `1` when running the Pashmak interpreter. For example:

```bash
$ PASHMAK_DISABLE_JIT=1 pashmak somefile.pashm
```
