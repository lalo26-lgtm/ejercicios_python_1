
lista = []
lista_2 = []
lista_3 = []

for i in range(5):
    num = int(input(f"Coloca un valor [{ i + 1 }] del vector:\n"))
    lista.append(num)
    num = int(input(f"Coloca un valor [{ i + 1 }] del vector:5\n"))
    lista_2.append(num)
    lista_3.append(lista[i] + lista_2[i])

print(lista)
print(lista_2)
print(lista_3)