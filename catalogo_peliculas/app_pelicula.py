import os.path
from pelicula import Pelicula
from servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:
    
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()
        
    def menu_peliculas(self):
        while True:
            print("""Opciones:
                1. Agregar Pelicula
                2. Listar Peliculas
                3. Eliminar catalogo peliculas
                4. Salir""")
            try:
                opcion = int(input("Escribe tu opcion (1-4): "))                        
                if opcion == 1:
                    self.servicio_peliculas.agregar_pelicula()
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_catalogo()
                elif opcion == 4:
                    print("Salimos del programa...")
                    break
                else:            
                    print("Invalido, introduce un numero de 1 a 4.")                    
            except ValueError:
                print(f"Error: Introduce un numero valido.")    
            except Exception as e:
                print(f"Ocurrio un error: {e}")
   
   
if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.menu_peliculas()
    