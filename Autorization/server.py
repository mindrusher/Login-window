#!/usr/bin/env python3
from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
http = HTTPServer(server_address, CGIHTTPRequestHandler)

http.serve_forever()