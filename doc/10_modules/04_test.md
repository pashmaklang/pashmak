# test module
the `test` module has some assertion functions to testing.

### default `assert` function
this function is a function in the pashmak. this function gets a value and asserts that is true:

```bash
# NOTE: you don't need to import anything for use this function
assert(2 == 2) # ok
assert(4 > 1) # ok
assert(True) # ok
assert('foo' == 'bar') # error: AssertError
```

### test.assertTrue
asserts true:

```bash
import @test

test.assertTrue(True)
test.assertTrue(5 == 5)
test.assertTrue(10 > 5)
```

above code will be run without error.

this code will get `AssertError`:

```bash
test.assertTrue(False)
test.assertTrue(3 == 2)
```

### test.assertFalse
this function is reverse of `test.assertTrue`.

```bash
test.assertFalse(False) # run be run without error
test.assertFalse(3 == 2) # run be run without error
test.assertFalse(2 == 2) # AssertionError
```

### test.assertEquals
this function asserts two values equals.

```bash
# two arguments should be passed:
test.assertEquals('hello', 'hello') # successful
test.assertEquals(2, 2) # successful
test.assertEquals('foo', 'bar') # AssertionError
```

### test.assertNotEquals
this function is reverse of `test.assertEquals`.

```bash
test.assertNotEquals('foo', 'bar') # successful
test.assertNotEquals(2, 7) # successful
test.assertNotEquals(2, 2) # AssertionError
```

### test.assertEmpty
asserts the value is empty(null).

```bash
test.assertEmpty(null)
test.assertEmpty('hello') # error
```

### test.assertNotEmpty
asserts value is not empty(null).

```bash
test.assertNotEmpty('hello')
test.assertNotEmpty(null) # error
```
