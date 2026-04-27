# CRUD de Usuarios con SQLite

Proyecto en Python que implementa un sistema CRUD de usuarios utilizando SQLite como base de datos local.

Este proyecto fue desarrollado como práctica para aprender manejo de bases de datos, separación de responsabilidades, validación de datos y estructura básica de proyectos en Python.

## Funcionalidades

- Agregar usuarios
- Eliminar usuarios
- Editar edad de usuarios
- Ver todos los usuarios
- Buscar usuarios por nombre
- Filtrar usuarios mayores de edad
- Vaciar la base de datos con confirmación
- Validar nombres y edades
- Persistencia de datos con SQLite

## Tecnologías utilizadas

- Python
- SQLite
- Git / GitHub

## Estructura del proyecto

```text
userscrud_sql/
│
├── main.py        # Menú principal y flujo del programa
├── users.py       # Funciones CRUD y lógica de usuarios
├── storage.py     # Creación de base de datos y tabla
├── console.py     # Funciones relacionadas con consola/input
├── .gitignore     # Archivos ignorados por Git
└── README.md      # Documentación del proyecto
