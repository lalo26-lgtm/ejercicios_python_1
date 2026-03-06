cont_positivos = 0
cont_negativos = 0
cont_ceros = 0

print("¿Cuántos números vas a introducir?:")
cantidad_num = int(input())

for i in range(cantidad_num):
    print("Número ", i + 1 ,":")
    num = int(input())
    if num > 0:
        cont_positivos += 1
    elif num < 0:
        cont_negativos += 1
    else:
        cont_ceros += 1

print("Números positivos:", cont_positivos)
print("Números negativos:", cont_negativos)
print("Números igual a 0:", cont_ceros)