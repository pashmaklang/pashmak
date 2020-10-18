# Pashmak Changelog

## next release

#### Changed
- add new hash algos to hash module [(6a3ef2b3)](https://github.com/parsampsh/pashmak/commit/6a3ef2b37e4c32a7b41e874684a73d368062c79c)
- some optimizations

## 1.10 (2020-10-16)

#### Added
- added function argument variable syntax [(97bcaafa)](https://github.com/parsampsh/pashmak/commit/97bcaafaa547e52250896f9cb7edd1b67f3acff2)

## 1.9 (2020-10-15)

#### Added
- added new syntax for variable mem assigning like `$variable = ^ function_name 'arguments';` [(e10632cd)](https://github.com/parsampsh/pashmak/commit/e10632cd19666611001e38985e1536bb35c49184)

## 1.8.2 (2020-10-14)

#### Changed
- optimized program core code [(46f1ec48)](https://github.com/parsampsh/pashmak/commit/46f1ec48cb87e8658061173dd49c2ffc2e32b820)
- renamed function `continue` to `while` for make loop in stdlib [(a2c0cff0)](https://github.com/parsampsh/pashmak/commit/a2c0cff0d25695da8376068355c91ae0e1baac60)

## 1.8.1 (2020-10-13)

#### Fixed
- fixed file module `file.close` function bug [(a5b801ea)](https://github.com/parsampsh/pashmak/commit/a5b801ea8e8c27ab471a098d425c2996efda1740)
- fixed file module `file.read` function bug [(101edd2c)](https://github.com/parsampsh/pashmak/commit/101edd2c39404b11550c4390268cc9bc1502b520)

## 1.8 (2020-10-12)

#### Changed
- changed document building directory structure [(311ff15c)](https://github.com/parsampsh/pashmak/commit/311ff15cada48af17dd869bcd5d0d6ef013a12d0)
- changed online interpreter code textarea selection style [(56d0eb01)](https://github.com/parsampsh/pashmak/commit/56d0eb01f18e694ffe47d1b43540b7ded009397c)

#### Added
- added `loop` and `continue` functions to stdlib [(af8a4c2e)](https://github.com/parsampsh/pashmak/commit/af8a4c2e6367ffe56d1970b21f79315d403ddce0)

## 1.7.1 (2020-10-11)

#### Fixed
- fixed pashmak cli `--version` and `--info` options exit code bug [(95d9d0d6)](https://github.com/parsampsh/pashmak/commit/95d9d0d6c3a51b54a5a587fb73a1b2134423e715)

## 1.7 (2020-10-11)

#### Added
- added function `println` to stdlib [(8ebb4c8e)](https://github.com/parsampsh/pashmak/commit/8ebb4c8e31692d0e74e0d1b25ab4ead77db6d70c)

#### Fixed
- fixed non-stop code bug and added timeout in online interpreter [(941a1467)](https://github.com/parsampsh/pashmak/commit/941a1467c3c21bc124a72018e0ea355e751ab903)
- fixed error rendering bootstrap index calculation bug [(fa5d54d8)](https://github.com/parsampsh/pashmak/commit/fa5d54d8f4ac662253cd918ef9d9f039d66758c9)

## 1.6 (2020-10-11)

#### Changed
- some clean up and optimizations in online interpreter

#### Added
- added syntax `$var = ^` to copy `mem` value to variables without using `copy` command and with better syntax
- showing total assertions in testing system after running tests

## 1.5 (2020-10-10)

#### Added
- added `$pashmakinfo` global variable to access pashmak interpreter info in code
- added online-interpreter to source code

## 1.4 (2020-10-10)

#### Changed
- big change in variable syntax
- optimize and clean up code

## v1.3.1 (2020-10-09)

#### Fixed
- fixed include system file path bug [(f056d194)](https://github.com/parsampsh/pashmak/commit/f056d19451adf32e13ab80901de7114166499cc8)
- clean up and optimize code

## v1.3 (2020-10-09)

#### Fixed
- fixed section system bug while including scripts [(fb781218)](https://github.com/parsampsh/pashmak/commit/fb7812187c063654bd0e4aab27de978b6151867b)
- fixed `include` filepath bug [(141b32df)](https://github.com/parsampsh/pashmak/commit/141b32dfccb42558b4ad8ce6d25612e90c6a5681)
- some optimizations in code

#### Changed
- sync variable system with namespace system [(e9f48a17)](https://github.com/parsampsh/pashmak/commit/e9f48a17646873d3ccaa574e6bf11911908ea3c6)
- make better error rendering [(0115448a)](https://github.com/parsampsh/pashmak/commit/0115448a95b02621d2e51009e41a18b268bd7729)

## v1.2.3 (2020-10-08)

#### Fixed
- fixed section bug after include

#### Changed
- some changes in cli error showing

## v1.2.2 (2020-10-07)

#### Added
- added Table of contents to documentation and clean up

## v1.2.1 (2020-10-07)

#### Changed
- clean up documentation

## v1.2 (2020-10-07)

#### Fixed
- fix `typeof` operation bug

#### Changed
- big clean up in documentation

## v1.1 (2020-10-06)

#### Added
- added operation `use` for namespace system

## v1.0.1 (2020-10-06)

#### Fixed
- fixed namespace-in-namespace bug
