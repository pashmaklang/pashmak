# Contributing
if you want to contribute to the pashmak project, this contributing guide is helpful.

### run/build
to run program, do following steps:

```bash
cd /path/to/project/folder
./src/pashmak.py # this is pashmak interpreter main executable file
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
you can run pashmak project tests via 5 ways:

```bash
make test
# OR
./scripts.py test
# OR
python3 scripts.py test
# OR
./tests/run.py
# OR
python3 ./tests/run.py
```

#### create new test
to create new test, run this command:

```bash
python3 scripts.py make-test test_something
```

alwasy put `test_` before name of test.

now the test script is created in `tests/items/test_something.py`

this is content of that:

```python
from TestCore import TestCore

class test_something(TestCore):
    def run(self):
        self.assert_true(True)
```

you can do your test in `run` function in `test_something` class.

if you adding a feature or changing feature, change/add test for that feature

#### test core functions
- assert_true(Value): gets a value and asserts that is True
- assert_false(Value): gets a value and asserts that is False
- assert_equals(first, last): gets two value and asserts they are equals
- assert_not_equals(first, last): gets two value and asserts they are NOT equals
- run_script(code): gets a code and run that then returns program result
- run_without_error(code): gets a code and run that then returns program result and auto assert program has not error
- assert_vars(program_result, vars): gets a program result and asserts variables equals `vars`
- assert_mem(program_result, mem): gets a program result and asserts mem equals `mem`
- assert_output(program_result, output): gets a program result and asserts output equals `output`
- assert_exit_code(program_result, exit_code): gets a program result and asserts exit code equals `exit_code`
- assert_has_error(program_result): gets a program result and asserts program has error
- assert_has_not_error(program_result): gets a program result and asserts program has NOT error
- dump(object): gets a object and dumps that object


example:

```python
from TestCore import TestCore

class test_something(TestCore):
    def run(self):
        self.assert_output(self.run_without_error('''
        mem 'hello world'; out ^;
        ''') , 'hello world')

        # my code prints `hello world` and i'm asserting the output is `hello world`
```
