
numero = int(input("Coloca un número para calcular su potencia: "))
potencia = int(input("Coloca la potencia para calcular: "))

while potencia <= 0:
    print("La potencia debe ser un número positivo. Inténtalo otra vez.")
    potencia = int(input("Coloca la potencia para calcular: "))

resultado = numero ** potencia
print(f"La potencia de {numero} elevado a {potencia} es: {resultado}")


    