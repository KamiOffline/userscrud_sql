
import sqlite3

def create_db():                        #Crea el archivo SQL
    conn = sqlite3.connect('usuarios.db')
    conn.close()
    
def create_tab():                       #Crea la tabla de users
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
        )
        """)
       
def get_users():                        #Cargar la lista de usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM usuarios ORDER BY edad
        ''')
    
    return cursor.fetchall()