
import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1,1000))

print(numeros)
numeros.sort()
print(numeros)

