from flask import Flask, send_from_directory, redirect
import os
from config import Config
from api.auth import auth_bp
from api.productos import productos_bp
from api.pedidos import pedidos_bp

def create_app():
    app = Flask(__name__, static_folder=None) # Desactivamos static_folder por defecto
    app.config.from_object(Config)

    # Registro de Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(productos_bp, url_prefix='/api/productos')
    app.register_blueprint(pedidos_bp, url_prefix='/api/pedidos')

    # Servir archivos estáticos manualmente para mayor control
    @app.route('/')
    def index():
        return redirect('/public/tienda.html')

    @app.route('/public/<path:path>')
    def serve_public(path):
        return send_from_directory(os.path.join(app.root_path, '..', 'public'), path)

    @app.route('/admin/<path:path>')
    def serve_admin(path):
        return send_from_directory(os.path.join(app.root_path, '..', 'admin'), path)

    @app.route('/uploads/<path:path>')
    def serve_uploads(path):
        return send_from_directory(os.path.join(app.root_path, '..', 'uploads'), path)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
