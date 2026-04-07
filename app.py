import os
from flask import Flask, render_template
from flask_cors import CORS
from database import db

# Importación de Blueprints (Asegúrate de que routes/__init__.py existe)
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp

app = Flask(__name__, 
            static_folder='static', 
            template_folder='templates')

CORS(app)

# --- CONFIGURACIÓN DE RUTAS Y BASE DE DATOS ---
# Usamos ruta absoluta para que SQLite no se pierda en las carpetas de Termux
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mallywear.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# --- RUTAS DE NAVEGACIÓN (FRONTEND) ---

@app.route('/')
def index():
    """Página principal de la tienda"""
    return render_template('index.html')

@app.route('/producto/<int:id>')
def producto_detalle(id):
    """Vista detallada de una prenda"""
    return render_template('producto.html')

@app.route('/carrito')
def carrito():
    """Sección de compra final"""
    return render_template('carrito.html')

# --- REGISTRO DE APIS (CONTROLADORES) ---
# Aquí se conectan el Bot de Telegram y el JavaScript del cliente
app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(public_bp, url_prefix='/api')

# --- MANEJO DE ERRORES ---
@app.errorhandler(404)
def not_found(e):
    return "<h1>Error 404: Mally Wear no encontró esta ruta</h1>", 404

# --- INICIO DEL SISTEMA ---
if __name__ == '__main__':
    with app.app_context():
        # Crea las tablas automáticamente al encender el servidor
        db.create_all()
        print("✅ Base de datos 'mallywear.db' verificada y lista.")
    
    print("\n" + "="*30)
    print("🚀 MALLY WEAR SYSTEM ONLINE")
    print(f"📍 URL LOCAL: http://127.0.0.1:5000")
    print(f"📍 URL RED: http://10.174.78.220:5000")
    print("="*30 + "\n")
    
    # Debug=True para que el servidor se reinicie solo al guardar cambios
    app.run(host='0.0.0.0', port=5000, debug=True)
