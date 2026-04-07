from flask import Flask
from flask_cors import CORS
from database import db
from routes.admin_routes import admin_bp
from routes.public_routes import public_bp

app = Flask(__name__)
CORS(app)

# Configuración de la Base de Datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mallywear.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registro de Rutas
app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(public_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Crea la base de datos al iniciar
    app.run(host='0.0.0.0', port=5000, debug=True)
