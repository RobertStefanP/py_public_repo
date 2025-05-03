# Calculadora con Funciones

def suma(nr_1, nr_2):
    return nr_1 + nr_2

def resta(nr_1, nr_2):
    return nr_1 - nr_2
   
def multiplica(nr_1, nr_2):
    return nr_1 * nr_2

def dividir(nr_1, nr_2):
    return nr_1 / nr_2

def elija_numeros():
    nr_1 = int(input("Introduzca primer numero: "))
    nr_2 = int(input("Introduzca segundo numero: "))
    return nr_1, nr_2

if __name__ == '__main__':
    while True:
        print("""\nOperaciones que se pueden realizar:             
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Salir
            """)
        opcion = int(input("Escoja una opcion(1-5): "))
        
        if opcion == 1:
            print("\nSumando: ")    
            nr_1, nr_2 = elija_numeros()
            print(f"\n{nr_1} + {nr_2} = {suma(nr_1, nr_2)}")
        elif opcion == 2:
            print("\nRestando:")
            nr_1, nr_2 = elija_numeros()
            print(f"\n{nr_1} - {nr_2} = {resta(nr_1, nr_2)}")
        elif opcion == 3:
            print("\nMultiplicando:")
            nr_1, nr_2 = elija_numeros()
            print(f"\n{nr_1} * {nr_2} = {multiplica(nr_1, nr_2)}")
        elif opcion == 4:
            print("\nDividiendo:")
            nr_1, nr_2 = elija_numeros()
            print(f"\n{nr_1} / {nr_2} = {dividir(nr_1, nr_2):.2f}")        
        elif opcion == 5:
            print("Saliendo del calculadora.")
            break
        else:
            print("No valido.")
