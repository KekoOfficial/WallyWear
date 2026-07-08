from flask import Blueprint, jsonify, request
from core.variantes import actualizar_variantes_producto, obtener_variantes_producto
variantes_bp = Blueprint('variantes', __name__)
@variantes_bp.route('/producto/<int:id>', methods=['GET'])
def get_variantes_producto(id): return jsonify(obtener_variantes_producto(id))
@variantes_bp.route('/producto/<int:id>', methods=['POST'])
def post_variantes_producto(id):
    data = request.json
    return jsonify({"success": actualizar_variantes_producto(id, data.get('variantes', []))})
