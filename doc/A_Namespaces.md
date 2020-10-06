# Namespaces

name space is a very useful system to split sections of program.

look at this example:

```bash
namespace App;
    func say_hello;
        mem 'hello world\n'; out ^;
    endfunc;

    say_hello;
endnamespace;

App.say_hello;
```

output:

```
hello world
hello world
```

actualy, everything where is declared between `namespace <something>;` and `endnamespace;` will be under this.

in above example, we declared a namespace named `App`. and we declared `say_hello` function in that.

next, we called `say_hello` inside the namespace, and one time we called `say_hello` outside the namespace.

when we are calling a member of namespace from outside of that namespace, we have to put name of namespace with a `.` before name of that function

for example here, our namespace name is `App` and out function name is `say_hello`. we can write only `say_hello` inside the namespace but for call it from outside of namespace, we have to write `App.say_hello`.

also look at this example:

```bash
namespace First;
    func dosomething;
        mem 'i am from First\n'; out ^;
    endfunc;
endnamespace;

namespace Last;
    func dosomething;
        mem 'i am from Last\n'; out ^;
    endfunc;
endnamespace;

First.dosomething;
Last.dosomething;
```

output:

```
i am from First
i am from Last
```

also you can use `endns` keyword insted of `endnamespace` (this is from stdlib):

```bash
namespace App;
    func say_hello;
        mem 'hello world\n'; out ^;
    endfunc;

    say_hello;
endns;

App.say_hello;
```

this system is very useful.
