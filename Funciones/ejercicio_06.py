def calcular_area_perimetro(radio):
    PI = 3.1416
    area = PI * radio ** 2
    perimetro = 2 * PI * radio
    return area, perimetro

radio = float(input("Introduce el radio: "))

resultado = calcular_area_perimetro(radio)
area = resultado[0]
perimetro = resultado[1]

print("Área:", area)
print("Perímetro:", perimetro)



