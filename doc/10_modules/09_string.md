# Module string
This module has some functions for working with strings.

### concat
This function concatenates two strings.

```bash
import @string

println(string.concat('pashm', 'ak')) # pashmak
```

### remove_last
This function removes the last character from a string.

```bash
println(string.remove_last('pashmak')) # pashma
```

### remove_first
This function removes the first character from a string.

```bash
println(string.remove_first('pashmak')) # ashmak
```

### add_last
This function appends one string to another.

```bash
println(string.add_last('pashma', 'k'))
```

### add_first
This function prepends one string to another.

```bash
println(string.add_first('ashmak', 'p'))
```

### length
This function returns the length of a string.

```bash
println(string.length('pashmak')) # 7
```

### cut
This function extracts part of a string.

```bash
println(string.cut('pashmak', 1, 4)) # ash
```

### upcase
This function converts a string to uppercase.

```bash
println(string.upcase('pashmak')) # PASHMAK
```

### lowcase
This function converts a string to lowercase.

```bash
println(string.lowcase('PASHMAK')) # pashmak
```

### reverse
This function reverses a string.

```bash
println(string.reverse('pashmak'))
```

### to_str
This function converts any value to a string.

```bash
println(string.to_str(100))
println(typeof(string.to_str(100))) # str
```
