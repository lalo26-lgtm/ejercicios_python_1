a = int(input("Introduce valor de la variable A: "))
b = int(input("Introduce valor de la variable B: "))

aux = a
a = b
b = aux

print("Nuevo valor de A:", a)
print("Nuevo valor de B:", b)
