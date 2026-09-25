# Classes general attributes
Classes have several general properties:

- `__name__`: name of the class
- `__parent__`: name of parent of class
- `__props__`: all object properties as a dictionary
- `__methods__`: all object methods as a dictionary
- `__theclass__`: the object class type

For example:

```bash
class Person

endclass

$person = Person()

println($person->__name__) # output: Person
```
