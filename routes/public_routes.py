from flask import Blueprint, jsonify
from models import Product

public_bp = Blueprint('public', __name__)

# RUTA PARA VER TODO EL CATÁLOGO
@public_bp.route('/products', methods=['GET'])
def get_products():
    try:
        # Traemos los productos, los más nuevos primero
        products = Product.query.order_by(Product.id.desc()).all()
        return jsonify([{
            "id": p.id,
            "type": p.category,
            "name": p.name,
            "price": p.price_gs,
            "sizes": p.sizes,
            "img": p.image_url,
            "autor": p.added_by
        } for p in products]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# RUTA PARA VER UN PRODUCTO SOLO (Detalles)
@public_bp.route('/product/<int:id>', methods=['GET'])
def get_single_product(id):
    p = Product.query.get_or_404(id)
    return jsonify({
        "id": p.id,
        "name": p.name,
        "price": p.price_gs,
        "sizes": p.sizes,
        "img": p.image_url,
        "desc": p.category
    }), 200
