from flask import Blueprint, jsonify
from core.detalle_pedido import obtener_detalle_pedido
detalle_pedido_bp = Blueprint('detalle_pedido', __name__)
@detalle_pedido_bp.route('/<string:id>', methods=['GET'])
def get_detalle_pedido(id):
    pedido = obtener_detalle_pedido(id)
    return jsonify(pedido) if pedido else (jsonify({"error": "Pedido no encontrado"}), 404)
