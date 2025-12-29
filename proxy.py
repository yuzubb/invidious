import http.server
import urllib.request

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.request.urlopen(url), self.wfile)

if __name__ == '__main__':
    port = 8080
    print(f"Starting proxy on port {port}...")
    http.server.HTTPServer(('127.0.0.1', port), Proxy).serve_forever()