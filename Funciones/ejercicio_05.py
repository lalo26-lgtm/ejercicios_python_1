import random

def calcular_max_min(vector, size):
    vmax = vector[0]
    vmin = vector[0]
    
    for i in range(size):
        if vmax < vector[i]:
            vmax = vector[i]
        if vmin > vector[i]:
            vmin = vector[i]
            
    return vmax, vmin

size_lista = 10
lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(size_lista):
    lista[i] = random.randint(1, 100)
    
resultado = calcular_max_min(lista, size_lista)

vmax = resultado[0]
vmin = resultado[1]

print("El valor máximo es", vmax)
print("El valor mínimo es", vmin)