# Session system
A session is data stored on the server, similar to cookies but kept on the server side.
This system allows you to save some variables in session with a user.

In general, the server creates a strong, random ID, sends it to the client as a cookie (`PASHMAK_SESSION`),
and stores the ID on the server.

When the browser sends requests to the server, the server checks that cookie. If it exists and is valid,
the server loads the data saved for that ID into memory (`$web.session`).

## Basic usage
Here is a basic example:

```bash
import @web

web.init()

# This function starts the session system
web.start_session()

# start the session before ending headers
# because cookie `PASHMAK_SESSION` should be set in this step
# and cookies can be set before ending the headers
web.end_headers()

var_dump($web.session) # output: {}
```

The `$web.session` variable is a dictionary. You can set or get its keys:

```bash
println $web.session['foo']
$web.session['bar'] = 'baz'
```

This variable will be saved at server.
In the next requests by the same user, the current variables in the session will be loaded.

This lets you keep data for each user who interacts with your website.

## Advance
The session system provides additional functions and options.

#### NOTE: Do not customize the session system when you don't NEED to do this(for security)!

### `web.generate_random_session_id()`
This function generates a random session id and returns it.

### `web.validate_session_id(string $id)`
This function takes a session ID and validates it.
If the ID is valid, it returns the same ID; otherwise, it returns a new session ID.

### `web.write_session(string $id=null, dict $default={})`
This function creates or updates a session.

If you call it without arguments, it creates a new session and returns the session ID:

```bash
# ...

println web.write_session() # output is the new session id
```

You can also pass two arguments: the first is the ID and the second is the session data:

```bash
write_session($current_session_id, {
    'foo': 'bar',
    # ...
})
```

### `web.load_session_by_id(string $id)`
This function takes an ID, reads the session, and returns its contents as a dictionary.
If the ID does not exist, it creates an empty session with that ID.

```bash
# ...

println web.load_session_by_id($id) # output: {...}
```

### `web.end_session()`
This function writes current `$web.session` variable on the disk.

This function is called at the end of your program. You can also call it explicitly wherever you need.
