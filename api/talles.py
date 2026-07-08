from flask import Blueprint, jsonify, request
from core.talles import listar_talles_por_categoria, actualizar_talles_producto
talles_bp = Blueprint('talles', __name__)
@talles_bp.route('/categoria/<string:categoria>', methods=['GET'])
def get_talles_categoria(categoria): return jsonify(listar_talles_por_categoria(categoria))
@talles_bp.route('/producto/<int:id>', methods=['POST'])
def post_talles_producto(id):
    data = request.json
    return jsonify({"success": actualizar_talles_producto(id, data.get('talles', []))})
