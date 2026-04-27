import sqlite3


def agg_user(name, edad):                               #Agregar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO usuarios (nombre, edad)
        VALUES (?, ?)
        ''', (name, edad))
    
    return True

def del_user(id):                                     #Eliminar Usuarios
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

def user_exists(search):                                  #Matchear usuario existente
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        search = search.strip()

        cursor.execute('''
        SELECT 1 FROM usuarios
        WHERE nombre = ?
        ''', (search, ))

    return cursor.fetchone() is not None

def user_exists_by_id(search):                                  #Matchear usuario existente
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

def edit_user(id, nueva_edad):                        #Editar usuarios
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE usuarios
        SET edad = ?
        WHERE id = ?
        ''', (nueva_edad, id))

    return cursor.rowcount > 0

def formato_users(user, index=None):                    #Formato de impresion de usuarios
    id_user = user[0]
    nombre = user[1].capitalize()
    edad = user[2]

    if index is not None:
         return f'{index}. ID: {id_user} / Nombre: {nombre} - {edad} años'
    return f"ID: {id_user} / Nombre: {nombre} - {edad} años"

def conf():
    conf = str(input('''Estas seguro de continuar con esta accion? No se puede deshacer!
\tEscriba "si" para continuar\n''')).lower().strip()
    if conf == 'si':
        return True
    return False

def clear_users():                                      #Borrar Lista Actual
    
    if conf():
        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
        DELETE FROM usuarios
        ''')
            
        return True
    return False