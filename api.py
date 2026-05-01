from fastapi import FastAPI
from storage import get_users
from users import formato_users_for_api, agg_user, del_user, edit_user_in_api


app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Khea duki sdlg'}


@app.get("/users")
def all_users():
    usuarios = get_users()      
    return [formato_users_for_api(user) for user in usuarios]

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    usuarios = get_users()
    for user in usuarios:
        if user[0] == user_id:
            return formato_users_for_api(user)
    return None

@app.post("/users")
def agg_user_api(name: str, edad: int):                               #Agregar usuarios
    agg_user(name, edad)
    return {'message': 'Se ha creado el usuario'}

@app.delete("/users/{user_id}")
def del_user_api(user_id: int):                                       #Eliminar Usuarios
    deleted = del_user(user_id)

    return {'message': 'Se ha eliminado el usuario'} if deleted else {'message': 'No se ha encontrado el usuario'}

@app.put("/users/{user_id}")
def edit_user(user_id: int, nuevo_name: str, nueva_edad: int):              #Editar usuarios
    edited = edit_user_in_api(user_id, nuevo_name, nueva_edad)  
    return {'message':'El usuario se editó correctamente'} if edited else {'message':'no se pudo editar el usuario'}                        
    