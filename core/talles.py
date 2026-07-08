import json
from core.utilidades import get_db_connection, registrar_log

def listar_talles_por_categoria(categoria):
    talles = {
        'calzado': [str(i) for i in range(35, 46)],
        'remeras': ['S', 'M', 'L', 'XL', 'XXL'],
        'pantalones': [str(i) for i in range(36, 56, 2)],
        'shorts': ['S', 'M', 'L', 'XL'],
        'personalizados': []
    }
    # Log talles lookup
    registrar_log("talles", f"Consultando talles para la categoria: {categoria}")
    return talles.get(categoria.lower(), [])

def actualizar_talles_producto(producto_id, talles):
    conn = get_db_connection()
    conn.execute('UPDATE productos SET talles = ? WHERE id = ?', (json.dumps(talles), producto_id))
    conn.commit()
    conn.close()
    registrar_log("talles", f"Talles actualizados para producto ID {producto_id}: {talles}")
    return True
