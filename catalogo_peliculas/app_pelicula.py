import os.path
from pelicula import Pelicula
from servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:
    
    def __init__(self):
        self.peliculas = []
        self.servicio_peliculas = ServicioPeliculas()
        self.pelicula = Pelicula(nombre = "")
        
    def menu_peliculas(self):
        salir = False
        while not salir:
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
                    print("Hasta pronto.")
                    return True
                else:            
                    print("Invalido, introduce un numero de 1 a 4.")
            except ValueError:
                print(f"Error: Introduce un numero valido.")    
                        
    def listar_pelicula(self):        
        pass
    
    def eliminar_catalogo(self):
        pass
            
    
if __name__ == '__main__':
    catalogo_peliculas = AppCatalogoPeliculas()
    catalogo_peliculas.menu_peliculas()