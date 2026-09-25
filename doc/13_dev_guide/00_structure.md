# Structure of Pashmak Project source code

The Pashmak project has this directory structure:

- `src/`: the main source code
- `tests/`: the test suite ([read about the testing system](../../CONTRIBUTING.md))
- `doc/`: Documentation

The `src/` directory contains several subdirectories. The **interpreter core** is in `src/core/`; the other directories contain built-in modules, which are covered in the next section.

The `src/pashmak.py` file is the Pashmak interpreter's main command-line entry point.

Other project directories include:

- `scripts/`: project automation scripts
- `examples/`: Pashmak examples

The `doc/` directory contains the documentation, arranged as follows:

```
doc/
    00_first_part/
        README.md: index
        00_a.md
        01_b.md
        ...
    01_second_part/
        ...
```
