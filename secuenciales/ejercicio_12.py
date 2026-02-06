import math

x1 = int(input("Dime la coordenada x del punto 1: "))
y1 = int(input("Dime la coordenada y del punto 1: "))

x2 = int(input("Dime la coordenada x del punto 2: "))
y2 = int(input("Dime la coordenada y del punto 2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distancia:", distancia)

