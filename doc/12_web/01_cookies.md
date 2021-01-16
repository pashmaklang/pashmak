# Working with cookies
In the pashmak web system, you can access cookies with `$web_cookies` global variable.

For example:

```bash
web_init()

println($web_cookies)
```

output:

```
{'foo': 'bar', 'x': 'y'...}
```

The `$web_cookies` variable is a dictonary. for example:

```bash
web_init()

println($web_cookies['cookie_name'])
```

### Setting the cookies
You cannot directly change items in `$web_cookies` variable. for setting cookies, you should use `web_set_cookie()` function.

for example:

```bash
web_init()

web_set_cookie({'name': 'cookie_name', 'value': 'value of cookie'})

println($web_cookies)
```

You should pass a dictonar to this function and set the items. `name` is name of cookie and `value` is value of cookie.

Also you can set more options. for example `expire`, `path`, `domain`...(All of cookie general options are available).
