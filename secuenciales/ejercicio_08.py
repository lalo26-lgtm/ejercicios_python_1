sueldo_base = int(input("Dime el sueldo base: "))
venta1 = int(input("Dime precio de la venta 1: "))
venta2 = int(input("Dime precio de la venta 2: "))
venta3 = int(input("Dime precio de la venta 3: "))
comision = venta1 * 0.10 + venta2 * 0.10 + venta3 * 0.10
print("Comisión por ventas:", comision)
sueldo_total = sueldo_base + comision
print("Sueldo total:", sueldo_total)


