# Working with files
working with files in pashmak is so easy.

we have 4 main operations on files: Open, Read, Write, Close

look at this example for reading content of a file:

```bash
$my_file = open('/path/to/some/file.txt', 'r')
println $my_file->read()
$my_file->close()
```

In above example, we opened our file, read content and then we closed that.

the `$file->read()`, the `read` method reads content of file and returns that.

you can put that in a variable:

```bash
$content = $file->read()
```

to write content of a file, we can use `write` method:

```bash
$my_file = open('/path/to/some/file.txt', 'w')
$my_file->write('new content')
$my_file->close()
```

The second argument for opening file is type of opening. `r` means Read and `w` means write.

The file objects in pashmak are handled by python you can use all of python file features in pashmak like python.
