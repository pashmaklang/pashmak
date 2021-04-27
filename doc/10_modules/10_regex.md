# Module regex

### Function `find($pattern, $string)`

This function searches for a regex pattern in a string and returns all things match with regex 
(Interface of re.findall in Python)

First argument named `pattern` is the regex pattern and
the second argument named `string` is the string that you want to search in.

An example:

```
import @regex

println regex.find('[0-9]', 'Hello 123 World')
```

output:

```
['1', '2', '3']
```
