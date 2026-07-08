from core.utilidades import get_db_connection

def listar_productos():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos WHERE estado = "activo"').fetchall()
    conn.close()
    return [dict(row) for row in productos]

def obtener_producto(id):
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    conn.close()
    return dict(producto) if producto else None

def crear_producto(datos):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, precio, stock, cantidad_prendas, categoria, imagen, codigo_interno, descripcion, material, variantes, talles)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (datos['nombre'], datos['precio'], datos['stock'], datos['cantidad_prendas'],
          datos['categoria'], datos['imagen'], datos.get('codigo_interno'),
          datos.get('descripcion'), datos.get('material'), datos.get('variantes'), datos.get('talles')))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def eliminar_producto(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM productos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return True
