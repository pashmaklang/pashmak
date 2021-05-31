# Eval

you can run Pashmak code from string.

look at this example:

```bash
eval('println("hello world from string")')
```

output:

```
hello world from string
```

this code is ran from a string.

look at this example:

```bash
print('enter some code: ')
$code = read()

eval($code)
```

output:

```
enter some code: <input>mem 'hi\n'; print(^);
hi
```

the above code gets a string from user and runs that as pashmak code.
