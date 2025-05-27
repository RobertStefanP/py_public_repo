#  Sistema de Gestión de Inventario (Python por consola)

Este es un proyecto simple en Python que permite gestionar productos en un 
inventario a través de un menú interactivo desde la terminal. El programa 
almacena datos como nombre, categoría, precio y cantidad de cada producto.


##  Funcionalidades

- Agregar productos nuevos al inventario
- Actualizar precio y cantidad de productos existentes
- Eliminar productos por nombre
- Mostrar el inventario completo en forma de tabla
- Buscar productos por nombre
- Validación de entradas vacías o incorrectas
- Interfaz basada en consola (sin GUI)


##  Conceptos Aplicados

- Programación Orientada a Objetos (POO)
- Encapsulamiento (uso de getters y setters)
- Listas y diccionarios
- Validación de entradas con expresiones regulares (`re`)
- Visualización de datos con `pandas`
- Control de flujo por menús y bucles


## Estructura del Proyecto

- `inventario.py`: contiene las clases `Producto` e `Inventario`
- `menu.py` (o archivo principal): ejecuta el menú interactivo en consola


## Requisitos

- Python 3.x
- Biblioteca `pandas` instalada

## Instalación de dependencias:

pip install pandas

## Cómo ejecutar

Clona el repositorio
Navega a la carpeta del proyecto
Ejecuta el script principal: python menu.py
