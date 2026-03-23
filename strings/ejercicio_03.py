cadena = input('Ingresa una cadena: ')
caracter = input('Ingresa un caracter: ')

repetidas = 0
for i in cadena:
    if i == caracter:
        repetidas += 1

print(f"La letra {caracter} se encuentra {repetidas} veces en la cadena: {cadena}")

