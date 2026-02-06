num = int(input("Dime un número de dos cifras: "))

decenas = num // 10      # División entera
unidades = num % 10      # Resto de la división

print("Primera cifra (decenas):", decenas)
print("Segunda cifra (unidades):", unidades)

invertido = unidades * 10 + decenas

print("Número invertido:", invertido)
