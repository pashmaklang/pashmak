# Session system
Session is a data saved in the backend (like cookies but at server).
This system allows you to save some variables in session with a user.

The general structure of the session is that, the server makes a very strong and random id
and gives that to the client as a cookie (`PASHMAK_SESSION`). also saves this id at server.

When browser sending requests to the server, server checks that cookie. if exists and is valid,
loads the data that saved for that id and brings that to the memory (`$web.session`).

## Basic usage
The basic usage:

```bash
import @web

web.init()

# This function starts the session system
web.start_session()

# you should start the session before ending headers
# because cookie `PASHMAK_SESSION` should be set in this step
# and cookies can be set before ending the headers
web.end_headers()

var_dump($web.session) # output: {}
```

The `$web.session` variable is a dictionary. you can set or get the keys:

```bash
println $web.session['foo']
$web.session['bar'] = 'baz'
```

This variable will be saved at server.
In the next requests by the same user, the current variables in the session will be loaded.

This allows you to keep some data for each user that interacting with your website.

## Advance
There is more functions and more options for them in session system.

#### NOTE: Do not customize the session system when you don't NEED to do this(for security)!

### `web.generate_random_session_id()`
This function generates a random session id and returns it.

### `web.validate_session_id(string $id)`
This function gets a session id and validates that.
If the session id is valid, returns the same id.
But if is NOT valid, returns a new session id.

### `web.write_session(string $id=null, dict $default={})`
This function writes a session(create/update).

If you call it without any argument, wil create a new session for you and returns the created session id:

```bash
# ...

println web.write_session() # output is the new session id
```

But you can pass two arguments to it: first is the id and second is the value:

```bash
write_session($current_session_id, {
    'foo': 'bar',
    # ...
})
```

### `web.load_session_by_id(string $id)`
This function gets a id and reads it and returns the session content(dict).
(If the passed id does not exists, creates a empty session with same id).

```bash
# ...

println web.load_session_by_id($id) # output: {...}
```

### `web.end_session()`
This function writes current `$web.session` variable on the disk.

This function will be called in End of your program. But you can optionlly call it everywhere you want.
