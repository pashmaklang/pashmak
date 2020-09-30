# Stdlib
`stdlib` is a very important and useful module.
this module make the pashmak syntax easy.

this module not need to be import because it will import automaticaly.

look at this example:

```bash
# print
print "hello world"; # INSTEAD OF `mem 'hello world'; out ^;`

# import
import 'somefile.pashm';
import '@hash'; # INSTEAD OF `mem '@hash'; include ^`

# exit
exit; # exits program
exit 2; # exits with exit code
# INSTEAD OF `return;` and `return 2;`

# py
py "print('hello world from python')"; # INSTEAD OF `mem "print('hello world from python')"; python ^`

# sys
sys 'ls /tmp'; # INSTEAD OF `mem 'ls /tmp'; system ^;`

# std.chdir
std.chdir "/tmp"; # INSTEAD OF `mem '/tmp'; chdir ^;`

# std.eval
std.eval 'mem "hi"\; out ^\;'; # INSTEAD OF `mem 'mem "hi"\; out ^\;'; eval ^`
```

this module includes some aliases to make the pashmak syntax better.

also look at this example:

```bash
print 'enter your name: ';
set $name; read $name;

print 'hello ' + $name + '\n';

```
