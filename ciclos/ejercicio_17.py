
horas_acum = 0
trabajadores = int(input("¿Cuántos trabajadores hay en la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

for trabajador in range(1, trabajadores + 1):
    horas_por_trabajador = 0
    dias = int(input(f"¿Cuántos días trabajó el trabajador {trabajador}?: "))
    for dia in range(1, dias + 1):
        horas = int(input(f"Trabajador {trabajador}, horas del día {dia}: "))
        horas_por_trabajador += horas
    print(f"Trabajador {trabajador} → sueldo: {horas_por_trabajador * sueldo_por_hora}")
    horas_acum += horas_por_trabajador

print(f"Pago total a {trabajadores} trabajadores: {horas_acum * sueldo_por_hora}")