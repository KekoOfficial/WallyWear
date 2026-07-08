from flask import Blueprint, jsonify, request
from core.whatsapp import obtener_configuracion_whatsapp, guardar_configuracion_whatsapp, generar_mensaje_whatsapp
whatsapp_bp = Blueprint('whatsapp', __name__)
@whatsapp_bp.route('/config', methods=['GET'])
def get_whatsapp_config(): return jsonify({"numero": obtener_configuracion_whatsapp()})
@whatsapp_bp.route('/config', methods=['POST'])
def post_whatsapp_config():
    data = request.json
    return jsonify({"success": guardar_configuracion_whatsapp(data.get('numero'))})
@whatsapp_bp.route('/mensaje/<string:pedido_id>', methods=['GET'])
def get_whatsapp_mensaje(pedido_id):
    from core.detalle_pedido import obtener_detalle_pedido
    pedido = obtener_detalle_pedido(pedido_id)
    if pedido:
        mensaje = generar_mensaje_whatsapp(pedido_id, pedido['total'])
        return jsonify({"mensaje": mensaje, "numero": obtener_configuracion_whatsapp()})
    return jsonify({"error": "Pedido no encontrado"}), 404
