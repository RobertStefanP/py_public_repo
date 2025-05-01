import re
import sys
import pandas as pd

from inventario import Producto, Inventario


def elija_opcion(): 
    while True:
        print("\t  1 -Reintentar.\n\t  2 -Salir.\n") 
        opcion = input("\t- Elija 1 o 2: ")
        if opcion == "1":
            salir = False
            break
        elif opcion == "2":      
            salir = True
            break
        else:
            print("\n\t- No valido, elegir 1 o 2.")
            continue
    return salir
   

if __name__ == '__main__':
    inventario = Inventario()  
    while True:
        salir_al_menu = False         
        try:
            menu = False 
            print("\n-----MENU INVENTARIO-----\n")                        
            print("1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Mostrar inventario")
            print("5. Buscar un producto")    
            print("6. Salir")               
            opcion = int(input("\nElige una opcion: "))  

            if opcion == 1:                               
                while not salir_al_menu:  
                    try:
                        nombre = input("\t- Nombra el produco que desea agregar: ")                                                                                                                                                                                                                 
                        if inventario.producto_existente(nombre):  
                            print("\n\t- El producto existe en el inventario.")  
                            salir = elija_opcion()                                                                                                                    
                            if salir:
                                salir_al_menu = True  
                                break
                        else:    
                            if re.fullmatch(r"[a-zA-Z0-9\s]+", nombre) and nombre.strip() != "":
                                    break                         
                            else:
                                raise ValueError                              
                    except ValueError:
                        print("\n\t- No espacios vacios/caracteres especiales.")
                        opcion = elija_opcion()                                                                                                                    
                        if opcion:
                            salir_al_menu = True  
                            break

                if nombre and not salir_al_menu:                                                                                   
                    while not salir_al_menu:     
                        try:                                                                                                                                                           
                            categoria = input("\t- Introduzca la categoria: ")                                                          
                            if re.fullmatch(r"[a-zA-Z0-9\s]+", categoria) and categoria.strip() != "":
                                break
                            else:
                                raise ValueError                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                        except ValueError:
                            print("\n\t- No espacios vacios/caracteres especiales.")                         
                            opcion = elija_opcion()                                                                                                                    
                            if opcion:
                                categoria = None
                                salir_al_menu = True  
                                break 

                    if categoria and not salir_al_menu:  
                        while not salir_al_menu:
                            try:                                                            
                                precio = float(input("\t- Precio del producto: "))                     
                                if precio <= 0:
                                    raise ValueError        
                                break                                                                                                                                                       
                            except ValueError:
                                print("\n\t- No espacios vacios/caracteres especiales/numeros negativos.")
                                opcion = elija_opcion()                                                                                                                    
                                if opcion:
                                    precio = None
                                    salir_al_menu = True  
                                    break
                                                                                                
                        if precio and not salir_al_menu:
                            while not salir_al_menu: 
                                try:                             
                                    cantidad = float(input("\t- Introduzca la cantidad: "))                                                                 
                                    if cantidad <= 0:
                                        raise ValueError
                                    break                                                                                                                                                                                     
                                except ValueError:
                                    print("\n\t- No espacios vacios/caracteres especiales/numeros negativos.")
                                    opcion = elija_opcion()                                                                                                                    
                                    if opcion:
                                        cantidad = None
                                        salir_al_menu = True  
                                        break           
                                                                                                                                                                                                                
                            if cantidad and not salir_al_menu:
                                producto = Producto(nombre, categoria, precio, cantidad)  
                                if inventario.agregar_producto(producto):  
                                    print(f"\n- Producto '{nombre}' agregado al inventario.")
                                
            elif opcion ==2:                                                       
                while not salir_al_menu:                
                    nombre_producto = input("\t- Introduzca el producto a actualizar: ")            
                    while inventario.producto_existente(nombre_producto): 
                        while True:
                            try:                                                                   
                                nuevo_precio = input("\t- Nuevo precio (vacío por no cambiar): ")                        
                                if nuevo_precio.strip() == "":
                                    nuevo_precio = None
                                    break                            
                                nuevo_precio = float(nuevo_precio)
                                if nuevo_precio <= 0:
                                    raise ValueError
                                else: 
                                    break  
                            except ValueError:
                                print("\n\t- Introducir un valor numerico valido.")
                                opcion = elija_opcion()                                                                                                                    
                                if opcion:
                                    salir_al_menu = True 
                                    break                             
                        if salir_al_menu:        
                            break                                                          
                        while True:
                            try:    
                                nueva_cantidad = input("\n\t- Nueva cantidad (vacío por no cambiar): ")                        
                                if nueva_cantidad.strip() == "":
                                    nueva_cantidad = None
                                    break                                 
                                nueva_cantidad = float(nueva_cantidad)
                                if nueva_cantidad <= 0:
                                    raise ValueError                                
                                else:
                                    break 
                            except ValueError:
                                print("\n\t- Introducir un valor numerico valido.")
                                opcion = elija_opcion()                                                                                                                    
                                if opcion:
                                    salir_al_menu = True 
                                    break                                
                        if salir_al_menu:        
                            break                                                                                                                           
                        inventario.actualizar_producto(nombre_producto, nuevo_precio, nueva_cantidad)
                        print(f"\n- Producto '{nombre_producto}' actualizado.")
                        salir_al_menu = True
                        break                                                                                                                                                                                                                   
                    else:                     
                        print("\n\t- Producto no encontrado!")
                        opcion = elija_opcion()                                                                                                                    
                        if opcion:
                            salir_al_menu = True  
                            break 
                    if salir_al_menu:
                        break                                  
                                                                                                                                                                    
            elif opcion == 3:
                while not salir_al_menu:                
                    nombre_producto = input("\t- Nombre del producto que desea eliminar: ")                   
                    if inventario.eliminar_producto(nombre_producto):
                        print(f"\t- Producto '{nombre_producto}' eliminado.")
                        break
                    else:
                        print("\n\t- Producto no encontrado!")
                        opcion = elija_opcion()                                                                                                                    
                        if opcion:
                            salir_al_menu = True  
                            break                                            
                            
            elif opcion == 4:
                df_inventario = inventario.mostrar_inventario()             
                if df_inventario is None: 
                    print("\t- El inventario está vacío.")                
                else:                
                    print("\n- Inventario:")
                    df_inventario.index = df_inventario.index + 1                
                    print(df_inventario)
                                                                                                                                
            elif opcion == 5:
                while not salir_al_menu:                
                    nombre_producto = input("\t- Introduzca el nombre del producto a buscar: ")
                    if nombre_producto:
                        producto = inventario.buscar_producto(nombre_producto) 
                        if producto:                      
                            df_producto = producto.mostrar_info() 
                            print(f"\t- Producto encontrado: ")
                            df_producto.index = df_producto.index + 1
                            print(df_producto)
                            break                  
                        else:                                             
                            print("\n\t- Producto no encontrado!")
                            opcion = elija_opcion()                                                                                                                    
                            if opcion:
                                salir_al_menu = True  
                                break  

            elif opcion == 6:  
                print("\t- Saliendo del programa.")
                sys.exit()            
            else:
                raise ValueError                                
        except ValueError:
            print("\t- Debe introducir un valor numérico válido.")
            continue  
                                