from database import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False) # zapatilla, remera, etc.
    name = db.Column(db.String(100), nullable=False)
    price_gs = db.Column(db.Integer, nullable=False)
    sizes = db.Column(db.String(200), nullable=False) # Guardamos "38, 39, 40"
    image_url = db.Column(db.String(500))
    added_by = db.Column(db.String(100)) # Nombre del gerente o Oliver
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
