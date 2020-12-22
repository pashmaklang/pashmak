# The Pashmak Jit Compiler
The **Jit** or **Just in time** compiler, is a system to cache the code and compress that to speed up the interpreter.

this system, compresses the content of scripts and saves them to `__pashmam__` directory. then, when file is runed again, jit system loads compressed content from that cache.

you can see `__pashmam__` directory alongside your scripts. this directory contains cached codes.

Also, make sure to add `__pashmam__` file to your **gitignore**.
