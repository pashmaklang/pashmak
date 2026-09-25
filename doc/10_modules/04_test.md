# test module
The `test` module provides assertion functions for testing.

### default `assert` function
The built-in `assert` function takes a value and asserts that it is true:

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

The code above runs without an error.

This code raises an `AssertError`:

```bash
test.assertTrue(False)
test.assertTrue(3 == 2)
```

### test.assertFalse
This function is the inverse of `test.assertTrue`.

```bash
test.assertFalse(False) # run be run without error
test.assertFalse(3 == 2) # run be run without error
test.assertFalse(2 == 2) # AssertionError
```

### test.assertEquals
This function asserts that two values are equal.

```bash
# two arguments should be passed:
test.assertEquals('hello', 'hello') # successful
test.assertEquals(2, 2) # successful
test.assertEquals('foo', 'bar') # AssertionError
```

### test.assertNotEquals
This function is the inverse of `test.assertEquals`.

```bash
test.assertNotEquals('foo', 'bar') # successful
test.assertNotEquals(2, 7) # successful
test.assertNotEquals(2, 2) # AssertionError
```

### test.assertEmpty
Asserts that a value is empty (`null`).

```bash
test.assertEmpty(null)
test.assertEmpty('hello') # error
```

### test.assertNotEmpty
Asserts that a value is not empty (`null`).

```bash
test.assertNotEmpty('hello')
test.assertNotEmpty(null) # error
```
