
notas = []
suma = 0

for i in range(1,6):
    numeros = int(input("Coloca tus notas: "))
    notas.append(numeros)
    suma += numeros

mas_alta = max(notas)
print("La calificaciono mas alta fue:",mas_alta)

mas_menos = min(notas)
print("La calificacion mas baja fue:",mas_menos)

print("El promedio de las calificsaciones dadas es:",suma / 5)
