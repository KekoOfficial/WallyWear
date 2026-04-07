from database import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False) # ej: zapatilla, remera, gorra
    name = db.Column(db.String(100), nullable=False)
    price_gs = db.Column(db.Integer, nullable=False)    # Precio en Guaraníes
    sizes = db.Column(db.String(200), nullable=False)   # "38, 39, 40" o "M, L, XL"
    image_url = db.Column(db.String(500))               # Link de la foto
    added_by = db.Column(db.String(100))                # Nombre del administrador/gerente
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Product {self.name}>'
