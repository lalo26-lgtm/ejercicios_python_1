frase = input('Ingresa una frase: ')
word = input('Ingresa una palabra: ')

if word in frase:
    print(frase.replace(word, f'"{word}"'))
else:
    print('La palabra no se encuentra en la frase.')
   