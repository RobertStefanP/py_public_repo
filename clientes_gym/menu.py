import re

from cliente_dao import ClienteDAO
from cliente import Cliente

class Menu:
    
    def seleccionar_opcion(self):
        salir = False
        while not salir:
            print("""Menu Clientes Gym:
                    1. Listar clientes
                    2. Insertar cliente
                    3. Actualizar cliente
                    4. Eliminar cliente
                    5. Salir""")            
            try:  
                opcion = int(input("Elige un opcion: "))                  
                if opcion == 1:
                    self.listar_clientes()
                elif opcion == 2:
                    self.insertar_cliente()
                elif opcion == 3:
                    self.actualizar_cliente()
                elif opcion == 4:
                    self.eliminar_cliente()
                elif opcion == 5:
                    print("Saliendo del programa.")
                    salir = True
                else:
                    print("Introduzca un numero de 1 a 5.")
            except ValueError:
                print(f"Opcion no valida, introducir un numero (1-5).")
            
    def listar_clientes(self):
        clientes = ClienteDAO.seleccionar()
        if clientes is not None:
            for cliente in clientes:
                print(cliente)
                
    def insertar_cliente(self):
        print("Alta nuevo cliente.")
        nombre_var = self.comprobar_texto("Nombre: ")       
        apellido_var = self.comprobar_texto("Apellido: ")
        membresia_var = self.comprobar_numero("Membresia: ", typo='membresia')
        nuevo_cliente = Cliente(nombre=nombre_var,
                                apellido=apellido_var, 
                                membresia=membresia_var)
        cliente = ClienteDAO.insertar(nuevo_cliente)
        print(f"Cliente agregado: {cliente}")
        print(f"Nuevo cliente: {nombre_var} {apellido_var}, "
              f"Membresia: {membresia_var}")
    
    def actualizar_cliente(self):
        print("Actualizando cliente:")
        id_cliente = self.comprobar_numero("El id del cliente: ")         
        nombre = self.comprobar_texto("Actualizar nombre: ")
        apellido = self.comprobar_texto("Actualizar apellido: ")
        membresia = self.comprobar_numero("Actualizar membresia: ", typo='membresia')    
        cliente_actualizar = Cliente(id_cliente, nombre, apellido, membresia)
        cliente_actualizado = ClienteDAO.actualizar(cliente_actualizar)
        print(f"Cliente actualizado: {cliente_actualizado}")
        print(f"Nuevos detalles: {nombre} {apellido}, Membresia: {membresia}")
        
    def eliminar_cliente(self):
        print("Eliminando cliente.")
        id_cliente = self.comprobar_numero("El id del cliente: ")
        eliminar_cliente = Cliente(id=id_cliente)
        cliente_eliminado = ClienteDAO.eliminar(eliminar_cliente)
        print(f"Cliente eliminado: {cliente_eliminado}")
    
    def comprobar_texto(self, texto):
        try:
            while True:
                entrada = input(texto).strip()
                if (re.match(r'^[a-zA-Z ]+$', entrada) and 
                    len(re.sub(r'[^a-zA-Z]', "", entrada)) >= 3):
                    return entrada                
                else:
                    print("No valido, al menos 3 caracteres,letras y espacios")                                                
        except Exception as e:
            print(f"Error al comprobar el texto: {e}")    
                    
    def comprobar_numero(self, numero, typo=None):
        try:
            while True:
                entrada = input(numero)
                if entrada.isdigit():
                    numr = int(entrada)
                    if typo == 'membresia' and (numr % 100 != 0):
                        print("Membresia tiene que ser un divisor de 100.")
                        continue
                    return numr
                else:
                    print(f"No valido, introduzca un numero.")
        except Exception as e:
            print(f"Error al comprobar el numero: {e}")                        
                                      
if __name__ == '__main__':
    menu = Menu()
    menu.seleccionar_opcion()
    