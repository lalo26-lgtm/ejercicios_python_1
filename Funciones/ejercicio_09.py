def intercambiar(mayor, menor):
    if mayor < menor:
        aux = mayor
        mayor = menor
        menor = aux
    return mayor, menor

def calcular_mcd(num1, num2):
    resultado = intercambiar(num1, num2)
    num1 = resultado[0]
    num2 = resultado[1]
    
    resto = num1 % num2
    
    if resto == 0:
        mcd = num2
    else:
        mcd = calcular_mcd(num2, resto)
        
    return mcd

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

print("MCD:", calcular_mcd(numero1, numero2))