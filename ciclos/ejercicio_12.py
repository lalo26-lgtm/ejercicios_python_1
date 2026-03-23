 
ahorro_acumulado = 0

for mes in range(1, 13):
    cantidad_mensual = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: "))
    ahorro_acumulado += cantidad_mensual
    print(f"En el mes {mes} llevas ahorrado {ahorro_acumulado}")