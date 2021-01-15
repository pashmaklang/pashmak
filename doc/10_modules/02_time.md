# time module
with this module, you can work with time.

### time.time
this function gives you current UNIX timestamp:

```bash
import @time

println(time.time()) # output is some thing like this: `1600416438.687201`
```

when you call this function, this function puts the unix timestamp into mem and you can access and use that.

### time.sleep
this function sleeps for secounds:

```bash
import @time

time.sleep(2) # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this function, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` function, then program will sleep for value of `mem` as secounds

### Another time functions
- time.ctime
- time.gmtime
- time.localtime

### cli usage
You can use this module in command line to see current UNIX timestamp:

```bash
$ pashmak @time
```
