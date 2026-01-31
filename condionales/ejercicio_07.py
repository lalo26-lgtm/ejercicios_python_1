
base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente > 0:
    resultado = base ** exponente
elif exponente == 0:
    resultado = 1
else:
    resultado = 1 / (base ** abs(exponente))

print("La potencia es:", resultado)
