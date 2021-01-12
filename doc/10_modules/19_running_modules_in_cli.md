# Running modules in command line
Some of modules maybe have a behavior like a application. You can run them directly from command line.

for example:

```bash
$ pashmak @helloworld
```

The `@helloworld` is a test module for this action.

output:

```
Hello world!
```

Actually, running above command is like that to import `helloworld` with `import_run` command:

```bash
import_run @helloworld
```
