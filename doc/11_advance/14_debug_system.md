# Debug system
Pashmak has a built-in debugging system. It lets you add a **breakpoint** to your code,
run code while debugging, and inspect variable values.

To start debugging, use the `debug()` function:

```bash
# enable debug mode; debugging will not work unless DEBUG is set to true
define('DEBUG', true)

$name = 'parsa'

# start debugging here
debug()

println $name
```

You will see something like this:

```
Debug started (None) at <file-name>:<line-number>
> ... enter your commands here
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

To end the debug session, enter `n`:

```
> n
```

Your program then continues:

```
hello new
```

(`$name` was changed to `new` during debugging.)

You can also provide a message for the debug session:

```bash
# ...
debug('some message')
# ...
```

Then you will see:

```
Debug started (some message) ...
```

You can call `debug()` several times:

```bash
define('DEBUG', true)

debug('before creating $name')

$name = 'parsa'

debug('after creating $name and before print')

println 'hello ' + $name

debug('after print')
```
