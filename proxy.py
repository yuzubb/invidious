import http.server
import urllib.request

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:] if self.path.startswith('/') else self.path
        try:
            self.send_response(200)
            self.end_headers()
            with urllib.request.urlopen(url) as response:
                self.copyfile(response, self.wfile)
        except Exception:
            self.send_error(500)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, Proxy)
    print(f"Proxy running on {host}:{port}")
    httpd.serve_forever()
