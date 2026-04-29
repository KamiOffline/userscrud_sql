def val_nombre(name):                                   #Validacion de nombres
    name = name.strip()
    return bool(name and all(p.isalpha() for p in name.split()) or name == '0')

def val_edad(edad):                                     #Validacion de edades
    try:
        if int(edad) >= 1 and int(edad) <= 100:
            return True
        else:
            return False
    except ValueError:
        return False