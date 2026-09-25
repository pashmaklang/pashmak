# Web Development with Pashmak
Pashmak is a general-purpose programming language that can be used for many kinds of work, including web development. You can run Pashmak on a server to build a website backend.

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

Visit `http://localhost:8000/myfile.pashm` (replacing `myfile.pashm` with the path to your script) to see `Hello world!` in the browser.

## Headers
HTTP headers are important; you should understand them before reading this guide. In Pashmak, use the `web.set_header($name, $value)` function to set a header.

For example:

```bash
import @web

web.init()

web.set_header('Content-type', 'application/json')
web.set_header('Foo', 'Bar')
# ...

# surely call this function to end the headers
web.end_headers()
```

Visit `http://localhost:8000/myfile.pashm` (replacing `myfile.pashm` with the path to your script) to view the response in a browser.

Remember to call `web.init()` at the start of your script. This function initializes the web environment.

## Status code
You can set status code of your HTTP response using `web.status($code)` function:

```bash
import @web

web.init()

web.status(404)

web.end_headers()
```

## Request Method
The HTTP request method is available under the `REQUEST_METHOD` key in the environment variables:

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

## Using Pit engine
You can also use Pashmak's Pit engine for web development:

```html
#!/usr/bin/pashmak @pit
{
web.init()
web.end_headers()

$name = 'parsa'
}
<h1>Hello {{ $name }}</h1>
```

Save the file with `.pashm.html` extension. For example: `hello.pashm.html`.

Now, run the server and go to http://localhost:8000/hello.pashm.html and you will see `Hello parsa` in `h1` tag.

Put the `#!/usr/bin/pashmak @pit` shebang at the start of your file. This is also required on Windows and other non-Unix-like systems.

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
When you serve a server in a directory, if request of user is `/some/dir/and/file.pashm`, webserver searches for `/some/dir/and/file.pashm` in that directory. But sometimes you want to set webserver to send all of requests to a specific file.

You can use the fourth argument to the web server command:

```bash
$ pashmak @serve localhost 8080 . ./server.pashm
```

Now all requests are sent to `server.pashm`, where you can handle them yourself. For example, you can use this feature to handle routing.
