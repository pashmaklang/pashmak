# random module
this module makes random numbers

### random.randint

```bash
import @random

# generates a random int between 1 and 10
println(random.randint(1, 10))
```

### random.seed
Initialize the random number generator

```bash
import @random
random.seed(1000)
```

### random.getstate
Returns the current internal state of the random number generator

```bash
import @random
print(random.getstate())
```

### random.random

```bash
import @random

# generates a random float less that 1
$rand = random.random()
println($rand)
```

### random.choice
This function gets a list and returns a random item from that list:

```bash
import @random
println random.choice([1, 2, 3])
```
