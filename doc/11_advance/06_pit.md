# Pit render engine
Pit is an engine for rendering Pashmak code embedded in HTML or other text formats (PIT means "Pashmak in Text").

It is similar to PHP's syntax for embedding code in another format, such as `Hello <?php echo $name; ?>`.

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
$ pashmak @pit myfile.html
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

This system can be used for web development.

You can also use it with any text format, not only HTML.

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
$ pashmak @pit /path/to/file.html
```

## Use as library
Also you can use this system as a library in your pashmak code.

Example:

```bash
import @pit

$output = pit.run_file('/path/to/file.html')
$output = pit.run('<code as string>')
```

The `run_file` function takes a file path, renders the file, and returns the output.
The `run` function takes code as a string, renders it, and returns the output.

You can also pass them a second argument, which must be a boolean. If it is `True`, the engine prints the output directly. If it is `False` (the default), Pit returns the output as a string.

for example:

```bash
import @pits

$output = pit.run_file('/path/to/file.html', True)
$output = pit.run('<code as string>', True)
```

## Using `{` and `}` characters inside code
The `{` and `}` characters are special in this system and are not printed as regular characters. To include them as regular characters, put a `\` before each one.

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
    while $i < 10
}<div>hello {{ $i }}</div>
{
    $i = $i + 1
    endwhile
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
    pit.include($__htmldir__ + '/bar.html') # include the bar.html
}

<h3>Good bye</h3>
```

##### `bar.html`:

```html
<div>I am bar</div>
```

When we run `foo.html`, the output is:

```html
<h1>Hello world</h1>

<div>I am bar</div>

<h3>Good bye</h3>
```

You can include other html files using `pit.include` function and pass file path to that.

You can also pass data when including a file. For example:

```html
{ pit.include('other.html', \{'key1': 'value1', 'key2': 'value2'\}) }
```

Then that data is accessible in `other.html` with `$htmldata` variable.

## Make executable scripts with Pit Engine format
You can write a script in this format, add a shebang, and make the file executable. For example:

```html
#!/usr/bin/pashmak @pit
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
