from flask import Blueprint, request, jsonify, session
from core.pedidos import crear_pedido, confirmar_pago, listar_pedidos
from functools import wraps

pedidos_bp = Blueprint('pedidos', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_auth'):
            return jsonify({"error": "No autorizado"}), 403
        return f(*args, **kwargs)
    return decorated_function

@pedidos_bp.route('/', methods=['POST'])
def post_pedido():
    data = request.json
    pedido_id = crear_pedido(data)
    return jsonify({"success": True, "pedido_id": pedido_id})

@pedidos_bp.route('/', methods=['GET'])
@admin_required
def get_pedidos():
    return jsonify(listar_pedidos())

@pedidos_bp.route('/<string:id>/confirmar', methods=['POST'])
@admin_required
def confirmar_pedido(id):
    success, message = confirmar_pago(id)
    if success:
        return jsonify({"success": True, "message": message})
    else:
        return jsonify({"success": False, "message": message}), 400
