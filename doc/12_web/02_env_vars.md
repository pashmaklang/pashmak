# Environment variables in web
The web system passes several environment variables to your script.

These variables contain request and server information.

| Name | Description | Example value |
|------|-------------|---------------|
| `REQUEST_URI` | The requested URI | `/foo/bar` |
| `REQUEST_METHOD` | The HTTP request method | `GET` or `POST` |
| `REMOTE_ADDR` | The remote client's IP address | `1.2.3.4` |
| `REMOTE_PORT` | The remote port | `5674` |
| `SERVER_ADDR` | Address of the server | `127.0.0.1` |
| `SERVER_PORT` | The server port | `80` or `8000` |
| `SERVER_PROTOCOL` | The server protocol | `HTTP/1.0` |
| `DOCUMENT_ROOT` | The root directory served by the web server | `/var/www/html` |
| `SCRIPT_FILENAME` | Real path of the current running Pashmak script | `/var/www/html/app.pashm` |
| `SCRIPT_NAME` | Script name (not full path) | `/app.pashm` |
| `QUERY_STRING` | The part of the URL after `?` (raw GET data; use `$web.get`) | `foo=bar&hi=bye` |
| `POST_RAW_DATA` | The raw POST data (use `$web.post`) | `foo=bar&hi=bye` |
