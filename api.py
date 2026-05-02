from fastapi import FastAPI
from storage import get_users
from users import formato_users_for_api, agg_user, del_user, edit_user_in_api,search
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
class user_create(BaseModel):
    name: str
    edad: int
class user_update(BaseModel):
    name : str | None = None
    edad : int | None = None
    
@app.get('/')
def root():
    return {'message': 'Running'}


@app.get("/users")
def all_users():
    usuarios = get_users()      
    return [formato_users_for_api(user) for user in usuarios]

@app.get("/users/{username}")
def get_user_by_id(username):
    db = search(username)
    resultado = []
    for user in db:
        if username.lower() == user[0] or user[1].lower():
            resultado.append(user)
    return resultado


@app.post("/users")
def agg_user_api(user: user_create):                               #Agregar usuarios
    agg_user(user.name, user.edad)
    return {'message': 'Se ha creado el usuario'}

@app.delete("/users/{user_id}")
def del_user_api(user_id: int):                                       #Eliminar Usuarios
    deleted = del_user(user_id)
    if deleted:
        return {'message': 'Se ha eliminado el usuario'}  
    else:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')

@app.put("/users/{user_id}")
def edit_user(user_id: int, user : user_update):              #Editar usuarios
    edited = edit_user_in_api(user_id, user.name, user.edad)
    
    if edited:
        return {'message':'El usuario se editó correctamente'}
    else: 
        raise HTTPException(status_code=404, detail='Usuario no encontrado')                        
    