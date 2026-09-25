# Working with files
Working with files in Pashmak is very easy.

We have 4 main operations on files: open, read, write and close.

Look at this example for reading the content of a file:

```bash
$my_file = open('/path/to/some/file.txt', 'r')
println($my_file->read())
$my_file->close()
```

In the above example, we opened our file, read the content and then closed it.

In `$file->read()`, the `read` method reads the content of the file and returns it.

You can put that in a variable:

```bash
$content = $file->read()
```

To write the content of a file, we can use the `write` method:

```bash
$my_file = open('/path/to/some/file.txt', 'w')
$my_file->write('new content')
$my_file->close()
```

The second argument for opening a file is the type of opening. `r` means read and `w` means write.

Also you can use the `fopen` function instead of `open`. There is no difference; it is just an alias.

The file objects in Pashmak are handled by Python, so you can use all of the Python file features in Pashmak just like in Python.
