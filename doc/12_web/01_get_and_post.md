# GET and POST data
You can access GET and POST data through the `$web.get` and `$web.post` variables. They are dictionaries.

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
    "name": "parsa"
}
```

You can access the keys like this:

```bash
# ...

println $web.get['name']
```

The `$web.post` variable works like `$web.get`:

```bash
# ...

println $web.post['some_key']
```

(If the request method is not POST, `$web.post` is an empty dictionary by default.)
