# Contributing
If you want to contribute to the Pashmak project, this contributing guide is helpful.

### Run/build
To run the program, do the following steps:

```bash
cd /path/to/project/folder
./src/pashmak.py # this is Pashmak interpreter main executable file
```

Also you can compile the program with `pyinstaller`:

```bash
make all
make
```

Then run the built executable:

```bash
./dist/pashmak
```

### Start contributing

To start contributing:
- Fork this project
- Clone your fork
- Create a branch
- Make changes and commit
- Push your code
- Send a pull request

```bash
git clone <your-fork-repo-url>
cd pashmak
git branch some-name-for-branch master
git checkout some-name-for-branch
# make changes and commit
make all # after run this, if something changed, commit again
git push origin some-name-for-branch
```

And then make a pull request from your branch to `master`

### Idea
If you don't have any idea for contributing, you can look at the [Issues](https://github.com/pashmaklang/pashmak/issues)

### Branch
Send **New/Changed Features** to the branch `master` (`master` is the development stage for the next release).

Send **Bug Fixes** to the branch `0.8` (the older supported release).

([Read the release process for more](doc/13_dev_guide/07_release_process.md)).

### Developer Guide
If you want to understand the structure of the Pashmak project source code, read [Developer Guide](doc/13_dev_guide).

### Makefile scripts
These scripts are helpful for development:

##### make module
This command makes the file `src/core/modules.py`.

This command loads the Pashmak modules from the `src/` folder and puts them in the `src/core/modules.py` file.

If you made changes to the modules in `src/`'s `.pashm` files, run this command.

```bash
make module
```

For example, the file `src/sys/path.pashm` will be built as the `sys.path` module (`import @sys.path`). And, for example, `src/os/__init__.pashm` will be built as `os` (`import @os`).

##### make update-headers
This command updates the copyright header of all `.py`, `.pashm` and `.pashmt` scripts in the project. If you added a file to the project, run this command.

```bash
make update-headers
```

##### make test
This command runs the tests.

```bash
make test
```

##### make pylint
This command runs pylint on the `src/` folder and saves the pylint output to the `pylint.out` file.

```bash
make pylint
```

##### make all
This is very useful. This command runs the `module`, `update-headers`, `docs` and `test` scripts one by one, and you don't need to run them manually.

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

#### On Windows
If you are developing on Windows, use `.\win-configure.bat` command instead of makefile scripts.

## Documentation
If you are adding/changing a feature, add/change documentation of that feature.

For example, if you are adding a new standard module, add documentation for that in `doc/10_modules/<x>.md`.

## Changelog
Write your changes into the `CHANGELOG.md` file (under the `next release` title).

For example:

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

If you need to describe more information about an item in the changelog, you can create a file
`doc/changelog/<version>/some-thing.md` and add a link to this file in `CHANGELOG.md`:

```markdown
- Fixed bug X ([read more](doc/changelog/<version>/some-thing.md))
```

## Testing
You can run the Pashmak project tests in 3 ways:

```bash
make test
# OR
./tests/run.py
# OR
python3 ./tests/run.py
```

#### Create a new test
To create a new test, you should create a file with the `.pashmt` extension in the `tests` folder. Also you can create it in any subdirectory, for example `tests/foo/bar/test.pashmt` or `tests/hello.pashmt`, etc.

The structure of `.pashmt` files is very easy. The test runner reads them, runs the code and runs assertions on the result of the code.

For example, `tests/example/test_something.pashmt`.

This is its content:

```
--test--
This is an example test
--file--
# this is my code
print('hello world')
--output--
"hello world"
```

In the above example, we are asserting that the output of that code is `hello world`.

The syntax of these files is very easy.
You have to write `--<section-name>--` on a line and write the value on the next lines.

For example, the `--test--` option sets a short description for the test.
And `--file--` sets the code. And `--output--` asserts the output.

In total, the above test runs the `print("hello world")` code and asserts that the output of that code is `"hello world"`.

If you are adding a feature or changing a feature, change/add a test for that feature.

#### Other test options
- `--vars--`: asserts the variables
- `--mem--`: asserts the mem value
- `--output--`: asserts the program output
- `--cliargs--`: sets the program command line arguments (list)
- `--stdin--`: sets the program stdin arguments (list)
- `--exit-code--`: asserts the program exit code
- `--with-error--`: asserts that the program has an error. The value is optional, but you can assert the error type as the value
- `--pyinit--`: this can be Python code to be run before running the test code
- `--skip--`: this option tells the test runner that if this test fails, it should ignore it and skip

Example:

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

REMEMBER, always write the values in `--mem--`, `--output--`, etc. using Python syntax!

For example, if you want to assert that the output is `hello world`, do not write this:

```
--output--
hello world
```

The above test is wrong, but this is correct:

```
--output--
"hello world"
```

Actually, you have to write the `"` characters and assert the values.

## Other notes
If you are adding/changing **Features**, please add/change **Documentation** and **Tests** for that Feature.

