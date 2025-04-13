import re
import sys

from inventario import Producto, Inventario


def elija_opcion(): 
#    while True:
    #print("  Elija opcion:")  
    print("\t  1 -Reintentar.\n\t  2 -Salir.\n") 
    opcion = input("\t- Elija 1 o 2: ")
    if opcion == "1":
        return 'reintentar'
    elif opcion == "2":
#        print("Volver al menu.")
        nombre = None 
        categoria = None                              
        return 'salir'
    else:
        print("\n\t- No valido, elegir 1 o 2.")
        return 'error'
    # if volver_al_menu:  
    #     return ''
    #return 'error'
   


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
                nombre = input("\t- Nombra el produco que desea agregar: ") 
                if inventario.producto_existente(nombre):  
                    print("\n\t- El producto ya existe en el inventario.")                                                         
                    while True:                        
                        mensaje = elija_opcion()
                        if mensaje == 'reintentar':
                            print(f"\t- {mensaje.title()}")
                            break
                        if mensaje == 'salir':
                            print(f"\t- {mensaje.title()}")
                            salir_al_menu = True
                            break
                        elif mensaje == 'error':
                            print(f"\t- {mensaje.title()}")
                            continue                                             
                        salir_al_menu = True                                
                        if salir_al_menu:  
                            break
                    if salir_al_menu:  
                        break
                else:    
                    if re.fullmatch(r"[a-zA-Z0-9\s]+", nombre) and nombre.strip() != "":
                            break                         
                    else: 
                        print("\n\t- El espacio no puede ser vacio o tener caracteres especiales.") 
                                                       
            if nombre and not salir_al_menu:                                                                                   
                while not salir_al_menu:         
                    
                    
                    
                    
                    
                    
                               
                    categoria = input("\t- Introduzca la categoria: ")                                                          
                    if re.fullmatch(r"[a-zA-Z0-9\s]+", categoria) and categoria.strip() != "":
                        break
                    else:
                        print("\n\t- El espacio no puede ser vacio o tener caracteres especiales.")                         
                        while True:
                            
                            mensaje = elija_opcion()
                            if mensaje == 'reintentar':
                                print(f"\t- {mensaje.title()}")
                                break
                            if mensaje == 'salir':
                                print(f"\t- {mensaje.title()}")
                                salir_al_menu = True
                                break
                            elif mensaje == 'error':
                                print(f"\t- {mensaje.title()}")
                                continue                                             
                            salir_al_menu = True       
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            # print(" 1 -Reintentar.\n 2 -Volver.\n")
                            # reintento_o_menuprincipal = input("  Opcion 1 o 2: ")
                                            
                            # if reintento_o_menuprincipal == "1":
                            #     break                                
                            # elif reintento_o_menuprincipal == "2":
                            #     print("Volviendo al menú principal")
                            #     categoria = None
                            #     volver_al_menu = True
                            #     break                                                                        
                            # else:
                            #     print("--ERROR! Elija 1 o 2.")
                            #     continue                  
                            salir_al_menu = True 
                    if salir_al_menu:
                        break  
                                                                     
                if nombre and categoria and not salir_al_menu:  
                    while not salir_al_menu:
                        try:                                    
                            precio = input("\t- Precio del producto: ")                     
                            if int(precio) > 0 and precio.isnumeric():
                                break 
                            else:                                
                                while True: 
                                    print("1 -Reintentar.\n2 -Volver.")
                                    reintentar_o_menu = input("\n   Opcion 1 o 2: ")

                                    if reintentar_o_menu == "1":
                                        break  
                                    elif reintentar_o_menu == "2":
                                        print("Volviendo al menu principal.")
                                        precio = None
                                        salir_al_menu = True
                                        break  
                                    else:
                                        print("--ERROR! Elija 1 o 2")
                                        continue                                                                             
                            if salir_al_menu: 
                                break                                
                        except ValueError:
                            print("\n\t - Introducir un valor numerico valido.")                                                                             
                            while True: 
                                print("1 -Reintentar. \n2 -Volver.")
                                reintentar_o_menu = input("\n   Elija 1 o 2: ")

                                if reintentar_o_menu == "1":
                                    break  
                                elif reintentar_o_menu == "2":
                                    print("Volviendo al menu principal.")
                                    precio = None
                                    salir_al_menu = True
                                    break  
                                else:
                                    print("-ERROR! Opcion no valida, elija 1 o 2.")
                                    continue           
                                                            
                    if precio is not None and not salir_al_menu:
                        cantidad = None  
                        while not salir_al_menu:  
                            try:
                                cantidad = float(input("\t- Introduzca la cantidad: ")) 
                                if cantidad > 0:
                                    break  
                                else:
                                    print("-La cantidad no puede ser 0 o negativa.")
                            
                                    while True:  
                                        print("1 -Reintentar.\n2 -Volver.")
                                        reintentar_o_menu = input("\n   Elija 1 o 2: ")

                                        if reintentar_o_menu == "1":                                            
                                            break 
                                        elif reintentar_o_menu == "2":
                                            print("Volviendo al menú principal.")
                                            cantidad = None  
                                            salir_al_menu = True
                                            break  
                                        else:
                                            print("-ERROR! Opción no válida, elija 1 o 2.")
                                            continue                              
                                if salir_al_menu:
                                    break                                
                            except ValueError:
                                print("-Introducir un valor numerico valido.")                                
                    if precio is not None and cantidad is not None:
                        producto = Producto(nombre, categoria, precio, cantidad)  
                        if inventario.agregar_producto(producto):  
                            print(f"\nProducto '{nombre}' agregado correctamente al inventario.") 
                        else:
                            print(f"-El producto '{producto.get_nombre()}' ya existe en el inventario.")                             
                        inventario.mostrar_inventario()  
                                                                 
        elif opcion ==2:                                                       
            while not salir_al_menu:
                try:
                    nombre_producto = input("\n  Introduzca el nombre del producto a actualizar: ")            
                    if inventario.producto_existente(nombre_producto): 
                        while True:                                                                   
                            nuevo_precio = input("  Introduzca el nuevo precio (dejar vacío para no cambiar): ")
                            
                            if nuevo_precio.strip() == "":
                                nuevo_precio = None
                                break
                            try:
                                nuevo_precio = float(nuevo_precio)
                                if nuevo_precio == 0:
                                    print("- El precio no puede ser 0. Inténtelo de nuevo.")
                                    continue  
                                else:
                                    break  
                            except ValueError:
                                print("\n-Debe introducir un valor numérico válido.")
                                continue  
                        while True:    
                            nueva_cantidad = input("\n  Introduzca la nueva cantidad (dejar vacío para no cambiar): ")
                            
                            if nueva_cantidad.strip() == "":
                                nueva_cantidad = None
                                break 
                            try:
                                nueva_cantidad = float(nueva_cantidad)
                                if nueva_cantidad <= 0:
                                    print("- La cantidad debe ser mayor que 0. Inténtelo de nuevo.")
                                    continue
                                else:
                                    break                                
                            except ValueError:
                                print("- Debe introducir un valor numérico válido.")                                                                                
                        inventario.actualizar_producto(nombre_producto, nuevo_precio, nueva_cantidad)
                        print(f"Producto '{nombre_producto}' actualizado correctamente.")
                        break                                 
                    else:
                        while True: 
                            print("\n-ERROR! Producto no encontrado!")
                            print("\n 1 -Reintentar.\n 2 -Volver.")
                            reintento_o_menuprincipal = input("\n   Elija 1 o 2: ")
                            if reintento_o_menuprincipal == "1":                                
                                break
                            elif reintento_o_menuprincipal == "2":
                                print("Volviendo al menu principal.")
                                salir_al_menu = True
                                break
                            else:
                                print("-ERROR! Opcion no valida, elige 1 o 2.")
                                continue
                    if salir_al_menu:
                        break                                         
                except ValueError:
                    print("-ERROR! Debe introducir un valor numérico válido.")    
                                                                                                         
        elif opcion == 3:
            while not salir_al_menu:                
                nombre_producto = input("  Introduzca el nombre del producto que desea eliminar: ")                   
                if inventario.eliminar_producto(nombre_producto):
                    print(f"Producto '{nombre_producto}' eliminado correctamente.")
                    break
                else:
                    while True:
                        print("\n-ERROR! Producto no encontrado!")
                        print(" 1 -Reintentar.\n 2 -Volver.")
                        reintento_o_menuprincipal = input("\n   Elija 1 o 2: ")
                        if reintento_o_menuprincipal == "1":
                            break  
                        elif reintento_o_menuprincipal == "2":
                            salir_al_menu = True
                            print("Volviendo al menu principal.")
                            break  
                        else:
                            print("-ERROR! Opción no válida, elige 1 o 2.")
                            continue                            
                if salir_al_menu:
                    break                    
                           
        elif opcion == 4:
            inventario_actual = inventario.mostrar_inventario()            
            if not inventario_actual: 
                print("\n  El inventario está vacío.")                
            else:                
                print("\n  Inventario:")
                for producto in inventario_actual:
                    producto.mostrar_info()  
                    
        elif opcion == 5:
            while not salir_al_menu:                
                nombre_producto = input("  Introduzca el nombre del producto que desea buscar: ")
                producto = inventario.buscar_producto(nombre_producto) 
                if producto:                      
                    producto.mostrar_info() 
                    break                  
                else:                         
                    while True:
                        print("\n-ERROR! Producto no encontrado!")
                        print(" 1 -Reintentar.\n 2 -Volver.")
                        reintento_o_menuprincipal = input("\n   Elija 1 o 2: ")
                        if reintento_o_menuprincipal == "1":
                            break  
                        elif reintento_o_menuprincipal == "2":
                            salir_al_menu = True
                            print("Volviendo al menú principal.")
                            break  
                        else:
                            print("-ERROR! Opción no válida, elige 1 o 2.")
                            continue
                if salir_al_menu:  
                    break           
                                                        
        elif opcion == 6:  
            print("  Saliendo del programa.")
            sys.exit()            
        else:
            print("-ERROR! Debe introducir un número válido del 1 al 6.")                                
    except ValueError:
        print("-ERROR! Debe introducir un numero.")
        