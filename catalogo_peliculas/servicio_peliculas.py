import os.path
from pelicula import Pelicula


class ServicioPeliculas:
    catalogo = "peliculas.txt"
    
    def __init__(self):
        self.peliculas = []
    
    def agregar_pelicula(self):
        print("Agregando pelicula.")
        pelicula = input("Dame el nombre de la pelicula: ")
        nueva_pelicula = Pelicula(pelicula)
        self.peliculas.append(nueva_pelicula)       
        try:
            with open(self.catalogo, "a") as archivo:
                archivo.write(f"{nueva_pelicula}\n")
        except Exception as e:
            print(f"Error al guardar la pelicula: {e}")
        print(f"Pelicula agregada correctamente." ) 
                   
    def listar_peliculas(self):
        peliculas = []
        try:           
            with open(self.catalogo, "r") as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    pelicula = Pelicula(nombre)
                    peliculas.append(pelicula)     
        except FileNotFoundError:
            print(f"El archivo {self.catalogo} no se econtro.")                                  
        except Exception as e:
            print(f"Ocurrio un error: {e}")            
        if peliculas:
            contador = 0
            print("Listado de peliculas:\n")
            for pelicula in peliculas:
                contador += 1
                print(f"Pelicula {contador}: {pelicula}")      
        else:
            print("No hay peliculas en el catalogo.")  
        self.peliculas = peliculas
         
    def eliminar_catalogo(self):
        os.remove(self.catalogo)
        print(f"Archivo eliminado: {self.catalogo}.")
            