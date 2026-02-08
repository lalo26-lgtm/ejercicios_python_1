
mes = int(input("Introduce el número de mes (1-12): "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("31 días")
elif mes in [4, 6, 9, 11]:
    print("30 días")
elif mes == 2:
    print("28 o 29 días")
else:
    print("Mes incorrecto")
