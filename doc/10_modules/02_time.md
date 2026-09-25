# time module
With this module, you can work with time.

### time.time
this function gives you current UNIX timestamp:

```bash
import @time

println(time.time()) # output is some thing like this: `1600416438.687201`
```

when you call this function, this function puts the unix timestamp into mem and you can access and use that.

### time.sleep
This function pauses execution for a number of seconds:

```bash
import @time

time.sleep(2) # sleeps for 2 seconds
# mem 2.4; time.sleep; # sleeps for 2.4 seconds
```

When you run this script, the program waits for 2 seconds and then continues.

With this function, you can wait for a number of seconds.

Put an integer or float into `mem`, or pass it as an argument, then call `time.sleep`. The program pauses for that many seconds.

### Another time functions
- time.ctime
- time.gmtime
- time.localtime

### cli usage
You can use this module in command line to see current UNIX timestamp:

```bash
$ pashmak @time
```
