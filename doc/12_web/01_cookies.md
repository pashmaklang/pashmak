# Working with cookies
In the pashmak web system, you can access cookies with `$web.cookies` global variable.

For example:

```bash
import @web

web.init()

println($web.cookies)
```

output:

```
{'foo': 'bar', 'x': 'y'...}
```

The `$web.cookies` variable is a dictonary. for example:

```bash
import @web

web.init()

println($web.cookies['cookie_name'])
```

### Setting the cookies
You cannot directly change items in `$web.cookies` variable. for setting cookies, you should use `web.set_cookie()` function.

for example:

```bash
import @web

web.init()

web.set_cookie({
    'name': 'cookie_name',
    'value': 'value of cookie'
})

println($web.cookies)
```

You should pass a dictonar to this function and set the items. `name` is name of cookie and `value` is value of cookie.

Also you can set more options. for example `expire`, `path`, `domain`...(All of cookie general options are available).
