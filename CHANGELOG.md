# Pashmak Changelog

## 1.6 (2020-10-11)

#### Fixed
- some clean up and optimizations in online interpreter

#### Feature
- added syntax `$var = ^` to copy `mem` value to variables without using `copy` command and with better syntax
- showing total assertions in testing system after running tests

## 1.5 (2020-10-10)

#### Feature
- added `$pashmakinfo` global variable to access pashmak interpreter info in code
- added online-interpreter to source code

## 1.4 (2020-10-10)

#### Fixed
- optimize and clean up code

#### Feature
- big change in variable syntax

## v1.3.1 (2020-10-09)

#### Fixed
- fixed include system file path bug [(f056d194)](https://github.com/parsampsh/pashmak/commit/f056d19451adf32e13ab80901de7114166499cc8)
- clean up and optimize code

## v1.3 (2020-10-09)

#### Fixed
- fixed section system bug while including scripts [(fb781218)](https://github.com/parsampsh/pashmak/commit/fb7812187c063654bd0e4aab27de978b6151867b)
- fixed `include` filepath bug [(141b32df)](https://github.com/parsampsh/pashmak/commit/141b32dfccb42558b4ad8ce6d25612e90c6a5681)
- some optimizations in code

#### Feature
- sync variable system with namespace system [(e9f48a17)](https://github.com/parsampsh/pashmak/commit/e9f48a17646873d3ccaa574e6bf11911908ea3c6)
- make better error rendering [(0115448a)](https://github.com/parsampsh/pashmak/commit/0115448a95b02621d2e51009e41a18b268bd7729)

## v1.2.3 (2020-10-08)

#### Fixed
- fixed section bug after include
- some changes in cli error showing

## v1.2.2 (2020-10-07)

#### Feature
- add Table of contents to documentation and clean up

## v1.2.1 (2020-10-07)

#### Fixed
- clean up documentation

## v1.2 (2020-10-07)

#### Fixed
- big clean up in documentation
- fix `typeof` operation bug

## v1.1 (2020-10-06)

#### Feature
- added operation `use` for namespace system

## v1.0.1 (2020-10-06)

#### Fixed
- fixed namespace-in-namespace bug
