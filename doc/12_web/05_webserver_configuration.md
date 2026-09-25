# WebServer Configuration
You can run Pashmak in Apache or other webservers.

To run Pashmak with a traditional web server, add a `.htaccess` file with the following contents:

```htaccess
AddHandler cgi-script .pashm .pashm.html .pit
Options +ExecCGI
DirectoryIndex .pashm
```

Then add a shebang to your Pashmak scripts (`.pashm`, `.pashm.html`, or `.pit`).
On Unix systems, make them executable with `chmod +x filename.pashm`.
