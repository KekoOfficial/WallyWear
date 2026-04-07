from flask import Blueprint, request, jsonify
from database import db
from models import Product

admin_bp = Blueprint('admin', __name__)

# RUTA PARA SUBIR PRODUCTO (Desde el Bot)
@admin_bp.route('/add', methods=['POST'])
def add_product():
    data = request.json
    try:
        nuevo = Product(
            category=data.get('type'),
            name=data.get('name'),
            price_gs=int(data.get('price')),
            sizes=data.get('sizes'),      # Recibe "38,39,40" o "S,M,L"
            image_url=data.get('img'),
            added_by=data.get('user')     # Nombre de quien lo subió
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"status": "success", "id": nuevo.id}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# RUTA PARA ELIMINAR (Desde el Bot de Eder)
@admin_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    prod = Product.query.get(id)
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return jsonify({"status": "deleted"}), 200
    return jsonify({"status": "not_found"}), 404
