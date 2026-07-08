import json
from core.utilidades import get_db_connection
def actualizar_variantes_producto(producto_id, variantes):
    conn = get_db_connection()
    conn.execute('UPDATE productos SET variantes = ? WHERE id = ?', (json.dumps(variantes), producto_id))
    conn.commit()
    conn.close()
    return True
def obtener_variantes_producto(producto_id):
    conn = get_db_connection()
    producto = conn.execute('SELECT variantes FROM productos WHERE id = ?', (producto_id,)).fetchone()
    conn.close()
    return json.loads(producto['variantes']) if producto and producto['variantes'] else []
