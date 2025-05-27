# Catalogo de Peliculas

Este es un proyecto basico en Python que permite gestionar un catalogo de 
peliculas desde la terminal. Se utiliza programación orientada a objetos y 
manejo de archivos.


## Funcionalidades

- Agregar una nueva película al catálogo
- Listar todas las películas guardadas
- Eliminar el archivo del catálogo
- Menú interactivo en consola
- Guarda las películas en un archivo `peliculas.txt` para mantener los datos 
entre ejecuciones
- Al iniciar, carga automáticamente las películas previamente guardadas
- Las películas se guardan en el archivo `peliculas.txt` en el mismo directorio 
  del proyecto.

## Estructura del Proyecto

- `pelicula.py`: Clase `Pelicula`, representa una película.
- `servicio_peliculas.py`: Clase `ServicioPeliculas`, gestiona el archivo y las 
    operaciones con peliculas.
- `app_catalogo_peliculas.py`: Clase `AppCatalogoPeliculas`, contiene el menu 
    y la interacción con el usuario.


## Cómo ejecutar

1. Clona el repositorio
2. Navega al directorio del proyecto
3. Ejecuta: python app_pelicula.py
