import http.server
import json
from http import HTTPStatus

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_headers(content_type='application/json')
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write("OK".encode())
        else:
            self._set_headers(HTTPStatus.NOT_FOUND)
            self.wfile.write("Endpoint not found".encode())

def run(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
