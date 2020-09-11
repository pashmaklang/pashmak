# Work with files
to work with files in pashmak, is simple operations

### read a file
```bash
mem '/path/to/file.txt'; fread ^;
set %content; copy %content;
mem 'content of file is: ' + %content; out ^;
```

the content of `/path/to/file.txt'` is:
```
hello world. this is my content
by
```

output of the program:

```
content of file is: hello world. this is my content
by
```

you can put a variable instead ^ in `fread ^` as path of file to read

after fread command, content of readed file will put in the mem and you can access that

### write on file
```bash
set %filepath; mem '/path/to/file.txt'; copy %filepath;

mem 'content of file';
fwrite %filepath ^; # write mem (^) on the %filepath (/path/to/file.txt)
```
