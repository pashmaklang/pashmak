# Web Development with Pashmak
Pashmak is a general programming language. means that this language is not for a specific work and you can use it anywhere. But Pashmak has potential of web development. You can run pashmak at server to develop website backend.

## Get started
This is a very basic example:

```bash
import @web

web.init()

web.end_headers()

println('Hello world!')
```

Then, you can run this using `@serve` module:

```bash
$ pashmak @serve 8000
```

Now, you can go into http://localhost:8000/myfile.pashm (Write path of your script instead of `myfile.pashm`), and you will see `Hello world!` in the browser.

## Headers
The headers in HTTP are important things(You should now about them before reading this guide). In pashmak, for setting the headers, you should use `web.set_header($name, $value)` function. This function sets the header.

for example:

```bash
import @web

web.init()

web.set_header('Content-type', 'application/json')
web.set_header('Foo', 'Bar')
# ...

# surely call this function to end the headers
web.end_headers()
```

Now, you can go into http://localhost:8000/myfile.pashm (Write path of your script instead of `myfile.pashm`), and you will see `Hello world!` in the browser!

Remember that to call `web.init()` function in the first of your script. This function initializes the web environment.

## Status code
You can set status code of your HTTP response using `web.status($code)` function:

```bash
import @web

web.init()

web.status(404)

web.end_headers()
```

## Request Method & Post data
The HTTP request method is accessible using key `REQUEST_METHOD` in envvars:

```bash
import @web, @os

web.init()
web.end_headers()

if $os.env['REQUEST_METHOD'] == 'POST'
    println('The post')
elif $os.env['REQUEST_METHOD'] == 'GET'
    println('The get')
endif
```

Accessing the Request POST data in HTTP is very important. To get the post data body, you can use key `HTTP_POST_DATA` in the environment variables:

```bash
import @web, @os

web.init()
web.end_headers()

import @os # env vars are accessible in `os` module
if $os.env['REQUEST_METHOD'] == 'POST'
    # This key is only available when request method is POST
    println($os.env['HTTP_POST_DATA'])
endif
```

## Using Pit engine
You learned about Pashmak's Pit engine in the previous parts. You can use this in web:

```html
#!/usr/bin/pashmak @pit
{
web.init()
web.end_headers()

$name = 'parsa'
}
<h1>Hello {{ $name }}</h1>
```

Save the file with `.pashm.html` extension. for example: `hello.pashm.html`.

Now, run the server and go to http://localhost:8000/hello.pashm.html and you will see `Hello parsa` in `h1` tag.

REMEMBER to put `#!/usr/bin/pashmak @pit` shebang in the first of your file. This is important(Also do this if your are in windows or non-UNIX like OS).

## Webserver cli options
You can use `pashmak @serve --help` command to see the help:

```
Usage:   pashmak @serve <port>
         pashmak @serve <host> <port>
         pashmak @serve <host> <port> <directory>
         pashmak @serve <host> <port> <directory> <main-script: main file is request handler>
Example: pashmak @serve 8080
         pashmak @serve 0.0.0.0 8080
         pashmak @serve 0.0.0.0 8080 path/to/public/html
         pashmak @serve 0.0.0.0 8080 path/to/public/html path/to/public/html/server.pashm
```

## Request handler
When you serve a server in a directory, if request of user is `/some/dir/and/file.pashm`, webserver searches for `/some/dir/and/file.pashm` in that directory. But sometimes you want to set webserver to send All of requests to a specify file.

You can use the 4th argument for webserver cli:

```bash
$ pashmak @serve localhost 8080 . ./server.pashm
```

Now, all of requests will be send to `server.pashm` and youself can handle them by this script. for example, you can handle routing with this feature.
