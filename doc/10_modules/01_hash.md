# hash module
With the `hash` module, you can calculate the hash of a value:

```bash
import @hash

hash.sha256("hello") # You can also use hash.md5 and other algorithms.
println(^) # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# OR
println(hash.sha256("hello"))
```

### how it works?
First, we call `hash.sha256` and pass the string `hello` as an argument (or put it in `mem`). The function calculates the SHA-256 hash and stores the result in `mem`, where it can then be accessed.

### Other hash algorithms
- hash.blake2b(string)
- hash.blake2s(string)
- hash.md5(string)
- hash.sha1(string)
- hash.sha224(string)
- hash.sha256(string)
- hash.sha384(string)
- hash.sha3_224(string)
- hash.sha3_256(string)
- hash.sha3_384(string)
- hash.sha3_512(string)
- hash.sha512(string)
- hash.shake_128(string, length)
- hash.shake_256(string, length)
