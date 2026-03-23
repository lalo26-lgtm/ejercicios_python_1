def calcular_factorial(num):
    if num == 1:
        fact = 1
    else:
        fact = num * calcular_factorial(num - 1)
    return fact

numero1 = int(input("Número: "))
print("El factorial es:", calcular_factorial(numero1))
