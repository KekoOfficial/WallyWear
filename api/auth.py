from flask import Blueprint, request, jsonify, session
from core.autenticacion import verificar_credenciales

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    master = data.get('master')
    verif = data.get('verif')

    if verificar_credenciales(master, verif):
        session['admin_auth'] = True
        return jsonify({"success": True, "message": "Acceso concedido"})
    else:
        return jsonify({"success": False, "message": "Acceso denegado"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('admin_auth', None)
    return jsonify({"success": True})

@auth_bp.route('/check', methods=['GET'])
def check():
    return jsonify({"authenticated": session.get('admin_auth', False)})
