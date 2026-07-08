from core.utilidades import get_db_connection

def verificar_credenciales(master, verif):
    conn = get_db_connection()
    pass_master = conn.execute("SELECT valor FROM configuracion WHERE clave = 'pass_master'").fetchone()
    pass_verif = conn.execute("SELECT valor FROM configuracion WHERE clave = 'pass_verif'").fetchone()
    conn.close()

    if not pass_master or not pass_verif:
        return master == '1111' and verif == '2222'

    return master == pass_master['valor'] and verif == pass_verif['valor']

def cambiar_passwords(nueva_master, nueva_verif):
    conn = get_db_connection()
    conn.execute("UPDATE configuracion SET valor = ? WHERE clave = 'pass_master'", (nueva_master,))
    conn.execute("UPDATE configuracion SET valor = ? WHERE clave = 'pass_verif'", (nueva_verif,))
    conn.commit()
    conn.close()
    return True
