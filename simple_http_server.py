import SimpleHTTPServer
import BaseHTTPServer
import sys

"""
Usage:
    python simple_http_server.py [port] 
Example:
    python simple_http_server.py 8000
"""

headers = [
    "Content-Type: application/x-protobuf",
    "Access-Control-Allow-Origin: *", 
    "Content-Encoding: gzip"
    ]

class CustomHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_new_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_new_headers(self):
        for i in headers:
            key, value = i.split(":", 1)
            self.send_header(key, value)

if __name__ == '__main__':
    BaseHTTPServer.test(HandlerClass=CustomHTTPRequestHandler, \
        ServerClass = BaseHTTPServer.HTTPServer, protocol="HTTP/1.1")
