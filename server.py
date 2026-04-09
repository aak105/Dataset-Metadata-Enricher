#!/usr/bin/env python3
"""
CORS Proxy Server for Dataset Metadata Augmenter
Handles requests to OpenMetadata API and serves the static HTML file.

Usage:
    python3 server.py [port]
    
Default port is 3000. Access at http://localhost:3000
"""

import http.server
import socketserver
import urllib.request
import urllib.error
import json
import sys
import os
from urllib.parse import urlparse, parse_qs

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

class CORSProxyHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with CORS support and proxy capability"""
    
    def end_headers(self):
        """Add CORS headers to all responses"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')
        self.send_header('Access-Control-Max-Age', '86400')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.end_headers()
    
    def proxy_request(self, method):
        """Proxy a request to the target URL"""
        path = self.path
        
        # Check if this is a proxy request
        if not path.startswith('/proxy/'):
            return False
        
        # Extract target URL from path
        target_url = path[7:]  # Remove '/proxy/' prefix
        
        # Handle URL encoding
        if target_url.startswith('http%3A') or target_url.startswith('https%3A'):
            from urllib.parse import unquote
            target_url = unquote(target_url)
        
        print(f"[PROXY] {method} -> {target_url}")
        
        try:
            # Read request body for POST/PUT/PATCH
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length) if content_length > 0 else None
            
            # Build request
            req = urllib.request.Request(target_url, data=body, method=method)
            
            # Copy relevant headers
            for header in ['Content-Type', 'Authorization', 'Accept']:
                if header in self.headers:
                    req.add_header(header, self.headers[header])
            
            # Add default headers if not present
            if 'Content-Type' not in self.headers and body:
                req.add_header('Content-Type', 'application/json')
            if 'Accept' not in self.headers:
                req.add_header('Accept', 'application/json')
            
            # Make request
            with urllib.request.urlopen(req, timeout=30) as response:
                response_body = response.read()
                
                self.send_response(response.status)
                
                # Copy response headers
                for header, value in response.getheaders():
                    if header.lower() not in ['transfer-encoding', 'connection', 'access-control-allow-origin']:
                        self.send_header(header, value)
                
                self.end_headers()
                self.wfile.write(response_body)
                
                print(f"[PROXY] Response: {response.status} ({len(response_body)} bytes)")
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8', errors='replace')
            error_code = e.code
            print(f"[PROXY] HTTP Error {error_code}: {error_body[:500]}")
            
            # Send the original error status code
            self.send_response(error_code)
            self.send_header('Content-Type', 'application/json')
            self.send_header('X-Original-Status', str(error_code))
            self.end_headers()
            
            # Try to pass through the error response body
            try:
                # If it's valid JSON, pass it through as-is
                json.loads(error_body)
                self.wfile.write(error_body.encode())
            except:
                # Otherwise wrap it in JSON
                wrapped = json.dumps({
                    'error': True,
                    'code': error_code,
                    'message': f'HTTP Error {error_code}: {e.reason}'
                })
                self.wfile.write(wrapped.encode())
            return True
                
        except urllib.error.URLError as e:
            print(f"[PROXY] URL Error: {e.reason}")
            self.send_response(502)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': True,
                'message': f'Connection failed: {e.reason}'
            }).encode())
            
        except Exception as e:
            print(f"[PROXY] Error: {e}")
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': True,
                'message': str(e)
            }).encode())
        
        return True
    
    def do_GET(self):
        """Handle GET requests"""
        if self.proxy_request('GET'):
            return
        
        # Serve index.html for root path
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        
        super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        if not self.proxy_request('POST'):
            self.send_error(404, 'Not Found')
    
    def do_PUT(self):
        """Handle PUT requests"""
        if not self.proxy_request('PUT'):
            self.send_error(404, 'Not Found')
    
    def do_PATCH(self):
        """Handle PATCH requests"""
        if not self.proxy_request('PATCH'):
            self.send_error(404, 'Not Found')
    
    def do_DELETE(self):
        """Handle DELETE requests"""
        if not self.proxy_request('DELETE'):
            self.send_error(404, 'Not Found')
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[HTTP] {args[0]}")


def main():
    # Change to directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CORSProxyHandler) as httpd:
        print(f"""
╔═══════════════════════════════════════════════════════════╗
║     Dataset Metadata Augmenter - Local Server             ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║   🌐 App URL:    http://localhost:{PORT}                    ║
║   🔌 Proxy:      http://localhost:{PORT}/proxy/{{url}}        ║
║                                                           ║
║   OpenMetadata Integration:                               ║
║   - Configure OM URL in Settings tab                      ║
║   - Get JWT token from OM → Settings → Bots → ingestion   ║
║   - Use "Push to OpenMetadata" on any dataset             ║
║                                                           ║
║   Press Ctrl+C to stop                                    ║
╚═══════════════════════════════════════════════════════════╝
""")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Server] Shutting down...")
            httpd.shutdown()


if __name__ == "__main__":
    main()
