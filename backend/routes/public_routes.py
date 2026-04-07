from flask import Blueprint, jsonify
from models import Product

public_bp = Blueprint('public', __name__)

@public_bp.route('/products', methods=['GET'])
def get_all_products():
    # Ordenamos por los más nuevos primero
    products = Product.query.order_id(Product.id.desc()).all()
    return jsonify([{
        "id": p.id,
        "type": p.category,
        "name": p.name,
        "price_gs": p.price_gs,
        "sizes": p.sizes,
        "img": p.image_url,
        "added_by": p.added_by
    } for p in products])

@public_bp.route('/product/<int:id>', methods=['GET'])
def get_one_product(id):
    p = Product.query.get_or_404(id)
    return jsonify({
        "id": p.id,
        "name": p.name,
        "price_gs": p.price_gs,
        "sizes": p.sizes,
        "img": p.image_url
    })
