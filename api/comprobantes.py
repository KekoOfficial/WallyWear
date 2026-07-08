from flask import Blueprint, jsonify, request
from core.comprobantes import guardar_comprobante
comprobantes_bp = Blueprint('comprobantes', __name__)
@comprobantes_bp.route('/<string:pedido_id>', methods=['POST'])
def post_comprobante(pedido_id):
    if 'comprobante' in request.files:
        filename = guardar_comprobante(pedido_id, request.files['comprobante'])
        if filename: return jsonify({"success": True, "filename": filename})
    return jsonify({"success": False, "message": "Archivo no enviado"}), 400
