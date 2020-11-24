# Work with files
there is two operations for working with files in pashmak: `fread`, `fwrite`

### read a file

```bash
mem '/path/to/file.txt'; fread ^
$content = ^
print 'content of file is: ' + $content
```

the content of `/path/to/file.txt'` is:

```
hello world. this is my content
bye
```

output of the program:

```
content of file is: hello world. this is my content
bye
```

you can put a variable instead `^` in `fread ^` as path of file to read

after fread command, content of readed file will put in the mem and you can access that

### write on file
```bash
$filepath = '/path/to/file.txt'

mem 'content of file'
fwrite $filepath ^ # write mem (^) on the $filepath (/path/to/file.txt)
```

the `fwrite` operation gets two argument: file path and new content of file

you will learn easier work with files in [File general module](#file-module) section.
