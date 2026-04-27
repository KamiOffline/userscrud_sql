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

def ask_id(en, error='Ingrese un id válido\n'):
    id = (input(en))

    while not id.isdigit():
        os.system('cls')
        id = input(error)

    return id
    
def ask_search(en):
    valor = input(en).strip()
    return valor

def pause():                                            #Pausa en pantalla
    os.system('pause')

def clear():                                            #Limpiar pantalla
    os.system('cls')

