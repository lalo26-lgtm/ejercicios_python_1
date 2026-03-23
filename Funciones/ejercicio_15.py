def inicializar_cola(cola, size_cola):
    for i in range(size_cola):
        cola[i] = "*"

def longitud_cola(cola, size_cola):
    size = 0
    while size < size_cola and cola[size] != "*":
        size = size + 1
    return size

def esta_vacia_cola(cola, size_cola):
    if longitud_cola(cola, size_cola) == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def esta_llena_cola(cola, size_cola):
    if longitud_cola(cola, size_cola) == size_cola:
        resultado = True
    else:
        resultado = False
    return resultado

def add_cola(cad, cola, size_cola):
    if not esta_llena_cola(cola, size_cola):
        cola[longitud_cola(cola, size_cola)] = cad
    else:
        print("No se puede añadir elemento. La cola está llena")

def sacar_de_la_cola(cola, size_cola):
    if not esta_vacia_cola(cola, size_cola):
        cad = cola[0]
        for i in range(size_cola - 1):
            cola[i] = cola[i + 1]
        cola[size_cola - 1] = "*"
    else:
        print("No se puede sacar elemento. La cola está vacia")
        cad = ""
    return cad

def escribir_cola(cola, size_cola):
    i = 0
    while i < size_cola and cola[i] != "*":
        print(cola[i], end=" ")
        i = i + 1
    print("")

micola = ["", "", ""]
tam_cola = 3
opcion = 0

inicializar_cola(micola, tam_cola)

while opcion != 5:
    print("1.- Añadir elemento a la cola")
    print("2.- Sacar elemento de la cola")
    print("3.- Longitud de la cola")
    print("4.- Mostrar cola")
    print("5.- Salir")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        elem = input("Dame la cadena para añadir a la cola: ")
        add_cola(elem, micola, tam_cola)
        
    elif opcion == 2:
        print(sacar_de_la_cola(micola, tam_cola))
        
    elif opcion == 3:
        print("Longitud:", longitud_cola(micola, tam_cola))
        
    elif opcion == 4:
        escribir_cola(micola, tam_cola)
        
    elif opcion == 5:
        pass
        
    else:
        print("Opción incorrecta")