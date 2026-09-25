# Working with cookies
In the pashmak web system, you can access cookies with `$web.cookies` global variable.

For example:

```bash
import @web

web.init()
web.end_headers()

println($web.cookies)
```

output:

```
{'foo': 'bar', 'x': 'y'...}
```

The `$web.cookies` variable is a dictionary. For example:

```bash
import @web

web.init()
web.end_headers()

println($web.cookies['cookie_name'])
```

### Setting the cookies
You cannot change items in the `$web.cookies` variable directly. To set cookies, use the `web.set_cookie()` function.

For example:

```bash
import @web

web.init()

web.set_cookie({
    'name': 'cookie_name',
    'value': 'value of cookie'
})

# remember to set the cookie BEFORE ending the headers
web.end_headers()

println($web.cookies)
```

Pass a dictionary to this function with the cookie options. `name` is the cookie name, and `value` is its value.

You can also set other options, such as `expire`, `path`, and `domain`. All standard cookie options are available.
