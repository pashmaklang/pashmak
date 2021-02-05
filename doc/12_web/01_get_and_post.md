# GET and POST data
You can access to the GET and POSt data using `$web.get` and `$web.post` variables. they are dictionary.

For example, if you open `/app.pashm?foo=bar&name=parsa`, and print content of `$web.get`:

```bash
import @web
web.init()
web.end_headers()

var_dump($web.get)
```

You will see:

```json
{
    "foo": "bar",
    "name": "pasa"
}
```

Means you can access the keys like this:

```bash
# ...

println $web.get['name']
```

Also the `$web.post` is even like `$web.get`:

```bash
# ...

println $web.post['some_key']
```

(If the request method is not POST, `$web.post` is a empty dictionary by default).
