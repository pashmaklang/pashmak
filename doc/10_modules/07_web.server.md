# Module web.server
This module is for serving HTTP. Core of this modules are using python's `http`.

## Simple usage
Example:

```bash
# import the module
import @web.server

# create a new webserver
$server = web.server.WebServer('<host>', <port>)
# for example
$server = web.server.WebServer('localhost', 8000)

# then, you need to set a handler for GET and POST requests
# you should declare a function and pass it to $server object
# for example:
func get_handler($handler)
    $handler->send_response(200)
    $handler->send_header("Content-type", "text/html")
    $handler->end_headers()

    $handler->wfile->write(bytes('Hello World!', "utf-8"))
endfunc

# pass the function to `set_get`
$server->set_get(get_handler)

# start the server
$server->serve()
```

Then, if you see the http://localhost:8000, you can see `Hello World!` as response.

Also you can use `set_post` to set handler for POST requests:

```bash
func post_handler($handler)
    # ...
endfunc

$server->set_post(post_handler)
```

### More features
All of the `$handler` object is handled by python `http` module. This object is a instance from python's `http.server.BaseHTTPRequestHandler` class. [Read the python documentation to learn more methods and properties on the handler](https://docs.python.org/3/library/http.server.html).
