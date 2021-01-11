# T-engine render Engine
The tengine is a engine to render pashmak code inside the Html/Text code(T-Engine: Text engine).

T-Engine is something like PHP's structure to write the code inside other formats(for example `Hello <?php echo $name; ?>`).

For example:

```html
{
    $name = 'parsa'
}
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    hello {{ $name }}
    { println('hello world') }
</body>
</html>
```

then we can render this code using this command:

```bash
$ pashmak @tengine myfile.html
```

output:

```html
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    hello parsa
    hello world
</body>
</html>
```

this system can be used in web development.

Also you can use it in every text format, not only html.

for example:

```
{ $name = 'someone' }
hello {= $name }
```

output:

```
hello someone
```

## Usage
Usage of this system is very easy.

We have 2 statements:

- `{ code }`: runs a pashmak code between `{ }`
- `{{ <value-or-variable> }}` OR `{= <value-or-variable> }`: prints the value of between `{{ }}` or `{=  }`

for example:

```html
{
    $somevar = 'somevalue'

    func somefunc
        return 'hello somefunc'
    endfunc
}
<h1>Hello {= $somevar }</h1>
<h2>{= somefunc() }</h2>
```

output:

```html

<h1>Hello somevalue</h1>
<h2>hello somefunc</h2>
```

You only need to run:

```bash
$ pashmak @tengine /path/to/file.html
```

## Use as library
Also you can use this system as a library in your pashmak code.

Example:

```bash
import @tengine

$output = tengine.run_file('/path/to/file.html')
$output = tengine.run('<code as string>')
```

The `run_file` function gets file path and runs that and returns the output.
`run` function gets code as string and runs that and returns the output.

Also you can pass a **Second Argument** to them. This argument should be a boolean. if this is `True`, this engine runs code directly and shows the output. but if this is `False`(default is false), tengine runs the code and returns output as string.

for example:

```bash
import @tengine

$output = tengine.run_file('/path/to/file.html', True)
$output = tengine.run('<code as string>', True)
```

## Using `{` and `}` characters inside code
The `{` and `}` chars are special chars that this system do not prints them like normal characters. If you want to use them as a normal character, you should put a `\` before them.

For example:

```html
<div>{ println('the \{\}') }</div>
```

output:

```html
<div>the {}</div>
```

## Using If and loop statements
You can use `if` and `loop` in this system.

for example:

```html
{ if $age > 18 }
<div class="alert alert-success">
    Welcome!
</div>
{ else }
<div class="alert alert-danger">
    You cannot access to this Site! :))
</div>
{ endif }
```

loops:

```html
{
    $i = 0
    section loop1
}<div>hello {{ $i }}</div>
{
    $i = $i + 1
    mem $i < 10; gotoif loop1
}
```

output:

```html
<div>hello 0</div>
<div>hello 1</div>
<div>hello 2</div>
<div>hello 3</div>
<div>hello 4</div>
<div>hello 5</div>
<div>hello 6</div>
<div>hello 7</div>
<div>hello 8</div>
<div>hello 9</div>
```

## `$__htmldir__` and `$__htmlfile__` variables

The `$__htmlfile__` variable contains the current file path.
The `$__htmldir__` contains the current file parent directory path.

## include other files

You can include other html files in your file.

for example, we have `foo.html` and `bar.html`:

##### `foo.html`:

```html
<h1>Hello world</h1>

{
    tengine.include($__htmldir__ + '/bar.html') # include the bar.html
}

<h3>Good bye</h3>
```

##### `bar.html`:

```html
<div>I am bar</div>
```

when we run `foo.html`, output is this:

```html
<h1>Hello world</h1>

<div>I am bar</div>

<h3>Good bye</h3>
```

You can include other html files using `tengine.include` function and pass file path to that.

Also you can send the data while including a file. for example:

```html
{ tengine.include('other.html', \{'key1': 'value1', 'key2': 'value2'\}) }
```

Then that data is accessible in `other.html` with `$htmldata` variable.

## Make executable scripts with T-Engine format
You can write your script and add a shebang for this and make it executable file. For example:

```html
#!/usr/bin/pashmak @tengine
{$name = 'parsa'}
<h1>Hello {= $name }</h1>
```

Then:

```bash
$ chmod +x myfile.html
```

Now you can run it:

```bash
$ ./myfile.html
```

output:

```html
<h1>Hello parsa</h1>
```
