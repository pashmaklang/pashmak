# Running modules in command line
Some modules behave like applications and can be run directly from the command line.

For example:

```bash
$ pashmak @helloworld
```

The `@helloworld` is a test module for this action.

output:

```
Hello world!
```

Running the command above is equivalent to importing `helloworld` with `import_run`:

```bash
import_run @helloworld
```
