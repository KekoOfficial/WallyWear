from http.server import SimpleHTTPRequestHandler, HTTPServer

PUERTO = 8080

class Servidor(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

if __name__ == "__main__":
    print(f"✅ Servidor corriendo en http://localhost:{PUERTO}")
    print("📂 Accede: /public/1_tienda.html para ver la tienda")
    print("🔐 Accede: /admin/1_panel_productos.html para el panel")
    servidor = HTTPServer(("0.0.0.0", PUERTO), Servidor)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    servidor.server_close()
    print("\n❌ Servidor detenido")
