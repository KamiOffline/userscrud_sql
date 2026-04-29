import os
from validators import val_nombre, val_edad

def ask_name(en, error='Ingrese un nombre válido\n'):   #Pedir nombre
    name = input(en).strip()

    while not val_nombre(name):
       os.system('cls')
       name = input(error).strip()

    return str(name).lower().capitalize()

def ask_edad(en, error='Ingrese una edad válida\n'):    #Pedir edad
    edad = input(en)

    while not val_edad(edad):
        os.system('cls')
        edad = input(error)
    
    return int(edad)

def ask_id(en, error='Ingrese un id válido o Ingrese 0 para regresar\n'):         #Input para busqueda por ID
    id = (input(en))

    while not id.isdigit():
        os.system('cls')
        id = input(error)

    return int(id)
    
def ask_search(en):                                     #Input para Busqueda por nombre
    valor = input(en).strip()
    return valor

def pause():                                            #Pausa en pantalla
    os.system('pause')

def clear():                                            #Limpiar pantalla
    os.system('cls')

def conf():                                             #Mensaje de confirmación
    conf = str(input('''Estas seguro de continuar con esta accion? No se puede deshacer!
\tEscriba "si" para continuar\n''')).lower().strip()
    if conf == 'si':
        return True
    return False