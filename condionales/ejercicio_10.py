x1 = float(input("Dime coordenada x primera circunferencia: "))
y1 = float(input("Dime coordenada y primera circunferencia: "))
r1 = float(input("Dime radio primera circunferencia: "))


x2 = float(input("Dime coordenada x segunda circunferencia: "))
y2 = float(input("Dime coordenada y segunda circunferencia: "))
r2 = float(input("Dime radio segunda circunferencia: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 4. Clasificar según la relación
if distancia > (r1 + r2):
    print("Circunferencias exteriores")
elif distancia == (r1 + r2):
    print("Circunferencias tangentes exteriores")
elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
    print("Circunferencias secantes")
elif distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")
elif distancia > 0 and distancia < abs(r1 - r2):
    print("Circunferencias interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")
