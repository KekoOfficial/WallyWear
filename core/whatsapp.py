from core.utilidades import get_db_connection
def obtener_configuracion_whatsapp():
    conn = get_db_connection()
    config = conn.execute('SELECT valor FROM configuracion WHERE clave = "whatsapp_pedidos"').fetchone()
    conn.close()
    return config['valor'] if config else ""
def guardar_configuracion_whatsapp(numero):
    conn = get_db_connection()
    conn.execute('INSERT OR REPLACE INTO configuracion (clave, valor) VALUES ("whatsapp_pedidos", ?)', (numero,))
    conn.commit()
    conn.close()
    return True
def generar_mensaje_whatsapp(pedido_id, total):
    return f"Hola.\nMi pedido es el ID #{pedido_id}.\n\nTotal a pagar:\nGs {total:,}.\n\nAdjunto mi comprobante de transferencia.\n\nMuchas gracias."
