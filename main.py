
from users import agg_user, del_user, filt_may, search, edit_user, formato_users, user_exists,user_exists_by_id, clear_users
from storage import get_users, create_db, create_tab
from console import ask_name, ask_edad, clear, pause, ask_search, ask_id

clear()
create_db()
create_tab()
usuarios = get_users()          #Carga/Crea base de datos

while True:                     #Menú principal
    clear()
    print('''Programa de usuarios
---------------------
1.-Agregar usuarios
2.-Eliminar usuarios
3.-Ver todos
4.-Buscar usuarios
5.-Ver mayores
6.-Editar usuario
7.-Limpiar lista
8.-Salir del programa
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
    
            name = ask_name('Ingrese el nombre:\n')
            clear()
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

        case 2:                 #Eliminar usuarios
            clear()
            name = ask_id('Ingrese el ID del usuario a eliminar:\n')
            clear()

            if user_exists_by_id(name):
                del_user(name)
                clear()
                usuarios = get_users()
                print('Usuario Eliminado.')
                pause()
                
            else:
                clear()
                print('EL usuario no existe.')
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
            name = ask_search('Ingrese el nombre / ID que desea encontrar\n')
            clear()
            resultado = search(name)


            if resultado:
                clear()
                for i, user in enumerate(resultado, start=1):
                    print(formato_users(user, i))
                pause()
                
            else:
                print('No se encontraron usuarios')
                pause()
                
        case 5:                 #Filtrar usuarios por mayores
            mayores = filt_may()
            for i, user in enumerate(mayores, start=1):
                print(formato_users(user, i))
            pause()

        case 6:                 #Editar usuario
            clear()
            id = ask_id('Ingrese el ID del usuario que quiere cambiar\n')

            if search(id):
                nueva_edad = ask_edad('Ingrese la nueva edad del usuario\n') 
                    
                edit_user(id, nueva_edad)
                get_users()
                print('EL usuario se ha editado con éxito.')
                pause()
                
                
            else:
                clear()
                print('El usuario no existe.')
                pause()
        
        case 7:                 #Limpiar la lista
            if clear_users():
                get_users()
                clear()
                print('La lista se ha eliminado correctamente')
                pause()
            else:
                clear()
                print('Operacion cancelada.')
                pause()

        case 8:                 #Salir del menú / Terminar programa
            break
print('**Fin del programa')