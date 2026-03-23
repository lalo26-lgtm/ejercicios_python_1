# segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
# Parámetros de entrada: dos números
# Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo 
# del segundo, Falso en caso contrario.

def es_multiplo(num1, num2):
    residuo = num1 % num2
    if residuo == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    if es_multiplo(num1, num2):
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")