dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    dias_del_mes = 31
elif mes in [4, 6, 9, 11]:
    dias_del_mes = 30
elif mes == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("Fecha incorrecta (mes inválido).")
    exit()

if dia < 1 or dia > dias_del_mes:
  print("Fecha incorrecta.")
else:
    print("Fecha correcta.")
