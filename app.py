from flask import Flask
from flask_cors import CORS
from database import db
# Importación de las Blueprints
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp

app = Flask(__name__)
CORS(app)

# Configuración
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mallywear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB
db.init_app(app)

# Registrar las rutas
app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(public_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        # Esto crea la base de datos automáticamente si no existe
        db.create_all()
    print("🚀 MALLY WEAR SERVER ACTIVO EN EL PUERTO 5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
