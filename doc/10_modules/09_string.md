# Module string
This module has some functions for working with strings

### concat
This function concats two strings

```bash
import @string

println(string.concat('pashm', 'ak')) # pashmak
```

### remove_last
This function removes last character of a string.

```bash
println(string.remove_last('pashmak')) # pashma
```

### remove_first
This function removes first character of a string.

```bash
println(string.remove_first('pashmak')) # ashmak
```

### add_last
This function add a string to last of string

```bash
println(string.add_last('pashma', 'k'))
```

### add_first
This function add a string to first of string

```bash
println(string.add_first('ashmak', 'p'))
```

### length
This function returns length of a string.

```bash
println(string.length('pashmak')) # 7
```

### cut
This function cuts a part of string.

```bash
println(string.cut('pashmak', 1, 4)) # ash
```

### upcase
This function makes upper case string.

```bash
println(string.upcase('pashmak')) # PASHMAK
```

### lowcase
This function makes lower case string.

```bash
println(string.lowcase('PASHMAK')) # pashmak
```

### reverse
This function reverse string

```bash
println(string.reverse('pashmak'))
```

### to_str
This function convert any type to string type

```bash
println(string.to_str(100))
println(typeof(string.to_str(100))) # test
```
