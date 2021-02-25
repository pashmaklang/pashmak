# Debug system
Pashmak has a builtin debug system. This system helps you to put **Break point** at your code
and run code inside your code or see value of variables while debuging.

For debuging, you should use function `debug()`:

```bash
# this line enables the debug mode
# if you dont define `DEBUG` to `true`, debug will not work
define('DEBUG', true)

$name = 'parsa'

# start debuging here
debug()

println $name
```

You will see something like this:

```
Debug started (None) at <file-name>:<line-number>
> ... enter you commands here
```

For example:

```
> println $name
parsa
```

Or you can change the value of `$name`:

```
> $name = 'new'
```

For ending the debug, you should enter `n`:

```
> n
```

then, your program continues:

```
hello new
```

(`$name` is changed to `new` at debug).

Also you can set a helper message for your debug:

```bash
# ...
debug('some message')
# ...
```

then you will see:

```
Debug started (some message) ...
```

Also you can call `debug()` several times:

```bash
define('DEBUG', true)

debug('before creating $name')

$name = 'parsa'

debug('after creating $name and before print')

println 'hello ' + $name

debug('after print')
```
