from datetime import datetime
def generar_pedido_id():
    return f"PED-{int(datetime.now().timestamp())}"
