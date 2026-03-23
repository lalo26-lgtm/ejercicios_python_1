def inicializar_pila(pila, size_pila):
    for i in range(size_pila):
        pila[i] = "*"

def longitud_pila(pila, size_pila):
    size = 0
    while size < size_pila and pila[size] != "*":
        size = size + 1
    return size

def esta_vacia_pila(pila, size_pila):
    if longitud_pila(pila, size_pila) == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def esta_llena_pila(pila, size_pila):
    if longitud_pila(pila, size_pila) == size_pila:
        resultado = True
    else:
        resultado = False
    return resultado

def add_pila(cad, pila, size_pila):
    if not esta_llena_pila(pila, size_pila):
        pila[longitud_pila(pila, size_pila)] = cad
    else:
        print("No se puede añadir elemento. La pila está llena")

def sacar_de_la_pila(pila, size_pila):
    if not esta_vacia_pila(pila, size_pila):
        cad = pila[longitud_pila(pila, size_pila) - 1]
        pila[longitud_pila(pila, size_pila) - 1] = "*"
    else:
        print("No se puede sacar elemento. La pila está vacia")
        cad = ""
    return cad

def escribir_pila(pila, size_pila):
    i = 0
    while i < size_pila and pila[i] != "*":
        print(pila[i], end=" ")
        i = i + 1
    print("")

mipila = ["", "", "", "", "", "", "", "", "", ""]
tam_pila = 10
opcion = 0

inicializar_pila(mipila, tam_pila)

while opcion != 5:
    print("1.- Añadir elemento a la pila")
    print("2.- Sacar elemento de la pila")
    print("3.- Longitud de la pila")
    print("4.- Mostrar pila")
    print("5.- Salir")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        elem = input("Dame la cadena para añadir a la pila: ")
        add_pila(elem, mipila, tam_pila)
        
    elif opcion == 2:
        print(sacar_de_la_pila(mipila, tam_pila))
        
    elif opcion == 3:
        print("Longitud:", longitud_pila(mipila, tam_pila))
        
    elif opcion == 4:
        escribir_pila(mipila, tam_pila)
        
    elif opcion == 5:
        pass
        
    else:
        print("Opción incorrecta")