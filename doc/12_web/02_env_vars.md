# Environment variables in web
There is some environment variables in web system that will be passed to your script.

This envvars contain some informations.

| Name | Description | Example value |
|------|-------------|---------------|
| `REQUEST_URI` | The requested uri | `/foo/bar` |
| `REQUEST_METHOD` | The http request method | `GET` or `POST` |
| `REMOTE_ADDR` | The remote(client) address(ip) | `1.2.3.4` |
| `REMOTE_PORT` | The remote port | `5674` |
| `SERVER_ADDR` | Address of the server | `127.0.0.1` |
| `SERVER_PORT` | The server port | `80` or `8000` |
| `SERVER_PROTOCOL` | The server protocol | `HTTP/1.0` |
| `DOCUMENT_ROOT` | The root of directory that web server serves that | `/var/www/html` |
| `SCRIPT_FILENAME` | Real path of the current running Pashmak script | `/var/www/html/app.pashm` |
| `SCRIPT_NAME` | Script name (not full path) | `/app.pashm` |
| `QUERY_STRING` | Part of URL after `?` (The get data query string) | `foo=bar&hi=bye` |
