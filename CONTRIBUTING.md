# Contributing
if you want to contribute to the pashmak project, this contributing guide is helpful.

### Branch
alwasy send your merge requests to `master` branch.

### Makefile scripts
this scripts are helpful for development:

###### make docs
this command loads documentation from `doc/` folder and mix them in `README.md`

```bash
make docs
```

file `doc/README.HEADER.md` will put in the first of `README.md`

another files in `doc/` will sort and append one by one to `README.md`

if you maked some changes in documentation, run this command to mix change into `README.md`

###### make module
this command makes file `src/core/modules.py`.

this command loads pashmak modules from `modules/` folder and put them in `src/core/modules.py` file.

if you maked changes in modules in `modules/`, run this command.

```bash
make module
```

###### make update-headers
this command updates all of `.py` scripts copyright header in project. if you added a file to the project, run this command.

```bash
make update-headers
```

###### make test
this command runs tests

```bash
make test
```

###### make all
this is very useful. this commands runs `module`, `update-headers`, `docs`, `test` scripts one by one and you don't need to run them manualy.

```bash
make all
```

## Testing





