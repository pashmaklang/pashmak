# Namespaces

name space is a very useful system to split sections of program.

look at this example:

```bash
namespace App;
    func say_hello;
        print 'hello world\n';
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
        print 'i am from First\n';
    endfunc;
endnamespace;

namespace Last;
    func dosomething;
        print 'i am from Last\n';
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
        print 'hello world\n';
    endfunc;

    say_hello;
endns;

App.say_hello;
```

also namespace system is sync with variables:

```bash
namespace App;
    $name = 'parsa';
    print $name + '\n'; # output: parsa
    print $App.name; # output: parsa
endns;

print $App.name; # output: parsa

# but this has error:
print $name; # VariableError: undefined variable $name, because it is in App namespace and is accessible with `$App.name`
```

this system is very useful.

### use operation
the `use` operation is a command to use content of a namespace.

look at this example:

```bash
namespace App;
    func dosomething;
        print 'hello world\n';
    endfunc;

    $name = 'parsa';
endns;

App.dosomething;
print $App.name + '\n';
```

output:

```
hello world
parsa
```

we have to put `App.` before `dosomething` to run this function.
but i want to don't use namespace prefix and just type name of function to call this. what i have to do?

look at this example:

```bash
namespace App;
    func dosomething;
        print 'hello world\n';
    endfunc;

    $name = 'parsa\n';
endns;

use App;

App.dosomething;
dosomething;

out $App.name;
out $name;
```

output:

```
hello world
hello world
parsa
parsa
```

when i use `use` operation and give a namespace as argument to that, i can call all of that namespace members without namespace prefix.

for example if there is a namespace named `App` and have a function named `dosomething`, for call that function i have to write `App.dosomething`. but if i run `use App;`, after that i can call this function just by typing `dosomething;`
