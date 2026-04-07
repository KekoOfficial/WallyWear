import os
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from database import db
# Importación de Blueprints
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp

app = Flask(__name__, 
            static_folder='static', 
            template_folder='templates')

CORS(app)

# --- CONFIGURACIÓN DE BASE DE DATOS ---
# Usamos una ruta absoluta para evitar problemas en Termux
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mallywear.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos con la App
db.init_app(app)

# --- RUTAS DE NAVEGACIÓN (FRONTEND) ---

@app.route('/')
def index():
    """Ruta principal: Muestra la tienda"""
    return render_template('index.html')

@app.route('/producto/<int:id>')
def producto_detalle(id):
    """Ruta para ver un producto específico"""
    return render_template('producto.html')

@app.route('/carrito')
def carrito():
    """Ruta del carrito de compras"""
    return render_template('carrito.html')

# --- REGISTRO DE APIS (BACKEND) ---
app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(public_bp, url_prefix='/api')

# --- MANEJO DE ERRORES ---
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>MALLY WEAR: Esta página no existe</h1>", 404

if __name__ == '__main__':
    with app.app_context():
        # Crea las tablas si no existen
        db.create_all()
        print("✅ Base de datos verificada/creada.")
    
    print("🚀 MALLY WEAR SERVER OPERATIVO")
    print("📍 Accede en: http://localhost:5000")
    # debug=True es clave para ver errores en Termux mientras programas
    app.run(host='0.0.0.0', port=5000, debug=True)
