import json
from core.utilidades import get_db_connection
def obtener_detalle_pedido(pedido_id):
    conn = get_db_connection()
    pedido = conn.execute('SELECT * FROM pedidos WHERE id = ?', (pedido_id,)).fetchone()
    if not pedido:
        conn.close()
        return None
    pedido_dict = dict(pedido)
    pedido_dict['productos'] = json.loads(pedido_dict['productos'])
    for item in pedido_dict['productos']:
        prod = conn.execute('SELECT imagen, categoria FROM productos WHERE id = ?', (item['id'],)).fetchone()
        if prod:
            item['imagen'] = prod['imagen']
            item['categoria'] = prod['categoria']
    conn.close()
    return pedido_dict
