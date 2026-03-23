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

def simplificar_fraccion(num, den):
    mcd = calcular_mcd(num, den)
    num = int(num / mcd)
    den = int(den / mcd)
    return num, den

def leer_fraccion():
    num = int(input("Numerador: "))
    den = int(input("Denominador: "))
    resultado = simplificar_fraccion(num, den)
    return resultado[0], resultado[1]

def escribir_fraccion(num, den):
    if den != 1:
        print(num)
        print("---")
        print(den)
    else:
        print("")
        print(num)
        print("")

def sumar_fracciones(n1, d1, n2, d2):
    nr = n1 * d2 + d1 * n2
    dr = d1 * d2
    resultado = simplificar_fraccion(nr, dr)
    return resultado[0], resultado[1]

def restar_fracciones(n1, d1, n2, d2):
    nr = n1 * d2 - d1 * n2
    dr = d1 * d2
    resultado = simplificar_fraccion(nr, dr)
    return resultado[0], resultado[1]

def multiplicar_fracciones(n1, d1, n2, d2):
    nr = n1 * n2
    dr = d1 * d2
    resultado = simplificar_fraccion(nr, dr)
    return resultado[0], resultado[1]

def dividir_fracciones(n1, d1, n2, d2):
    nr = n1 * d2
    dr = d1 * n2
    resultado = simplificar_fraccion(nr, dr)
    return resultado[0], resultado[1]

opcion = 0
num1 = 0
den1 = 0
num2 = 0
den2 = 0

while opcion != 5:
    print("1.- Sumar dos fracciones")
    print("2.- Restar dos fracciones")
    print("3.- Multiplicar dos fracciones")
    print("4.- Dividir dos fracciones")
    print("5.- Salir")
    opcion = int(input("Elige una opción: "))
    
    if opcion != 5:
        print("Fracción 1:")
        resultado1 = leer_fraccion()
        num1 = resultado1[0]
        den1 = resultado1[1]
        
        print("Fracción 2:")
        resultado2 = leer_fraccion()
        num2 = resultado2[0]
        den2 = resultado2[1]
        
    if opcion == 1:
        print("Sumar fracciones")
        resr = sumar_fracciones(num1, den1, num2, den2)
        numr = resr[0]
        denr = resr[1]
        escribir_fraccion(numr, denr)
        
    elif opcion == 2:
        print("Restar fracciones")
        resr = restar_fracciones(num1, den1, num2, den2)
        numr = resr[0]
        denr = resr[1]
        escribir_fraccion(numr, denr)
        
    elif opcion == 3:
        print("Multiplicar fracciones")
        resr = multiplicar_fracciones(num1, den1, num2, den2)
        numr = resr[0]
        denr = resr[1]
        escribir_fraccion(numr, denr)
        
    elif opcion == 4:
        print("Dicidir fracciones")
        resr = dividir_fracciones(num1, den1, num2, den2)
        numr = resr[0]
        denr = resr[1]
        escribir_fraccion(numr, denr)
        
    elif opcion == 5:
        pass
        
    else:
        print("Opción incorrecta")