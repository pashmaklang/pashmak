# Formating function arguments
The Pashmak function argument handling is **Dynamic**. this means that, you can dynamicaly handle arguments in your functions and you don't need to staticaly declare arguments.

for example, in lot of languages, you should write something like this:

```php
// php
function hello($name, $family){
    // ...
}
```

But in Pashmak, you will recive arguments in a variable as tuple. for example:

```bash
func hello(*$args) # you should write only ONE variable name
    println($args)
endfunc

hello('hello')
hello(100)
hello('foo', 'bar', 100)
```

output:

```
hello
100
('foo', 'bar', 100)
```

And you can dynamicaly handle the arguments.

### But what is the problem?
The problem is that, when function has Only One Argument, `$args/etc` is not a Tuple(list). in the above example, this is show.

But how to fix this? When i run `hello('hi')`, argument variable should be `('hi',)`(a tuple) but this is `'hi'`(self of variable) I want to do something to always(With any argument count) arguments be a tuple.

To do this, you can use `format_args` function.

for example:

```bash
func hello(*$args)
    $args = format_args($args)
    # ...
endfunc

hello('hello') # output: ('hello',)
```

With this function, this problem will be solved.
