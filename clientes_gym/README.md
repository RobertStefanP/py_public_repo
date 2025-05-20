# Gestion de Clientes de un Gym

Este es un proyecto en Python que permite gestionar un registro de clientes de 
un gimnasio. Usa MySQL como base de datos y muestra el uso de programacion 
orientada a objetos, DAO y expresiones regulares.

## Funciones del programa

- Listar todos los clientes
- Insertar un nuevo cliente
- Actualizar los datos de un cliente
- Eliminar un cliente
- Validacion de texto y numeros con expresiones regulares

## Requisitos

- Python 3
- MySQL Server
- Libreria `mysql-connector-python`

## Estructura del proyecto

- `cliente.py`: clase Cliente
- `conexion.py`: clase Conexion con pool de conexiones
- `cliente_dao.py`: clase ClienteDAO para manejar operaciones SQL
- `menu.py`: clase Menu para la interfaz por consola
- `zona_fit_db`: nombre de la base de datos en MySQL
- Tabla `cliente` debe tener las siguientes columnas:

```sql
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    membresia INT
);


