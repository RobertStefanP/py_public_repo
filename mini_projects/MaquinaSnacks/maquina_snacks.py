maquina_snacks = [
    {"id": '1', "producto": "Papas", "precio": 30},
    {"id": '2', "producto": "Refresco", "precio": 50},
    {"id": '3', "producto": "Chocolate", "precio": 100},
    {"id": '4', "producto": "Sandwich", "precio": 120},
]
compras = []

def mostrar_snacks():
    print("Snacks disponibles:")
    for producto in maquina_snacks:      
        print(f"Id: {producto.get('id')} -> {producto.get('producto')} - Precio: {producto.get('precio')}")
    
def comprar_snack():   
    while True:
        id_snack = input("Introduzca el id del snack (s/salir): ")
        if id_snack != 's':
            if id_snack == '0':
                print(f"El id {id_snack} no partenece a ningun producto.")
                break
            else:
                for producto in maquina_snacks:
                    if id_snack == producto.get('id'):
                        compras.append(producto)
                        print(f"{producto.get('producto')} con el coste {producto.get('precio')}, anadido al carrito.")
                        continue
        else:
            print("Abandonando la compra!")
            break

def mostrar_ticket():
    total = 0
    for producto in compras:
        print(f" - {producto.get('producto')} - {producto.get('precio')}")         
        total += producto.get('precio')
    print(f"Total a pagar -> {total}")
    

if __name__ == '__main__':
    while True:
        print("""
        Menu:
              1. Mostrar Snacks
              2. Comprar Snack
              3. Mostrar ticket
              4. salir
        """)
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Regresa Pronto.")
            break
        else:
            print("Opcion no valida.")
            continue
