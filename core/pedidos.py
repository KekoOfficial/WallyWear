import json
from datetime import datetime
from core.utilidades import get_db_connection, registrar_log
from core.generador_id import generar_pedido_id

def crear_pedido(datos):
    conn = get_db_connection()
    cursor = conn.cursor()

    pedido_id = generar_pedido_id()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO pedidos (id, fecha, cliente_nombre, cliente_telefono, total, productos, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (pedido_id, fecha, datos.get('nombre'), datos.get('telefono'),
          datos['total'], json.dumps(datos['productos']), 'pendiente'))

    conn.commit()
    conn.close()
    registrar_log("pedidos", f"Nuevo pedido creado: {pedido_id}")
    return pedido_id

def confirmar_pago(pedido_id):
    conn = get_db_connection()
    pedido = conn.execute('SELECT * FROM pedidos WHERE id = ?', (pedido_id,)).fetchone()

    if not pedido:
        conn.close()
        return False, "Pedido no encontrado"

    productos_pedido = json.loads(pedido['productos'])

    # Validar stock
    for item in productos_pedido:
        prod = conn.execute('SELECT stock, nombre FROM productos WHERE id = ?', (item['id'],)).fetchone()
        if not prod or prod['stock'] < item['cantidad']:
            conn.close()
            return False, f"Stock insuficiente para {prod['nombre'] if prod else 'ID ' + str(item['id'])}"

    # Descontar stock
    for item in productos_pedido:
        conn.execute('UPDATE productos SET stock = stock - ? WHERE id = ?', (item['cantidad'], item['id']))

    # Actualizar pedido
    conn.execute('UPDATE pedidos SET estado = "pagado" WHERE id = ?', (pedido_id,))

    conn.commit()
    conn.close()
    registrar_log("inventario", f"Stock descontado por pedido {pedido_id}")
    return True, "Pago confirmado y stock actualizado"

def listar_pedidos():
    conn = get_db_connection()
    pedidos = conn.execute('SELECT * FROM pedidos ORDER BY fecha DESC').fetchall()
    conn.close()
    return [dict(row) for row in pedidos]
