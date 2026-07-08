from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PUERTO = 8080

class RedirigirHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirigir la raíz a la ubicación correcta del catálogo
        if self.path == "/" or self.path == "/index.html":
            self.send_response(301)
            self.send_header('Location', '/public/catalog/index.html')
            self.end_headers()
            return
        return super().do_GET()

if __name__ == "__main__":
    print(f"✅ Servidor en http://localhost:{PUERTO}")
    print("🏪 Redirigiendo entrada a la tienda")
    servidor = HTTPServer(("0.0.0.0", PUERTO), RedirigirHandler)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    servidor.server_close()
