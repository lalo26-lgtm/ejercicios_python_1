peso = int(input("¿Qué peso tiene el paquete (en gramos)?: "))

if peso <= 0 or peso > 5000:
    print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")
else:
    # 3. Mostrar opciones de zona
    print("1.- América del Norte")
    print("2.- América Central")
    print("3.- América del Sur")
    print("4.- Europa")
    print("5.- Asia")

    zona = int(input("¿A qué zona se reparte (1-5)?: "))

    if zona == 1:
        coste = peso * 24
    elif zona == 2:
        coste = peso * 20
    elif zona == 3:
        coste = peso * 21
    elif zona == 4:
        coste = peso * 10
    elif zona == 5:
        coste = peso * 18
    else:
        print("Zona incorrecta.")
        coste = None
if coste is not None:
        print("Coste:", coste, "euros.")
