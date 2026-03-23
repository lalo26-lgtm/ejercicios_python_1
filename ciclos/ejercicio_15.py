mes = 20
total = 0
for i in range(1, 20 + 1):
    pago = int(input(f"Cuanto pagas en el mes:{i} "))
    total = pago ** mes
print(f"El tolat de la deuda es {total}")