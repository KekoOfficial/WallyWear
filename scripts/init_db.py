import sqlite3
import os

DB_PATH = 'database/mallywear.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabla de productos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        stock INTEGER NOT NULL,
        cantidad_prendas INTEGER DEFAULT 1,
        categoria TEXT NOT NULL,
        imagen TEXT,
        codigo_interno TEXT,
        estado TEXT DEFAULT 'activo'
    )
    ''')

    # Tabla de categorías
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL
    )
    ''')

    # Tabla de pedidos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id TEXT PRIMARY KEY,
        fecha TEXT NOT NULL,
        cliente_nombre TEXT,
        cliente_telefono TEXT,
        total INTEGER NOT NULL,
        productos TEXT NOT NULL, -- JSON string
        estado TEXT DEFAULT 'pendiente'
    )
    ''')

    # Tabla de redes sociales
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS redes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        url TEXT,
        activo INTEGER DEFAULT 1
    )
    ''')

    # Tabla de contenido (políticas, nosotros, etc.)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contenido (
        id TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        cuerpo TEXT NOT NULL
    )
    ''')

    # Tabla de configuración
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS configuracion (
        clave TEXT PRIMARY KEY,
        valor TEXT NOT NULL
    )
    ''')

    # Insertar categorías por defecto si no existen
    categorias_defecto = [('Remeras',), ('Zapatillas',), ('Pantalones',)]
    cursor.executemany('INSERT OR IGNORE INTO categorias (nombre) VALUES (?)', categorias_defecto)

    # Insertar configuración inicial
    config_inicial = [
        ('pass_master', '1111'),
        ('pass_verif', '2222'),
        ('nombre_tienda', 'Mally Wear')
    ]
    cursor.executemany('INSERT OR IGNORE INTO configuracion (clave, valor) VALUES (?, ?)', config_inicial)

    conn.commit()
    conn.close()
    print(f"✅ Base de datos inicializada en {DB_PATH}")

if __name__ == "__main__":
    init_db()
