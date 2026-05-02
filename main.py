
from users import agg_user, del_user, filt_may, search, edit_user, formato_users, user_exists,user_exists_by_id, clear_users
from storage import get_users, create_db, create_tab
from console import ask_name, ask_edad, clear, pause, ask_search, ask_id

clear()
create_db()
create_tab()
usuarios = get_users()          #Carga/Crea base de datos

while True:                     
    clear()                     #Menú principal
    print('''\033[30;47mPrograma de usuarios\033[0m   
---------------------
\033[93m1.-\033[0m Agregar usuarios
\033[93m2.-\033[0m Eliminar usuarios
\033[93m3.-\033[0m Ver todos
\033[93m4.-\033[0m Buscar usuarios
\033[93m5.-\033[0m Ver mayores
\033[93m6.-\033[0m Editar usuario
\033[93m7.-\033[0m Limpiar lista
\033[93m8.-\033[0m Salir del programa
---------------------''')
    
    while True:
        try:
            option = int(input('Ingrese la opcion que desea\n'))
            clear()
            break
        except ValueError:
            print('Ingrese una opcion valida')
    match option:               #Selector de opciones
        case 1:                 #Agregar usuario
            clear()
    
            name = ask_name('Ingrese el nombre, o ingrese "0" para cancelar:\n')
            clear()
            if name != '0':
                if not user_exists(name):
                    edad = ask_edad('Ingrese la edad\n')

                    clear() 
                    if agg_user(name, edad):
                        usuarios = get_users()
                        print('Usuario Agregado correctamente.') 
                        pause()   

                else:
                    print('Error. El usuario ya existe.')  
                    pause()
            else:
                clear()
                print('Operacion cancelada')
                pause()

        case 2:                 #Eliminar usuarios
            clear()
            id = ask_id('Ingrese el ID del usuario a eliminar, o ingrese "0" para cancelar:\n')
            clear()

            if id != 0:
                if user_exists_by_id(id):
                    del_user(id)
                    clear()
                    usuarios = get_users()
                    print('Usuario Eliminado.')
                    pause() 
                else:
                    clear()
                    print('EL usuario no existe.')
                    pause()
            else:
                clear()
                print('Se ha cancelado la operación')
                pause()
            
        case 3:                 #Ver todos los usuarios
            clear()
            usuarios = get_users()
            if usuarios:
                for i, user in enumerate(usuarios, start=1):
                    print(formato_users(user, i))
                pause()
            else:
                clear()
                print('No se han encontrado usuarios')
                pause()
            
        case 4:                 #Buscar nombres
            name = ask_search('Ingrese el nombre / ID que desea encontrar, o ingrese "0" para cancelar\n')
            clear()
            if name != '0':
                resultado = search(name)


                if resultado:           #Regresa resultados de busqueda por nombre/ID
                    clear()
                    for i, user in enumerate(resultado, start=1):
                        print(formato_users(user, i))
                    pause()
                    
                else:
                    print('No se encontraron usuarios')
                    pause()
            else:
                clear()
                print('Operacion cancelada')
                pause()
                
        case 5:                 #Filtrar usuarios por mayores
            mayores = filt_may()
            for i, user in enumerate(mayores, start=1):
                print(formato_users(user, i))
            pause()

        case 6:                 #Editar usuario
            clear()
            id = ask_id('Ingrese el ID del usuario que quiere cambiar, o ingrese "0" para cancelar\n')
            if id != 0:
                if user_exists_by_id(id):       #Verifica que la ID del usuario existe
                    nueva_edad = ask_edad('Ingrese la nueva edad del usuario\n') 
                        
                    edit_user(id, nueva_edad)
                    print('EL usuario se ha editado con éxito.')
                    pause()
                    
                    
                else:
                    clear()
                    print('El usuario no existe.')
                    pause()
            else:
                clear()
                print('Operacion cancelada')
                pause()

        case 7:                 #Limpiar la lista
            if clear_users():
                clear()
                print('La lista se ha eliminado correctamente')
                pause()
            else:
                clear()
                print('Operacion cancelada.')
                pause()

        case 8:                 #Salir del menú / Terminar programa
            break

        case _:                 #Opciones fuera del menú
            clear()
            print('Ingrese una opcion válida')
            pause()

print('**Fin del programa')     #Texto de salida