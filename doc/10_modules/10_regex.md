# Module regex

### Function `find($pattern, $string)`

This function searches a string for a regular expression pattern and returns all matches.
It provides an interface similar to Python's `re.findall`.

The first argument, `pattern`, is the regular expression. The second argument, `string`, is the text to search.

For example:

```
import @regex

println regex.find('[0-9]', 'Hello 123 World')
```

output:

```
['1', '2', '3']
```
