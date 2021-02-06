# WebServer Configuration
You can run Pashmak in Apache or other webservers.

For running Pashmak in the Traditional webservers, You only need to write a `.htaccess` file with the following contents:

```htaccess
AddHandler cgi-script .pashm .pashm.html .pit
Options +ExecCGI
```

And then, add the Shebang for your Pashmak scripts (`.pashm`, '.pashm.html', '.pit').
And make them executable using `chmod +x filename.pashm` (If you are on UNIX systems).

