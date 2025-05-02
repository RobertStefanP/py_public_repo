import re
import sys

from inventario import Producto, Inventario


def elija_opcion(): 
    while True:
        print("\n\t- No vacio/caracteres/nr negativos/ceros.") 
        print("\t  1 -Reintentar.\n\t  2 -Salir.\n") 
        opcion = input("\t- Elija 1 o 2: ")
        if opcion == "1":
            return False
        elif opcion == "2":  
            print("\t- Volviendo al menu principal.")    
            return True
        else:
            print("\n\t- No valido, elegir 1 o 2.")

def pedir_input_texto(prompt):
    while True:
        entrada = input(prompt)
        if re.fullmatch(r"[a-zA-Z0-9\\s]+", entrada) and entrada.strip() != "":
            return entrada
        salir = elija_opcion()
        if salir:
            return None

def pedir_input_float(prompt):
    while True:
        try:
            entrada = float(input(prompt))
            if entrada > 0:
                return entrada
            raise ValueError
        except ValueError:
            if elija_opcion():
                return None

    
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
            opcion = int(input("\nElige una opcion(1-6): "))  

            if opcion == 1:                               
                while not salir_al_menu:                      
                    nombre = pedir_input_texto("\t- Nombra el produco que desea agregar: ") 
                    if inventario.producto_existente(nombre):
                        print("\n\t- El producto existe en el inventario.")
                        if elija_opcion():
                            salir_al_menu = True
                        else:
                            continue
                    break
                    
                if nombre and not salir_al_menu:
                    categoria = pedir_input_texto("\t- Introduzca la categoria: ")
                    if categoria is None:
                        salir_al_menu = True

                    if categoria and not salir_al_menu:
                        precio = pedir_input_float("\t- Precio del producto: ")
                        if precio is None:
                            salir_al_menu = True                   
                        if precio and not salir_al_menu:
                            cantidad = pedir_input_float("\t- Introduzca la cantidad: ")
                            if cantidad is None:
                                salir_al_menu = True
                            if cantidad and not salir_al_menu:
                                producto = Producto(nombre, categoria, precio, cantidad)
                                if inventario.agregar_producto(producto):
                                    print(f"\n- Producto {nombre} agregado al inventario.")

            elif opcion == 2:
                while not salir_al_menu:
                    nombre_producto = pedir_input_texto("\t- Introduzca el producto a actualizar: ")
                    while inventario.producto_existente(nombre_producto):
                        nuevo_precio = pedir_input_float("\t- Nuevo precio (nr): ")
                        if nuevo_precio is None:
                            salir_al_menu = True
                            break                        
                        nueva_cantidad = pedir_input_float("\t- Nueva cantidad (nr): ")
                        if nueva_cantidad is None:
                            salir_al_menu = True
                            break                
                        if nuevo_precio and nueva_cantidad:
                            inventario.actualizar_producto(nombre_producto, nuevo_precio, nueva_cantidad)
                            print(f"\n- Producto {nombre_producto} actualizado.")
                            salir_al_menu = True
                            break
                    else:
                        print("\n\t- Producto no encontrado!")
                        if elija_opcion():
                            salir_al_menu = True

            elif opcion == 3:
                while not salir_al_menu:
                    nombre_producto = input("\t- Nombre del producto a eliminar: ")
                    if inventario.eliminar_producto(nombre_producto):                        
                        print(f"\t- Producto {nombre_producto} eliminado.")
                        break
                    else:
                        print("\n\t- Producto no encontrado.")
                        if elija_opcion():
                            salir_al_menu = True
                            break
            
            elif opcion == 4:
                df_inventario = inventario.mostrar_inventario()
                if df_inventario is None:
                    print("\t- El inventario esta vacio.")
                else:
                    print("\n- Inventario:")
                    df_inventario.index = df_inventario.index + 1
                    print(df_inventario)

            elif opcion == 5:
                while not salir_al_menu:
                    nombre_producto = pedir_input_texto("\t- Nombre del producto a buscar: ")
                    if nombre_producto:
                        producto = inventario.buscar_producto(nombre_producto)
                        if producto:
                            df_producto = producto.mostrar_info()
                            df_producto.index = df_producto.index + 1
                            print(f"\t- Producto {nombre_producto} encontrado: ")
                            print(f"\n{df_producto}")
                            break
                        else:
                            print("\n\t- Producto no encontrado.")
                            if elija_opcion():
                                salir_al_menu = True
                                break
                    else:
                        if elija_opcion():
                            salir_al_menu = True

            elif opcion == 6:
                print("\n\t- Saliendo del programa.")        
                sys.exit()

            else:
                raise ValueError
        except ValueError:
            print("\t- Debe introducir un valor numerico valido.")
            continue
