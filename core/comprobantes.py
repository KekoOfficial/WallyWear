import os
from werkzeug.utils import secure_filename
from core.utilidades import get_db_connection
def guardar_comprobante(pedido_id, archivo):
    if archivo:
        filename = secure_filename(f"comprobante_{pedido_id}_{archivo.filename}")
        upload_dir = os.path.join('uploads', 'comprobantes')
        if not os.path.exists(upload_dir): os.makedirs(upload_dir)
        archivo.save(os.path.join(upload_dir, filename))
        conn = get_db_connection()
        conn.execute('UPDATE pedidos SET comprobante = ? WHERE id = ?', (filename, pedido_id))
        conn.commit()
        conn.close()
        return filename
    return None
