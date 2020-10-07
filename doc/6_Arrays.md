# Arrays
arrays are a list from variables

look at this example:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

print $names; # output: ['parsa' , 'pashmak' , 'jack']
print $names[0]; # output: parsa
print $names[1]; # output: pashmak
print $names[2]; # output: jack
```

this is a example about array and loop:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

set $i; mem 0; copy $i;

section loop;
    print $names[$i] + '\n';
    mem $i + 1; copy $i;
mem $i < len($names); gotoif loop;
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### arraypush
you can add new item to a array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
print $myarray; # output: ['red' , 'green' , 'blue']

mem 'yellow'; arraypush $myarray ^; # add mem (^) to the $myarray
print $myarray; # output: ['red' , 'green' , 'blue' , 'yellow']
```

`arraypush` operation gets two argument: array and new item you want to add to the array

### arraypop
you can delete a item from array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
out $myarray; # output: ['red' , 'green' , 'blue']

mem 1; arraypop $myarray ^; # remove index mem (^) from $myarray
print $myarray; # output: ['red' , 'blue']
```

`arraypop` operation gets two argument: array and index of that item you want to be remove from array
