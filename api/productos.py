from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from core.productos import listar_productos, crear_producto, eliminar_producto, obtener_producto, actualizar_producto
from functools import wraps
from flask import session

productos_bp = Blueprint('productos', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_auth'):
            return jsonify({"error": "No autorizado"}), 403
        return f(*args, **kwargs)
    return decorated_function

@productos_bp.route('/', methods=['GET'])
def get_productos():
    return jsonify(listar_productos())

@productos_bp.route('/<int:id>', methods=['GET'])
def get_producto_by_id(id):
    prod = obtener_producto(id)
    if prod:
        return jsonify(prod)
    return jsonify({"error": "Producto no encontrado"}), 404

@productos_bp.route('/', methods=['POST'])
@admin_required
def add_producto():
    if 'imagen' in request.files:
        file = request.files['imagen']
        if file.filename != '':
            filename = secure_filename(file.filename)
            upload_dir = os.path.join('uploads', 'productos')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file.save(os.path.join(upload_dir, filename))

            # Recoger otros datos de form data ya que es multipart
            data = {
                'nombre': request.form.get('nombre'),
                'precio': int(request.form.get('precio')),
                'stock': int(request.form.get('stock')),
                'cantidad_prendas': int(request.form.get('cantidad_prendas', 1)),
                'categoria': request.form.get('categoria'),
                'imagen': filename,
                'descripcion': request.form.get('descripcion', ''),
                'material': request.form.get('material', ''),
                'variantes': request.form.get('variantes', '[]'),
                'talles': request.form.get('talles', '[]')
            }
            new_id = crear_producto(data)
            return jsonify({"success": True, "id": new_id})

    return jsonify({"success": False, "message": "Imagen requerida"}), 400

@productos_bp.route('/<int:id>', methods=['PUT'])
@admin_required
def update_producto_route(id):
    data = request.json
    success = actualizar_producto(id, data)
    return jsonify({"success": success})

@productos_bp.route('/<int:id>', methods=['DELETE'])
@admin_required
def delete_producto(id):
    eliminar_producto(id)
    return jsonify({"success": True})
