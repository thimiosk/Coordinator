from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

port = int(os.environ.get('PORT', '10000'))
ThreadingHTTPServer(('0.0.0.0', port), Handler).serve_forever()
