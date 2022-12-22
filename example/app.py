from sdk.progressively import Progressively
from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        sdk = Progressively.create(
            "valid-sdk-key", "http://localhost:4000", {"hello": "world", "number": 1})

        if (sdk.evaluate("newHomepage")):
            self.wfile.write(b'New homepage')
        else:
            self.wfile.write(b'Old homepage')


httpd = HTTPServer(('localhost', 3003), HelloWorldHandler)
httpd.serve_forever()
