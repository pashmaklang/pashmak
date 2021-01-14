# Web Development with Pashmak
Pashmak is a general programming language. means that this language is not for a specific work and you can use it anywhere. But Pashmak has potential of web development. You can run pashmak at server to develop website backend.

## Basics
This is a very basic example:

```bash
web_init()

println('Hello world!')
```

Then, you can run this using `@webserver` module:

```bash
$ pashmak @webserver 8000
```

## Headers
The headers in HTTP are important things(You should now about them before reading this guide). In pashmak, for setting the headers, you should use `web_set_header($name, $value)` function. This function sets the header.

for example:

```bash
web_init()

web_set_header('Content-type', 'application/json')
web_set_header('Foo', 'Bar')
# ...
```

Now, you can go into http://localhost:8000/myfile.pashm (Write path of your script instead of `myfile.pashm`), and you will see `Hello world!` in the browser!

Remember that to call `web_init()` function in the first of your script. This function initializes the web environment.

## Status code
You can set status code of your HTTP response using `web_status($code)` function:

```bash
web_init()

web_status(404)
```

## Request Method & Post data
The HTTP request method is accessible using key `REQUEST_METHOD` in envvars:

```bash
web_init()

if $os.env['REQUEST_METHOD'] == 'POST'
    println('The post')
elif $os.env['REQUEST_METHOD'] == 'GET'
    println('The get')
endif
```

Accessing the Request POST data in HTTP is very important. To get the post data body, you can use key `HTTP_POST_DATA` in the environment variables:

```bash
web_init()

import @os # env vars are accessible in `os` module
if $os.env['REQUEST_METHOD'] == 'POST'
    # This key is only available when request method is POST
    println($os.env['HTTP_POST_DATA'])
endif
```

## Using T-Engine
You learned about Pashmak's T-Engine in the previous parts. You can use this in web:

```html
#!/usr/bin/pashmak @tengine
{
web_init()

$name = 'parsa'
}
<h1>Hello {{ $name }}</h1>
```

Save the file with `.pashm.html` extension. for example: `hello.pashm.html`.

Now, run the server and go to http://localhost:8000/hello.pashm.html and you will see `Hello parsa` in `h1` tag.

REMEMBER to put `#!/usr/bin/pashmak @tengine` shebang in the first of your file. This is important.
