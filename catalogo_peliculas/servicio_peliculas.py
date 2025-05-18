import os.path
from pelicula import Pelicula


class ServicioPeliculas:
    PELICULAS = "peliculas.txt"
    
    def __init__(self):
        self.peliculas = []
        # If path exist
        if os.path.isfile(self.PELICULAS):
            self.peliculas = self.obtener_peliculas()
        # else:
        #     self.guardar_archivo()
    
    def agregar_pelicula(self):
        print("Agregando pelicula.")
        pelicula = input("Dame el nombre de la pelicula: ")
        nueva_pelicula = Pelicula(pelicula)
        self.peliculas.append(nueva_pelicula)       
        try:
            with open(self.PELICULAS, "w") as archivo:
                archivo.write(f"{nueva_pelicula}\n")
        except Exception as e:
            print(f"Error al guardar la pelicula: {e}")
        print(f"Pelicula agregada correctamente." ) 
        
             
    def obtener_peliculas(self):
        peliculas = []
        try:
            with open(self.PELICULAS, "r") as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    pelicula = Pelicula(nombre)
                    peliculas.append(pelicula)                    
        except Exception as e:
            print(f"Error al leer el catalogo de peliculas: {e}.")        
        return peliculas
                       
    def listar_peliculas(self):
        try:
            with open(self.PELICULAS, "r") as archivo:
                
                pass
            
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        
            
    def eliminar_catalogo(self):
        pass
    