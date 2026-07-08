import sqlite3
import os
from config import Config

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def registrar_log(tipo, mensaje):
    log_dir = "database/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = f"{log_dir}/{tipo}.log"
    with open(log_path, "a") as f:
        f.write(f"{mensaje}\n")
