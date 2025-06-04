# Gestion de Clientes de un Gimnasio

Este es un proyecto en Python que permite gestionar un registro de clientes de 
un gimnasio. Usa MySQL como base de datos y muestra el uso de programacion 
orientada a objetos, patron DAO y validaciones con expresiones regulares.

## Funciones del programa

- Listar todos los clientes
- Insertar un nuevo cliente
- Editar información existente
- Eliminar un cliente por ID
- Validacion de texto y numeros con expresiones regulares
- Conexión a base de datos con pool de conexiones MySQL
- Interfaz gráfica moderna con tabla y botones

## Ventana interactiva

La ventana permite ver los datos de los clientes, insertar nuevos, actualizar y 
eliminar con botones y campos de texto. Tambien muestra los datos en una tabla 
con scroll.

## Requisitos

- Python 3
- MySQL Server
- Libreria `mysql-connector-python`

## Estructura del proyecto

- `cliente.py`: clase Cliente
- `conexion.py`: clase Conexion con pool de conexiones
- `cliente_dao.py`: clase ClienteDAO para manejar operaciones SQL
- `menu.py`: clase Menu para la interfaz por consola
- `menu_GUI.py`: ventana grafica con tkinter
- `zona_fit_db`: nombre de la base de datos en MySQL

## Notas

- La membresía debe ser un número múltiplo de 100 (100, 200, 300…).
- Los nombres y apellidos deben tener al menos 3 letras (no se permiten números).
- Los datos ingresados se almacenan directamente en la base de datos.

La tabla `cliente` debe tener las siguientes columnas:

```sql
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    membresia INT
);
```

## Como usarlo

1. Clona el repositorio
2. Navega a la carpeta del proyecto
3. Para menu en terminal usar: python menu.py
4. Para menu por ventana interactiva: python menu_GUI.py
