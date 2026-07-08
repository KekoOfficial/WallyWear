from core.utilidades import get_db_connection, registrar_log

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
    registrar_log("pedidos_whatsapp", f"Configuracion de WhatsApp actualizada a: {numero}")
    return True

def generar_mensaje_whatsapp(pedido_id, total):
    # Format total with dots (standard Paraguayan format)
    total_formateado = f"{int(total):,}".replace(",", ".")
    mensaje = (
        f"Hola.\n"
        f"Mi pedido es el ID #{pedido_id}.\n\n"
        f"Total a pagar:\n"
        f"Gs {total_formateado}.\n\n"
        f"Adjunto mi comprobante de transferencia.\n\n"
        f"Muchas gracias."
    )
    registrar_log("pedidos_whatsapp", f"Mensaje de WhatsApp generado para pedido: {pedido_id}")
    return mensaje
