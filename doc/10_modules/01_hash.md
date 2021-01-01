# hash module
with hash module, you can calculate hash sum of values:

```bash
import @hash

hash.sha256("hello") # also you can use hash.md5 and...
println(^) # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# OR
println(hash.sha256("hello"))
```

### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this function calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

### another hash algos
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
