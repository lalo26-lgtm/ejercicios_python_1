frase = input('Ingresa una frase: ')

while True:
    letra_1 = input('Ingresa una letra para reemplazar: ')
    if len(letra_1) == 1:
        break

while True:
    letra_2 = input('Ingresa la letra nueva: ')
    if len(letra_2) == 1:
        break

frase_nueva = ""
for letra in frase:
    if letra == letra_1:
        frase_nueva += letra_2
    else:
        frase_nueva += letra

print("La frase nueva es:\n" + frase_nueva)

frase_2 = frase.replace(letra_1, letra_2)
print("La frase nueva es:\n" + frase_2)

