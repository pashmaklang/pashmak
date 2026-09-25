# Module web.server
This module provides an HTTP server. It uses Python's `http` module internally.

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

Visit `http://localhost:8000` to see `Hello World!` in the response.

You can also use `set_post` to set a handler for POST requests:

```bash
func post_handler($handler)
    # ...
endfunc

$server->set_post(post_handler)
```

### More features
The `$handler` object is provided by Python's `http` module. It is an instance of Python's `http.server.BaseHTTPRequestHandler` class. [Read the Python documentation to learn more about its methods and properties](https://docs.python.org/3/library/http.server.html).
