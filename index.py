from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PUERTO = 8080

class RedirigirHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Si entran a la raíz, redirige directamente a la tienda
        if self.path == "/" or self.path == "/index.html":
            self.send_response(301)
            self.send_header('Location', '/public/1_tienda.html')
            self.end_headers()
            return
        return super().do_GET()

if __name__ == "__main__":
    print(f"✅ Servidor en http://localhost:{PUERTO}")
    print("🏪 Entrada directa a la tienda")
    servidor = HTTPServer(("0.0.0.0", PUERTO), RedirigirHandler)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    servidor.server_close()
