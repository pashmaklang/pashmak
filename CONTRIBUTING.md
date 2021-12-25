# Contributing
if you want to contribute to the Pashmak project, this contributing guide is helpful.

### run/build
to run program, do following steps:

```bash
cd /path/to/project/folder
./src/pashmak.py # this is Pashmak interpreter main executable file
```

also you can compile program with `pyinstaller`:

```bash
make all
make
```

then run built executable:

```bash
./dist/pashmak
```

### start contributing

to start contributing:
- fork this project
- clone your fork
- create a branch
- make changes and commit
- push your code
- send pull request

```bash
git clone <your-fork-repo-url>
cd pashmak
git branch some-name-for-branch master
git checkout some-name-for-branch
# make changes and commit
make all # after run this, if something changed, commit again
git push origin some-name-for-branch
```

and then make pull request from your branch to `master`

### Idea
if you haven't any idea for contributing, you can see [Issues](https://github.com/pashmaklang/pashmak/issues)

### Branch
Send **New/Change Features** to branch `master`(`master` is develop stage for next release).

Send **Bug Fixes** to branch `0.8` (older supported release).

([Read release process for more](doc/13_dev_guide/07_release_process.md)).

### Developer Guide
If you want to undrestand structure of Pashmak project source code, Read [Developer Guide](doc/13_dev_guide).

### Makefile scripts
this scripts are helpful for development:

##### make module
this command makes file `src/core/modules.py`.

this command loads Pashmak modules from `src/` folder and put them in `src/core/modules.py` file.

if you made changes in modules in `src/`'s `.pashm` files, run this command.

```bash
make module
```

For example, file `src/sys/path.pashm` will built as `sys.path` module(`import @sys.path`). and for example `src/os/__init__.pashm` will built as `os`(`import @os`).

##### make update-headers
this command updates all of `.py`, `.pashm` and `.pashmt` scripts copyright header in project. if you added a file to the project, run this command.

```bash
make update-headers
```

##### make test
this command runs tests

```bash
make test
```

##### make pylint
this command runs pylint on `src/` folder and saves pylint output to `pylint.out` file

```bash
make pylint
```

##### make all
this is very useful. this commands runs `module`, `update-headers`, `docs`, `test` scripts one by one and you don't need to run them manualy.

```bash
make all
```

##### make speed-test
This is a simple script that tests interpreter speed.

```bash
make speed-test
```

You can also run:

```bash
./src/pashmak.py scripts/speed-test.pashm
```

#### On windows
If you are developing on Windows, use `.\win-configure.bat` command instead of makefile scripts.

## Documentation
If you are adding/changing a feature, add/change documentation of that feature.

For example, if you are adding a new standard module, add documentation for that in `doc/10_modules/<x>.md`.

## Changelog
Write your changes into the `CHANGELOG.md` file(under the `next release` title).

for example:

```markdown
## next release

#### New Features
- List of new features
- Added x
- ...

#### Changes
- List of changes
- Changed x to y
- ...

#### Bug Fixes
- Fixed bug x
- ...
```

If you need to describe more information about a item in changelog, you can create a file directory
`doc/changelog/<version>/some-thing.md` and add a link to this file in `CHANGELOG.md`:

```markdown
- Fixed bug X ([read more](doc/changelog/<version>/some-thing.md))
```

## Testing
you can run Pashmak project tests via 5 ways:

```bash
make test
# OR
./tests/run.py
# OR
python3 ./tests/run.py
```

#### create new test
to create new test, you should create a file with `.pashmt` extension in `tests` folder. also you can create that in any subdirectory. for example `tests/foo/bar/test.pashmt` or `tests/hello.pashmt`, etc.

the strcuture of `.pashmt` files is so easy. test runner reads them and runs code and runs assertions on result of the code.

for example `tests/example/test_something.pashmt`

this is content of that:

```
--test--
This is a example test
--file--
# this is my code
print('hello world')
--output--
"hello world"
```

in above example, we are asserting output of that code is `hello world`.

syntax of this files is very easy.
you have to write `--<section-name>--` in a line and write value in next lines.

for example, `--test--` option sets a short description for the test.
and `--file--` set the code. and `--output--` asserts output.

totally, the above test runs `print("hello world")` code and asserts output of that code is `"hello world"`

if you adding a feature or changing feature, change/add test for that feature

#### Another test options
- `--vars--`: asserts variables
- `--mem--`: asserts mem value
- `--output--`: asserts program output
- `--cliargs--`: sets program command line arguments (list)
- `--stdin--`: sets program stdin arguments (list)
- `--exit-code--`: asserts program exit code
- `--with-error--`: asserts program has error. value is optional, but you can assert error type as value
- `--pyinit--`: this can be a python code to be ran before running test code
- `--skip--`: this option says that to test runner, if this was faild, ignore this and skip

example:

```
--test--
Example test
--file--
# this is my code
println('hello world')
$foo = 'bar'
$name = 'pashmak'
mem 'the mem'
exit 5

--output--
"hello world\n"

--vars--
{"foo": "bar", "name": "pashmak"}

--mem--
"the mem"

--exit-code--
5
```

REMEMBER, always put values in `--mem--`, `--output--` and... as python syntax!

for example, if you want to assert output is `hello world`, DO NOT WRITE THIS:

```
--output--
hello world
```

above test is wrong, but this is value:

```
--output--
"hello world"
```

actually, you have to write `"` and... assert values.

## Other notes
If you are adding/changing **Features**, please add/change **Documentation** and **Tests** for that Feature.

