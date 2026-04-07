from flask import Blueprint, jsonify
from models import Product

public_bp = Blueprint('public', __name__)

@public_bp.route('/products', methods=['GET'])
def get_products():
    try:
        # Trae todo el stock de Mally Wear
        products = Product.query.order_by(Product.id.desc()).all()
        return jsonify([{
            "id": p.id,
            "type": p.category,
            "name": p.name,
            "price": p.price_gs,
            "sizes": p.sizes,
            "img": p.image_url
        } for p in products]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
