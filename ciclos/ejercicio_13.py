
horas_acum = 0
sueldo_por_hora = float(input("Introduce el sueldo por hora: "))

for dia in range(1, 7):
    horas = int(input(f"¿Cuántas horas has trabajado el día {dia}?: "))
    horas_acum += horas

print("Horas acumuladas en la semana:", horas_acum)
print("Sueldo:", sueldo_por_hora * horas_acum)