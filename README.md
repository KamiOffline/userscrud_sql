# API CRUD de Usuarios con FastAPI

API REST desarrollada en Python utilizando FastAPI y SQLite para la gestión de usuarios.

---

## Características

* Crear usuarios
* Obtener lista de usuarios
* Obtener usuario por ID
* Editar usuarios (parcial o completo)
* Eliminar usuarios
* Validación de datos con Pydantic
* Manejo de errores con HTTPException

---

## Tecnologías utilizadas

* Python 3
* FastAPI
* SQLite3
* Pydantic
* Uvicorn

---

## Estructura del proyecto

```
/proyecto
│
├── api.py          # Endpoints de la API
├── db.py           # Funciones de base de datos
├── schemas.py      # Modelos Pydantic
├── usuarios.db     # Base de datos SQLite
└── README.md
```

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio o descargar archivos

2. Instalar dependencias:

```bash
pip install fastapi uvicorn
```

3. Ejecutar el servidor:

```bash
uvicorn api:app --reload
```

4. Abrir en el navegador:

* Swagger UI:
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Endpoints disponibles

### Estado de la API

```
GET /
```

Respuesta:

```json
{
  "status": "API running"
}
```

---

### Obtener todos los usuarios

```
GET /users
```

---

### Obtener usuario por ID

```
GET /users/{user_id}
```

Respuesta:

* 200 → usuario encontrado
* 404 → usuario no encontrado

---

### Crear usuario

```
POST /users
```

Body (JSON):

```json
{
  "name": "Juan",
  "edad": 20
}
```

---

### Editar usuario (parcial o completo)

```
PUT /users/{user_id}
```

Body (JSON):

```json
{
  "name": "Pedro"
}
```

o:

```json
{
  "edad": 25
}
```

o:

```json
{
  "name": "Pedro",
  "edad": 25
}
```

---

### Eliminar usuario

```
DELETE /users/{user_id}
```

Respuesta:

* 200 → usuario eliminado
* 404 → usuario no encontrado

---

## Conceptos aprendidos

* Creación de APIs REST con FastAPI
* Uso de métodos HTTP (GET, POST, PUT, DELETE)
* Manejo de base de datos SQLite
* Separación de responsabilidades (API vs DB)
* Uso de Pydantic para validación de datos
* Manejo de parámetros en URL (path) y cuerpo (body)
* Manejo de errores con HTTPException

---

## Posibles mejoras futuras

* Autenticación (JWT)
* Uso de ORM (SQLAlchemy)
* Validaciones avanzadas
* Logging y manejo de errores global
* Deploy en la nube (Render, Railway, etc.)

---

## Autor

KamiOffline
---
