from flask import Blueprint, request, jsonify
from database import db
from models import Product

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/add', methods=['POST'])
def add_product():
    data = request.json
    try:
        nuevo = Product(
            category=data.get('type'),
            name=data.get('name'),
            price_gs=int(data.get('price')),
            sizes=data.get('sizes'),
            image_url=data.get('img'),
            added_by=data.get('user')
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"status": "success", "id": nuevo.id}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@admin_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    prod = Product.query.get(id)
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return jsonify({"status": "deleted"}), 200
    return jsonify({"status": "not_found"}), 404
