# Classes general attributes
classes has some general properties:

- `__name__`: name of the class
- `__parent__`: name of parent of class
- `__props__`: all of object properties as Dictonary
- `__private_props__`: list of the name of the private properties
- `__protected_props__`: list of the name of the protected properties
- `__methods__`: all of object methods as Dictonary
- `__theclass__`: the object class type

for example:

```bash
class Person

endclass

$person = Person()

println($person->__name__) # output: Person
```
