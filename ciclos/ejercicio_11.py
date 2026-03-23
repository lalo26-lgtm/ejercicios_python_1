
numero = int(input("Introduce un número: "))

if numero <= 1:
    print(f"{numero} no es primo.")
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")