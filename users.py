import sqlite3
from console import conf

def agg_user(name, edad):                               #Agregar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO usuarios (nombre, edad)
        VALUES (?, ?)
        ''', (name, edad))
    
    return True

def del_user(id):                                       #Eliminar Usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?
        ''', (id,))

    return cursor.rowcount > 0

def filt_may():                                         #Filtrar usuarios mayores
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM usuarios
        WHERE edad >= 18
        ''')

        return cursor.fetchall() 

def user_exists(search):                                #Identificar usuario existente por nombre
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        search = search.strip()

        cursor.execute('''
        SELECT 1 FROM usuarios
        WHERE nombre = ?
        ''', (search, ))

    return cursor.fetchone() is not None

def user_exists_by_id(search):                          #Identificar usuario existente por ID
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT 1 FROM usuarios
        WHERE id = ?
        ''', (search, ))

    return cursor.fetchone() is not None

def search(name):                                       #Buscar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM usuarios 
        WHERE nombre LIKE ? OR id = ?
        ''', (f'%{name}%', int(name) if name.isdigit() else -1))

    return cursor.fetchall()

def edit_user(id, nueva_edad):                          #Editar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE usuarios
        SET edad = ?
        WHERE id = ?
        ''', (nueva_edad, id))

    return cursor.rowcount > 0

def edit_user_in_api(user_id, name, nueva_edad):                          #Editar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        
        if name is None and nueva_edad is None:
            return False

        elif name is None:
            cursor.execute('''
                UPDATE usuarios
                SET edad = ?
                WHERE id = ?
                ''', (nueva_edad, user_id))
            
            return cursor.rowcount > 0
        
        elif nueva_edad is None:
            cursor.execute('''
                UPDATE usuarios
                SET nombre = ?
                WHERE id = ?
                ''', (name, user_id))
            
            return cursor.rowcount > 0 
        
        else:
            cursor.execute('''
                UPDATE usuarios
                SET nombre = ?, edad = ?
                WHERE id = ?
                ''', (name, nueva_edad, user_id))
            
            return cursor.rowcount > 0

def formato_users(user, index=None):                    #Formato de impresion de usuarios
    id_user = user[0]
    nombre = user[1].capitalize()
    edad = user[2]

    if index is not None:
         return f'{index}. ID: {id_user} / Nombre: {nombre} - {edad} años'
    return f"ID: {id_user} / Nombre: {nombre} - {edad} años"

def formato_users_for_api(user):
    return {'id': user[0],
            'nombre': user[1].capitalize(),
            'edad': user[2]
            }

def clear_users():                                      #Limpiar BD Actual
    
    if conf():
        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
        DELETE FROM usuarios
        ''')
            
        return True
    return False