import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 10))

for n in numeros:
    print(n, 'su cuadrado:', n ** 2, 'su cubo:', n ** 3)

